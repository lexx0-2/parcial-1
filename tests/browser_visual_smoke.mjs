import { chromium } from "playwright";

const base = process.env.APP_URL || "http://127.0.0.1:5000";
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
const failures = [];
page.on("pageerror", error => failures.push(error.message));

async function waitForPlot(selector) {
  await page.waitForFunction(
    sel => {
      const el = document.querySelector(sel);
      return Boolean(el && el._fullLayout && el.data);
    },
    selector,
    { timeout: 20000 }
  );
}

try {
  for (let module = 7; module <= 14; module++) {
    await page.goto(`${base}/modulo/${String(module).padStart(2, "0")}/`, { waitUntil: "domcontentloaded" });
    await page.waitForFunction(() => Boolean(window.Plotly), null, { timeout: 20000 });
    await waitForPlot("#plot");

    if (module !== 7) await waitForPlot("#methodDiagram");

    if (module === 13) {
      const before = await page.locator("#methodDiagram").evaluate(el => el.data?.[0]?.type);
      await page.locator("#shape").selectOption("semicircle");
      await page.waitForFunction(() => document.querySelector("#methodDiagram")?._fullLayout?.scene);
      const after = await page.locator("#methodDiagram").evaluate(el => el.data?.[0]?.type);
      if (before !== "surface" || after !== "surface") throw new Error("Módulo 13: no se renderizó la superficie 3D de secciones.");
    }

    if (module === 14) {
      await page.locator("#method").selectOption("washer");
      await page.waitForFunction(() => document.querySelector("#methodDiagram")?._fullLayout?.scene);
      let types = await page.locator("#methodDiagram").evaluate(el => (el.data || []).map(t => t.type));
      if (!types.includes("surface")) throw new Error("Módulo 14: no se renderizó el sólido 3D de arandelas.");
      await page.locator("#method").selectOption("shell");
      await page.waitForFunction(() => document.querySelector("#methodDiagram")?._fullLayout?.scene);
      types = await page.locator("#methodDiagram").evaluate(el => (el.data || []).map(t => t.type));
      if (!types.includes("surface")) throw new Error("Módulo 14: no se renderizó la capa cilíndrica 3D.");
      await page.locator("#method").selectOption("disk");
      await page.waitForFunction(() => document.querySelector("#methodDiagram")?._fullLayout?.scene);
    }

    console.log(`OK módulo ${module}: gráfica 2D creada${module === 7 ? "" : " y esquema visual creado"}`);
  }

  if (failures.length) throw new Error("Errores JavaScript del navegador: " + failures.join(" | "));
  console.log("OK: sin errores JavaScript no controlados en los módulos 7–14.");
} finally {
  await browser.close();
}

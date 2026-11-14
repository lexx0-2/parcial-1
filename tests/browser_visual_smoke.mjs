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
  for (let module = 1; module <= 14; module++) {
    await page.goto(`${base}/modulo/${String(module).padStart(2, "0")}/`, { waitUntil: "domcontentloaded" });
    await page.waitForFunction(() => Boolean(window.Plotly), null, { timeout: 20000 });
    await waitForPlot("#plot");

    if (module >= 1 && module <= 5) {
      await page.waitForFunction(() => {
        const el = document.querySelector("#result");
        return Boolean(el && el.textContent.trim().length > 0);
      });
      const traces = await page.locator("#plot").evaluate(el => el.data || []);
      if (traces.length < 2) throw new Error(`Módulo ${module}: la gráfica no contiene las trazas esperadas.`);
      console.log(`OK módulo ${module}: gráfico 2D y resultado calculado`);
      continue;
    }
    if (module === 6) {
      await page.waitForFunction(() => {
        const el = document.querySelector("#solverResult");
        return Boolean(el && el.textContent.trim().length > 0);
      });
      const names = await page.locator("#plot").evaluate(el => (el.data || []).map(trace => trace.name));
      if (!names.includes("f(x)") || !names.includes("F(x)")) throw new Error("Módulo 6: deben aparecer f(x) y F(x).");
      console.log("OK módulo 6: gráficas de f(x), F(x) y solucionador");
      continue;
    }

    if (module !== 7) await waitForPlot("#methodDiagram");

    if (module === 7) {
      const hasAntiderivative = await page.locator("#plot").evaluate(el =>
        (el.data || []).some(trace => trace.name === "Primitiva F(x)")
      );
      if (!hasAntiderivative) throw new Error("Módulo 7: falta la curva de la primitiva.");
    }

    if (module === 13) {
      const before = await page.locator("#methodDiagram").evaluate(el => el.data?.[0]?.type);
      await page.locator("#shape").selectOption("semicircle");
      await page.waitForFunction(() => document.querySelector("#methodDiagram")?._fullLayout?.scene);
      const after = await page.locator("#methodDiagram").evaluate(el => el.data?.[0]?.type);
      if (before !== "surface" || after !== "surface") throw new Error("Módulo 13: no se renderizó la superficie 3D de secciones.");
    }

    if (module === 14) {
      await page.locator("#expr").fill("x+2");
      await page.locator("#a").fill("0");
      await page.locator("#b").fill("2");
      await page.locator("#inner").fill("x");
      await page.locator("#method").selectOption("washer");
      await page.locator("button[onclick='calculateVolume()']").click();
      await page.waitForFunction(() => document.querySelector("#methodDiagram")?._fullLayout?.scene);
      let types = await page.locator("#methodDiagram").evaluate(el => (el.data || []).map(t => t.type));
      if (!types.includes("surface")) throw new Error("Módulo 14: no se renderizó el sólido 3D de arandelas.");
      const innerTrace = await page.locator("#plot").evaluate(el => el.data.find(t => t.name === "Radio interior r(x)")?.y);
      if (!innerTrace || Math.abs(innerTrace[0]) > 1e-6 || Math.abs(innerTrace.at(-1) - 2) > 1e-5) {
        throw new Error("Módulo 14: la gráfica no interpretó g(x)=x como radio interior variable.");
      }
      await page.locator("#inner").fill("x+3");
      await page.locator("button[onclick='calculateVolume()']").click();
      await page.waitForFunction(() => document.querySelector("#result")?.textContent.includes("radio interior"));
      await page.locator("#inner").fill("x");
      await page.locator("#method").selectOption("shell");
      await page.waitForFunction(() => document.querySelector("#methodDiagram")?._fullLayout?.scene);
      types = await page.locator("#methodDiagram").evaluate(el => (el.data || []).map(t => t.type));
      if (!types.includes("surface")) throw new Error("Módulo 14: no se renderizó la capa cilíndrica 3D.");
      await page.locator("#method").selectOption("disk");
      await page.waitForFunction(() => document.querySelector("#methodDiagram")?._fullLayout?.scene);
    }

    console.log(`OK módulo ${module}: gráfica 2D creada y procedimiento visual activo`);
  }

  if (failures.length) throw new Error("Errores JavaScript del navegador: " + failures.join(" | "));
  console.log("OK: sin errores JavaScript no controlados en los módulos 1–14.");
} finally {
  await browser.close();
}

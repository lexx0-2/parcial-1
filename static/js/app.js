async function postJSON(url,body){const r=await fetch(url,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});const d=await r.json();if(!r.ok||!d.ok)throw new Error(d.error||"Error de procesamiento.");return d}
function makeX(a,b,n=250){const x=[];for(let i=0;i<=n;i++)x.push(a+(b-a)*i/n);return x}
function processFormula(e){return postJSON("/api/parse",{expression:e})}
function sampleFormula(e,x){return postJSON("/api/sample",{expression:e,x})}
function integrateFormula(e,a,b){return postJSON("/api/integrate",{expression:e,a,b})}
function toggleTheme(){const d=document.documentElement;d.classList.toggle("dark");localStorage.setItem("theme",d.classList.contains("dark")?"dark":"light");updateThemeButton()}
function updateThemeButton(){const b=document.getElementById("themeToggle");if(b)b.textContent=document.documentElement.classList.contains("dark")?"☀️ Modo claro":"🌙 Modo oscuro"}
function loadTheme(){if(localStorage.getItem("theme")==="dark")document.documentElement.classList.add("dark");updateThemeButton()}
function renderFormula(){if(window.renderMathInElement)renderMathInElement(document.body,{delimiters:[{left:"\\[",right:"\\]",display:true},{left:"\\(",right:"\\)",display:false}]})}
document.addEventListener("DOMContentLoaded",loadTheme);

const titles = {
 dashboard: "Dashboard Overview",
 forecast: "Water Demand Forecast",
 model: "Model Training & Evaluation",
 agents: "Intelligent Agent Centre",
 allocation: "Water Allocation Optimizer",
 data: "Dataset Manager",
 about: "Project Details"
};

function showPage(id) {
 document.querySelectorAll(".page").forEach(p =>
  p.classList.toggle("active", p.id === id)
 );

 document.querySelectorAll(".nav button").forEach(b =>
  b.classList.toggle("active", b.dataset.page === id)
 );

 document.getElementById("pageTitle").textContent = titles[id];

 if (id === "dashboard") drawTrend();
 if (id === "forecast") drawForecastChart();
}

document.querySelectorAll(".nav button").forEach(b =>
 b.addEventListener("click", () => showPage(b.dataset.page))
);

function drawLine(canvasId, labels, values, forecastStart) {
 const c = document.getElementById(canvasId);
 if (!c) return;

 const rect = c.getBoundingClientRect();
 const w = Math.max(300, rect.width);
 const h = 245;
 const dpr = window.devicePixelRatio || 1;

 c.width = w * dpr;
 c.height = h * dpr;

 const ctx = c.getContext("2d");
 ctx.scale(dpr, dpr);

 const pad = { l: 42, r: 15, t: 15, b: 32 };
 const cw = w - pad.l - pad.r;
 const ch = h - pad.t - pad.b;

 const min = Math.min(...values) - 8;
 const max = Math.max(...values) + 8;

 ctx.strokeStyle = "#e8eef3";
 ctx.lineWidth = 1;

 for (let i = 0; i < 5; i++) {
  let y = pad.t + i * ch / 4;

  ctx.beginPath();
  ctx.moveTo(pad.l, y);
  ctx.lineTo(w - pad.r, y);
  ctx.stroke();

  ctx.fillStyle = "#8293a3";
  ctx.font = "10px Arial";

  ctx.fillText(
   (max - (max - min) * i / 4).toFixed(0),
   5,
   y + 3
  );
 }

 const x = i => pad.l + i * cw / (values.length - 1);
 const y = v => pad.t + (max - v) * ch / (max - min);

 ctx.strokeStyle = "#1677c8";
 ctx.lineWidth = 2.5;
 ctx.beginPath();

 values.forEach((v, i) => {
  if (i === 0) {
   ctx.moveTo(x(i), y(v));
  } else if (i === forecastStart) {
   ctx.moveTo(x(i), y(v));
  } else {
   ctx.lineTo(x(i), y(v));
  }
 });

 ctx.stroke();

 if (forecastStart < values.length) {
  ctx.strokeStyle = "#22b8cf";
  ctx.setLineDash([5, 4]);
  ctx.beginPath();

  for (let i = forecastStart; i < values.length; i++) {
   if (i === forecastStart) {
    ctx.moveTo(x(i), y(values[i]));
   } else {
    ctx.lineTo(x(i), y(values[i]));
   }
  }

  ctx.stroke();
  ctx.setLineDash([]);
 }

 ctx.fillStyle = "#8293a3";
 ctx.font = "10px Arial";

 labels.forEach((lab, i) => {
  if (i % 2 === 0 || i === labels.length - 1) {
   ctx.fillText(lab, x(i) - 8, h - 8);
  }
 });
}

function drawTrend() {
 drawLine(
  "trendChart",
  ["2000", "2004", "2008", "2012", "2016", "2020", "2024", "2027", "2030"],
  [80, 84, 87, 91, 95, 101, 108, 117, 126],
  6
 );
}

function drawForecastChart() {
 drawLine(
  "forecastChart",
  ["2020", "2022", "2024", "2026", "2028", "2030"],
  [101, 104, 108, 113, 119, 125],
  3
 );
}

function runForecast() {
 const country =
  document.getElementById("country").value || "Selected region";

 const year = +document.getElementById("year").value;
 const pop = +document.getElementById("population").value;
 const prev = +document.getElementById("previous").value;
 const temp = +document.getElementById("temperature").value;
 const rain = +document.getElementById("rainfall").value;

 if (!year || !pop || prev < 0 || rain < 0) {
  alert("Please enter valid scenario values.");
  return;
 }

 const years = Math.max(0, year - 2024);

 const estimate = Math.max(
  0,
  prev +
  years * (prev * .018) +
  (pop / 1000) * .8 +
  (temp - 25) * .18 -
  (rain / 1000) * .7
 );

 document.getElementById("forecastValue").textContent =
  estimate.toFixed(2) + " BCM";

 document.getElementById("forecastStatus").textContent =
  country + " · " + year +
  " · Illustrative estimate generated from the entered scenario.";

 document.getElementById("forecastStatus").className =
  "notice success";

 document.getElementById("inputSummary").textContent =
  `Population: ${pop} million · Previous consumption: ${prev} BCM · Temperature: ${temp} °C · Rainfall impact: ${rain} mm`;

 document.getElementById("agentDemand").value =
  estimate.toFixed(2);

 document.getElementById("dashDemand").textContent =
  estimate.toFixed(1);

 drawForecastChart();
}

function resetForecast() {
 document.getElementById("country").value = "India";
 document.getElementById("year").value = 2027;
 document.getElementById("population").value = 1420;
 document.getElementById("previous").value = 115;
 document.getElementById("temperature").value = 28;
 document.getElementById("rainfall").value = 800;
}

function runAgent() {
 const d = +document.getElementById("agentDemand").value;
 const s = +document.getElementById("agentSupply").value;
 const t = +document.getElementById("threshold").value;

 if (d < 0 || s < 0 || t < 0) {
  alert("Enter non-negative values.");
  return;
 }

 const gap = d - s;
 const pct = d ? gap / d * 100 : 0;

 let status, msg, cls;

 if (gap > 0 && pct >= t) {
  status = "Shortage risk";

  msg = `Potential shortage detected. Predicted demand is ${d.toFixed(2)} BCM and available supply is ${s.toFixed(2)} BCM. The gap is ${gap.toFixed(2)} BCM (${pct.toFixed(1)}%). Consider reviewing allocation and conservation measures.`;

  cls = "alert critical";

 } else if (gap > 0) {
  status = "Monitor";

  msg = `A supply gap of ${gap.toFixed(2)} BCM exists, but it is below the selected ${t}% alert threshold. Continue monitoring.`;

  cls = "alert";

 } else {
  status = "Supply sufficient";

  msg = `Available supply meets or exceeds predicted demand by ${Math.abs(gap).toFixed(2)} BCM.`;

  cls = "alert ok";
 }

 document.getElementById("agentDecision").className = cls;
 document.getElementById("agentDecision").textContent = msg;

 const tr = document.createElement("tr");

 tr.innerHTML = `
  <td>${new Date().toLocaleTimeString()}</td>
  <td>${d.toFixed(1)}</td>
  <td>${s.toFixed(1)}</td>
  <td>${gap.toFixed(1)}</td>
  <td>
   <span class="status ${
    status === "Shortage risk" ? "bad" :
    status === "Monitor" ? "warn" : ""
   }">${status}</span>
  </td>
 `;

 document.getElementById("agentLog").prepend(tr);

 document.getElementById("dashSupply").textContent =
  s.toFixed(1);

 document.getElementById("dashGap").textContent =
  gap.toFixed(1);

 document.getElementById("dashboardAlerts").innerHTML =
  `<div class="${cls}">${msg}</div>`;
}

function optimizeAllocation() {
 const supply = +document.getElementById("allocSupply").value;

 const weights = [
  +document.getElementById("homeWeight").value,
  +document.getElementById("agriWeight").value,
  +document.getElementById("industryWeight").value
 ];

 const names = ["Household", "Agriculture", "Industry"];

 const total = weights.reduce((a, b) => a + b, 0);

 if (
  supply < 0 ||
  weights.some(x => x < 0) ||
  total === 0
 ) {
  alert("Enter a non-negative supply and at least one positive priority weight.");
  return;
 }

 let html =
  `<p><b>Total available supply:</b> ${supply.toFixed(2)} BCM</p>`;

 weights.forEach((v, i) => {
  const amount = supply * v / total;
  const pct = v / total * 100;

  html += `
   <div style="margin:14px 0">
    <div style="display:flex;justify-content:space-between">
     <b>${names[i]}</b>
     <b>${amount.toFixed(2)} BCM (${pct.toFixed(1)}%)</b>
    </div>
    <div class="barline">
     <span style="width:${pct}%"></span>
    </div>
   </div>
  `;
 });

 html +=
  "<p class='small muted'>Calculated proportionally from the weights entered. This is a demonstration, not an operational water-distribution instruction.</p>";

 document.getElementById("allocationResult").innerHTML = html;
}

function loadCSV(event) {
 const file = event.target.files[0];

 if (!file) return;

 if (!file.name.toLowerCase().endsWith(".csv")) {
  alert("Please choose a CSV file.");
  return;
 }

 const reader = new FileReader();

 reader.onload = e => {
  const text = e.target.result;

  const rows = text.trim().split(/\r?\n/).map(line =>
   line.split(/,(?=(?:[^"]*"[^"]*")*[^"]*$)/).map(v =>
    v.replace(/^"|"$/g, "").trim()
   )
  );

  if (!rows.length) return;

  const headers = rows[0];
  const body = rows.slice(1, 6);

  document.getElementById("rowCount").textContent =
   `${rows.length - 1} data rows · ${headers.length} columns`;

  let table =
   "<table><thead><tr>" +
   headers.map(h => `<th>${escapeHTML(h)}</th>`).join("") +
   "</tr></thead><tbody>";

  body.forEach(row => {
   table += "<tr>" +
    headers.map((_, i) =>
     `<td>${escapeHTML(row[i] || "")}</td>`
    ).join("") +
    "</tr>";
  });

  table += "</tbody></table>";

  document.getElementById("csvPreview").innerHTML = table;

  document.getElementById("uploadMessage").textContent =
   `Loaded ${file.name}. Previewing the first ${body.length} data rows. Uploading previews the CSV only; it does not train the machine-learning model.`;

  document.getElementById("uploadMessage").className =
   "notice success";
 };

 reader.readAsText(file);
}

function escapeHTML(s) {
 return String(s).replace(/[&<>"']/g, c => ({
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&#39;"
 }[c]));
}

document.getElementById("dashboardAlerts").innerHTML =
 '<div class="alert">Demand is higher than the illustrative available supply. Agent review recommended.</div><div class="alert ok">Dataset and model evaluation sections are ready for project data.</div>';

drawTrend();
drawForecastChart();

window.addEventListener("resize", () => {
 drawTrend();
 drawForecastChart();
});

// ===============================
// PARTICLES BACKGROUND
// ===============================
particlesJS("particles-js", {
  particles: {
    number: { value: 80 },
    color: { value: "#ffffff" },
    size: { value: 3 },
    move: { speed: 1 },
    line_linked: { enable: true }
  }
});


// ===============================
// PAGE LOAD EVENTS
// ===============================
document.addEventListener("DOMContentLoaded", () => {

  const uploadBox = document.getElementById("uploadBox");
  const fileInput = document.getElementById("resume");
  const analyzeBtn = document.getElementById("analyzeBtn");

  // Upload click
  uploadBox.addEventListener("click", () => {
    fileInput.click();
  });

  // Show filename
  fileInput.addEventListener("change", () => {

    if(fileInput.files.length > 0){

      const fileName = fileInput.files[0].name;

      const textElement = uploadBox.querySelector("p");

      if(textElement){
        textElement.innerText = "✓ " + fileName;
        textElement.classList.remove("text-gray-400");
        textElement.classList.add("text-green-400");
      }

    }

  });

  // Analyze button
  analyzeBtn.addEventListener("click", analyzeResume);

});


// ===============================
// ANALYZE RESUME FUNCTION
// ===============================
async function analyzeResume(){

  const resumeInput = document.getElementById("resume");
  const jobDesc = document.getElementById("jobdesc").value.trim();
  const results = document.getElementById("results");

  if(!resumeInput || resumeInput.files.length === 0){
    alert("Please upload a resume");
    return;
  }

  if(!jobDesc){
    alert("Please enter job description");
    return;
  }

  results.innerHTML = `
  <div class="text-center text-xl mt-10 animate-pulse">
  🤖 Analyzing resume with AI...
  </div>
  `;

  const formData = new FormData();
  formData.append("resume", resumeInput.files[0]);
  formData.append("job_description", jobDesc);

  const response = await fetch("/analyze", {
    method: "POST",
    body: formData
  });

  const data = await response.json();

  // ===============================
  // DASHBOARD UI
  // ===============================
  results.innerHTML = `

  <div class="grid grid-cols-3 gap-6 mt-8">

    <div class="bg-slate-900/70 backdrop-blur-xl p-4 rounded-xl">
      <h3 class="text-xl mb-2">Match Score</h3>
      <canvas id="scoreChart"></canvas>
    </div>

    <div class="bg-slate-900/70 backdrop-blur-xl p-4 rounded-xl">
      <h3 class="text-xl mb-2">Top Roles</h3>
      <ul>
      ${data.predicted_roles.map(r =>
        `<li>${r.role} (${(r.score*100).toFixed(1)}%)</li>`
      ).join("")}
      </ul>
    </div>

    <div class="bg-slate-900/70 backdrop-blur-xl p-4 rounded-xl">
      <h3 class="text-xl mb-2">Missing Skills</h3>
      ${
        data.missing_skills.length
        ? data.missing_skills.join(", ")
        : "No critical gaps"
      }
    </div>

  </div>


  <!-- Resume Skills -->
  <div class="bg-slate-900/70 backdrop-blur-xl p-6 rounded-xl mt-6">

  <h3 class="text-xl mb-3">Resume Skills</h3>

  ${data.resume_skills.map(skill =>
    `<span class="bg-blue-500/20 text-blue-400 px-3 py-1 rounded-full text-sm mr-2">
      ${skill}
    </span>`
  ).join("")}

  </div>


  <!-- AI Feedback -->
  <div class="bg-slate-900/70 backdrop-blur-xl p-6 rounded-xl mt-6">

  <h3 class="text-xl mb-3">AI Feedback</h3>

  <ul>
  ${data.feedback.map(f => `<li>- ${f}</li>`).join("")}
  </ul>

  </div>


  <!-- ATS Radar Chart -->
  <div class="bg-slate-900/70 backdrop-blur-xl p-6 rounded-xl mt-6">

  <h3 class="text-xl mb-3">ATS Resume Score</h3>

  <canvas id="atsChart"></canvas>

  </div>


  <!-- Skill Evidence -->
  <div class="bg-slate-900/70 backdrop-blur-xl p-6 rounded-xl mt-6">

  <h3 class="text-xl mb-3">Skill Evidence</h3>

  ${
  Object.entries(data.evidence).map(([skill,lines]) => `

  <div class="mb-4">

  <p class="text-blue-400 font-semibold">${skill}</p>

  <ul class="text-gray-300 text-sm">

  ${lines.map(line => `<li>✔ ${line}</li>`).join("")}

  </ul>

  </div>

  `).join("")
  }

  </div>

  `;


  // ===============================
  // MATCH SCORE CHART
  // ===============================
  const ctx = document.getElementById("scoreChart");

  new Chart(ctx, {

    type: "doughnut",

    data:{
      labels:["Match","Gap"],
      datasets:[{
        data:[data.match_score,100-data.match_score],
        backgroundColor:["#22c55e","#1f2937"]
      }]
    },

    options:{
      cutout:"70%",
      plugins:{legend:{display:false}}
    }

  });



  // ===============================
  // ATS RADAR CHART
  // ===============================
  const atsCanvas = document.getElementById("atsChart");

  if (atsCanvas) {

    new Chart(atsCanvas, {

      type: "radar",

      data: {
        labels: ["Skills", "Role Fit", "Projects", "Education"],

        datasets: [{
          label: "ATS Score",

          data: [
            data.ats_score.skills,
            data.ats_score.role,
            data.ats_score.projects,
            data.ats_score.education
          ],

          backgroundColor: "rgba(59,130,246,0.25)",
          borderColor: "#3b82f6",
          pointBackgroundColor: "#3b82f6"
        }]
      },

      options: {
        responsive: true,

        scales: {
          r: {
            min: 0,
            max: 30,
            ticks: {
              stepSize: 5,
              color: "#9ca3af"
            },
            grid: {
              color: "rgba(255,255,255,0.1)"
            },
            pointLabels: {
              color: "#e5e7eb",
              font: { size: 14 }
            }
          }
        },

        plugins: {
          legend: {
            labels: {
              color: "#e5e7eb"
            }
          }
        }
      }

    });

  }

}
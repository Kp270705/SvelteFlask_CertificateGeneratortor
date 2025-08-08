<script>

  import { push } from 'svelte-spa-router';
  import { onMount } from 'svelte';
  import { Animate } from 'svelte-animate';

  // importing static media files:
  import officeWorkers from "../assets/Images/Home/officeWorkers.gif";
  import demoCertImg1 from "../assets/Images/Home/demoCertImg1.png";
  import demoCertImg2 from "../assets/Images/Home/demoCertImg2.png";
  import demoCertImg3 from "../assets/Images/Home/demoCertImg3.png";
  import demoCertImg4 from "../assets/Images/Home/demoCertImg4.png";
  import routesType from '../config/backend_routes.js';

  const demoImg = [demoCertImg1, demoCertImg2, demoCertImg3, demoCertImg4, demoCertImg2];

  //form data values:
  let eventName = $state('');
  let organizationName = $state('');
  let certificateType = $state('');
  let organizer1Desig = $state('');
  let organizer2Desig = $state('');
  let clickedAction = null;

  onMount(() => {
    const saved = localStorage.getItem("homeFormData");
      if (saved) {
        const parsed      = JSON.parse(saved);
        eventName         =  parsed.eventName || '';
        organizationName  =  parsed.organizationName || '';
        certificateType   =  parsed.certificateType || '';
        organizer1Desig   =  parsed.organizer1Desig || '';
        organizer2Desig   =  parsed.organizer2Desig || '';
      }
  });

  function handleClick(e) { // manually assigns click value
    clickedAction = e.target.value;
  }

  // Handling user input data:
  async function handleSubmit(e) {
    e.preventDefault();

    const userInputData = {
      eventName,
      organizationName,
      certificateType,
      organizer1Desig,
      organizer2Desig,
    };
    localStorage.setItem("homeFormData", JSON.stringify(userInputData));
    console.log(`userInputData: ${eventName}, ${organizationName}, ${certificateType}, ${organizer1Desig}, ${organizer2Desig}`)

    const form = e.target;
    const formData = new FormData(form);
    
    // Append action value:
    if (clickedAction) {
      formData.append("action", clickedAction);
    }

    try {
      const response = await fetch(`${routesType.current_route}/home/formData`, {
        method: "POST",
        body: formData,
        credentials: "include",
      });

      const result = await response.json();
      if (!response.ok) {
        throw new Error(result.error || `Server responded with ${response.status}`);
      }

      if (response.ok && clickedAction === 'Generate') {
        console.log("✅ Backend Response:", result);
        alert("🎉 Certificates generated successfully!");
        push('/acknowledgement');
      }
      if (response.ok && clickedAction=='Preview'){
        console.log("✅ Backend Response:", result);
        alert("🎉 Certificate generate for preview mode!");
      }

    } catch (error) {
      console.error("❌ Submission failed:", error);
      alert("❗"+ error.message);
    }
  }
</script>


<!-- ==========  GLOBAL COLOURS  ========== -->
<style>

  :root{
    --bg-page:       linear-gradient(135deg, #fef7ed 0%, #fff1f2 25%, #f0f9ff 50%, #f7fee7 75%, #fefce8 100%);
    --bg-card:       rgba(255, 255, 255, 0.95);
    --bg-input:      rgba(255, 255, 255, 0.98);
    --border:        rgba(251, 146, 60, 0.2);
    --text-main:     #1f2937;
    --text-muted:    #6b7280;
    --text-white:    #ffffff;
    
    /* Certificate-inspired colors */
    --cert-gold:     #f59e0b;
    --cert-blue:     #3b82f6;
    --cert-green:    #10b981;
    --cert-purple:   #8b5cf6;
    --cert-orange:   #f97316;
    --cert-rose:     #f43f5e;
    --cert-emerald:  #059669;
    --cert-indigo:   #6366f1;
    
    /* Dynamic gradients */
    --gradient-warm:    linear-gradient(135deg, #fbbf24 0%, #f97316 100%);
    --gradient-cool:    linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
    --gradient-nature:  linear-gradient(135deg, #34d399 0%, #10b981 100%);
    --gradient-sunset:  linear-gradient(135deg, #fb7185 0%, #f97316 100%);
    --gradient-ocean:   linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%);
    --gradient-forest:  linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
    
    --shadow-warm:   0 10px 25px rgba(251, 146, 60, 0.15);
    --shadow-cool:   0 10px 25px rgba(59, 130, 246, 0.15);
    --shadow-nature: 0 10px 25px rgba(16, 185, 129, 0.15);
    --shadow-hover:  0 20px 40px rgba(0, 0, 0, 0.1);
  }

  * {
    box-sizing: border-box;
  }

  body{ 
    background: var(--bg-page);
    color: var(--text-main);
    margin: 0;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    min-height: 100vh;
    position: relative;
  }

  /* Add floating decorative elements */
  body::before {
    content: '';
    position: fixed;
    top: 10%;
    left: 5%;
    width: 120px;
    height: 120px;
    background: var(--gradient-warm);
    border-radius: 50%;
    opacity: 0.08;
    animation: float 6s ease-in-out infinite;
    z-index: -1;
  }

  body::after {
    content: '';
    position: fixed;
    top: 60%;
    right: 10%;
    width: 100px;
    height: 100px;
    background: var(--gradient-cool);
    border-radius: 50%;
    opacity: 0.08;
    animation: float 8s ease-in-out infinite reverse;
    z-index: -1;
  }

  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
  }

  /* ==========  WRAPPER / LAYOUT  ========== */
  .wrapper {
    max-width: 1400px;
    margin: 0 auto;
    padding: 2rem 1rem;
    min-height: 100vh;
    position: relative;
  }

  h1.main {
    text-align: center;
    margin-bottom: 3rem;
    line-height: 1.2;
    font-size: 3.2rem;
    font-weight: 900;
    background: var(--gradient-warm);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    position: relative;
  }

  h1.main::after {
    content: '';
    position: absolute;
    bottom: -15px;
    left: 50%;
    transform: translateX(-50%);
    width: 120px;
    height: 6px;
    background: var(--gradient-sunset);
    border-radius: 3px;
  }

  .main-content {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 4rem;
    align-items: start;
    margin-bottom: 4rem;
  }

  /* ==========  LEFT COLUMN - ILLUSTRATION & TESTIMONIALS  ========== */
  .left-column {
    display: flex;
    flex-direction: column;
    gap: 3rem;
  }

  .illustration {
    position: relative;
    padding: 2rem;
    background: var(--bg-card);
    border-radius: 30px;
    box-shadow: var(--shadow-cool);
    backdrop-filter: blur(10px);
  }

  .illustration::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--gradient-ocean);
    border-radius: 30px;
    opacity: 0.1;
    transform: rotate(-1deg);
  }

  .illustration img {
    width: 100%;
    max-width: 400px;
    border-radius: 20px;
    box-shadow: var(--shadow-warm);
    transition: transform 0.3s ease;
    position: relative;
    z-index: 1;
  }

  .illustration img:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: var(--shadow-hover);
  }

  /* ==========  FEATURE CARDS  ========== */
  .feature-cards {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .feature-card {
    background: var(--bg-card);
    padding: 2.5rem;
    border-radius: 25px;
    box-shadow: var(--shadow-nature);
    position: relative;
    overflow: hidden;
    border-left: 6px solid var(--cert-green);
    backdrop-filter: blur(10px);
  }

  .feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 100px;
    height: 100px;
    background: var(--gradient-nature);
    border-radius: 50%;
    opacity: 0.1;
    transform: translate(30px, -30px);
  }

  .feature-card h3 {
    font-size: 1.5rem;
    font-weight: 800;
    margin-bottom: 1rem;
    color: var(--cert-green);
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .feature-card h3::before {
    content: '✨';
    font-size: 1.2rem;
  }

  .feature-card p {
    color: var(--text-muted);
    line-height: 1.7;
    font-size: 1.1rem;
  }

  .stats-card {
    background: linear-gradient(135deg, var(--cert-gold) 0%, var(--cert-orange) 100%);
    border-left: 6px solid var(--cert-gold);
    color: var(--text-white);
  }

  .stats-card h3 {
    color: var(--text-white);
  }

  .stats-card p {
    color: rgba(255, 255, 255, 0.9);
  }

  .stats-card h3::before {
    content: '🎯';
  }

  /* ==========  FORM STYLING  ========== */
  form {
    background: var(--bg-card);
    border-radius: 30px;
    padding: 3rem;
    box-shadow: var(--shadow-cool);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    position: relative;
    overflow: hidden;
  }

  form::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: linear-gradient(90deg, var(--cert-gold), var(--cert-blue), var(--cert-green), var(--cert-purple), var(--cert-orange));
  }

  /* ==========  FORM SECTIONS  ========== */
  .form-section {
    margin-bottom: 3rem;
    padding: 2.5rem;
    border-radius: 25px;
    position: relative;
    overflow: hidden;
  }

  .form-section:nth-child(1) {
    background: linear-gradient(135deg, rgba(251, 191, 36, 0.12) 0%, rgba(249, 115, 22, 0.12) 100%);
    border-left: 6px solid var(--cert-gold);
  }

  .form-section:nth-child(2) {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.12) 0%, rgba(139, 92, 246, 0.12) 100%);
    border-left: 6px solid var(--cert-blue);
  }

  .form-section:nth-child(3) {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.12) 0%, rgba(34, 197, 94, 0.12) 100%);
    border-left: 6px solid var(--cert-green);
  }

  .section-title {
    font-size: 1.3rem;
    font-weight: 800;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }

  .form-section:nth-child(1) .section-title {
    color: var(--cert-gold);
  }

  .form-section:nth-child(2) .section-title {
    color: var(--cert-blue);
  }

  .form-section:nth-child(3) .section-title {
    color: var(--cert-green);
  }

  .section-title::before {
    content: '';
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: currentColor;
    box-shadow: 0 0 15px currentColor;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.1); opacity: 0.8; }
  }

  /* ==========  FORM ELEMENTS  ========== */
  .input-group {
    margin-bottom: 2rem;
  }

  .input-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
  }

  label {
    display: block;
    font-weight: 700;
    color: var(--text-muted);
    margin-bottom: 0.8rem;
    font-size: 0.95rem;
    text-transform: uppercase;
    letter-spacing: 0.6px;
  }

  input[type="text"],
  select,
  input[type="file"] {
    width: 100%;
    padding: 1.3rem 1.5rem;
    font-size: 1.1rem;
    color: var(--text-main);
    background: var(--bg-input);
    border: 2px solid transparent;
    border-radius: 15px;
    transition: all 0.3s ease;
    font-family: inherit;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    font-weight: 500;
  }

  input[type="file"] {
    padding: 1rem 1.5rem;
  }

  input:focus,
  select:focus {
    outline: none;
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
  }

  .form-section:nth-child(1) input:focus,
  .form-section:nth-child(1) select:focus {
    border-color: var(--cert-gold);
    box-shadow: 0 0 0 4px rgba(251, 191, 36, 0.25);
  }

  .form-section:nth-child(2) input:focus,
  .form-section:nth-child(2) select:focus {
    border-color: var(--cert-blue);
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.25);
  }

  .form-section:nth-child(3) input:focus,
  .form-section:nth-child(3) select:focus {
    border-color: var(--cert-green);
    box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.25);
  }

  input::placeholder {
    color: var(--text-muted);
    opacity: 0.7;
    font-weight: 400;
  }

  /* ==========  TEMPLATE PICKER  ========== */
  .template-section {
    margin-top: 3rem;
    padding: 3rem;
    background: linear-gradient(135deg, 
      rgba(249, 115, 22, 0.12) 0%, 
      rgba(244, 63, 94, 0.12) 25%, 
      rgba(139, 92, 246, 0.12) 50%, 
      rgba(16, 185, 129, 0.12) 75%, 
      rgba(251, 191, 36, 0.12) 100%);
    border-radius: 30px;
    border: 3px solid transparent;
    background-clip: padding-box;
    position: relative;
  }

  .template-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, var(--cert-orange), var(--cert-rose), var(--cert-purple), var(--cert-green), var(--cert-gold));
    border-radius: 30px;
    padding: 3px;
    mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    mask-composite: exclude;
    z-index: -1;
  }

  h2.pick-head {
    text-align: center;
    margin-bottom: 3rem;
    font-weight: 900;
    font-size: 2rem;
    background: var(--gradient-sunset);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    position: relative;
    text-transform: uppercase;
    letter-spacing: 1.5px;
  }

  h2.pick-head::after {
    content: '';
    position: absolute;
    bottom: -15px;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 5px;
    background: var(--gradient-sunset);
    border-radius: 3px;
  }

  .template-picker {
    overflow-x: auto;
    padding-bottom: 2rem;
  }

  .template-list {
    display: flex;
    gap: 2.5rem;
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .template-list li {
    position: relative;
    flex: 0 0 auto;
  }

  .template-list img {
    width: 300px;
    height: 200px;
    border-radius: 20px;
    transition: all 0.4s ease;
    cursor: pointer;
    border: 4px solid transparent;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
  }

  .template-list input[type="radio"] {
    position: absolute;
    top: 20px;
    left: 20px;
    transform: scale(1.6);
    z-index: 2;
    accent-color: var(--cert-orange);
  }

  .template-list li:nth-child(1) input[type="radio"]:checked + label img {
    border-color: var(--cert-gold);
    box-shadow: 0 0 0 5px rgba(251, 191, 36, 0.3), 0 15px 40px rgba(251, 191, 36, 0.4);
  }

  .template-list li:nth-child(2) input[type="radio"]:checked + label img {
    border-color: var(--cert-blue);
    box-shadow: 0 0 0 5px rgba(59, 130, 246, 0.3), 0 15px 40px rgba(59, 130, 246, 0.4);
  }

  .template-list li:nth-child(3) input[type="radio"]:checked + label img {
    border-color: var(--cert-green);
    box-shadow: 0 0 0 5px rgba(16, 185, 129, 0.3), 0 15px 40px rgba(16, 185, 129, 0.4);
  }

  .template-list li:nth-child(4) input[type="radio"]:checked + label img {
    border-color: var(--cert-purple);
    box-shadow: 0 0 0 5px rgba(139, 92, 246, 0.3), 0 15px 40px rgba(139, 92, 246, 0.4);
  }

  .template-list input[type="radio"]:checked + label img {
    transform: scale(1.05);
  }

  .template-list img:hover {
    transform: scale(1.03) translateY(-8px);
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.25);
  }

  /* ==========  ACTION BUTTONS  ========== */
  .actions {
    text-align: center;
    margin-top: 4rem;
    display: flex;
    gap: 2rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  button {
    cursor: pointer;
    border: none;
    border-radius: 20px;
    font-weight: 800;
    padding: 1.5rem 4rem;
    font-size: 1.2rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    min-width: 200px;
    color: var(--text-white);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  }

  button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
    transition: left 0.6s;
  }

  button:hover::before {
    left: 100%;
  }

  .preview {
    background: var(--gradient-nature);
    box-shadow: var(--shadow-nature);
  }

  .generate {
    background: var(--gradient-warm);
    box-shadow: var(--shadow-warm);
  }

  button:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
  }

  button:active {
    transform: translateY(-2px);
  }

  /* ==========  RESPONSIVE  ========== */
  @media(max-width: 1024px) {
    .main-content {
      grid-template-columns: 1fr;
      gap: 3rem;
    }
    
    .wrapper {
      max-width: 900px;
    }
  }

  @media(max-width: 768px) {
    .wrapper {
      padding: 1rem;
    }

    h1.main {
      font-size: 2.5rem;
      margin-bottom: 2rem;
    }

    form {
      padding: 2rem;
    }

    .form-section {
      padding: 2rem;
    }

    .template-section {
      padding: 2rem;
    }

    .input-row {
      grid-template-columns: 1fr;
    }

    .actions {
      flex-direction: column;
      align-items: center;
    }

    button {
      width: 100%;
      max-width: 300px;
    }

    .template-list img {
      width: 250px;
      height: 170px;
    }
  }

  @media(max-width: 480px) {
    .template-list img {
      width: 220px;
      height: 150px;
    }

    h1.main {
      font-size: 2.2rem;
    }

    .template-list {
      gap: 2rem;
    }

    .feature-card {
      padding: 2rem;
    }

    .feature-card h3 {
      font-size: 1.3rem;
    }
  }
</style>


<!-- ==========  PAGE CONTENT  ========== -->



<div class="wrapper">
  <h1 class="main">🎓 Automated Certificate Generator</h1>

  <div class="main-content">
    <div class="left-column">

        <div class="illustration">
          <img src={officeWorkers} alt="Working office illustration" />
        </div>


      <div class="feature-cards">
      
        <div class="feature-card">
          <h3>Professional Excellence</h3>
          <p>Create stunning, professional certificates that leave a lasting impression. Our advanced templates are designed by experts to meet industry standards and exceed expectations.</p>
        </div>

        <div class="feature-card stats-card">
          <h3>Trusted by Thousands</h3>
          <p>Over 50,000+ certificates generated for organizations worldwide. Join the community of professionals who trust our platform for their certification needs.</p>
        </div>

        <div class="feature-card">
          <h3>Lightning Fast</h3>
          <p>Generate hundreds of certificates in minutes, not hours. Our automated system processes your data instantly while maintaining the highest quality standards.</p>
        </div>
      </div>
    </div>

    <form enctype="multipart/form-data" on:submit|preventDefault={handleSubmit}>      

      <!-- Basic Information Section -->
      <div class="form-section">
        <div class="section-title">📋 Basic Information</div>
        
        <div class="input-group">
          <label for="eventName">Event Name</label>
          <input bind:value={eventName} id="eventName" name="eventName" type="text" placeholder="Enter event name" required />
        </div>

        <div class="input-row">
          <div class="input-group">
            <label for="OrgName">Organisation Name</label>
            <input bind:value={organizationName} id="organizationName" name="organizationName" type="text" placeholder="Enter organisation name" required />
          </div>

          <div class="input-group">
            <label for="certificateType">Certificate Type</label>
            <select bind:value={certificateType} id="certificateType" name="certificateType" required>
              <option value="" disabled selected>Select certificate type</option>
              <option value="of participation">Certificate of Participation</option>
              <option value="of completion">Certificate of Completion</option>
              <option value="of appreciation">Certificate of Appreciation</option>
              <option value="of recognition">Certificate of Recognition</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Assets Section -->
      <div class="form-section">
        <div class="section-title">🎨 Assets & Files</div>
        
        <div class="input-row">
          <div class="input-group">
            <label for="logo">Organisation Logo (.png)</label>
            <input id="logo" name="logo" type="file" accept=".png" required />
          </div>

          <div class="input-group">
            <label for="logo2">Event Logo (.png)</label>
            <input id="logo2" name="logo2" type="file" accept=".png" />
          </div>
        </div>

        <div class="input-group">
          <label for="formfile">CSV File</label>
          <input id="formfile" name="file" type="file" multiple accept=".csv,text/csv" required />
        </div>
      </div>

      <!-- Organizers Section -->
      <div class="form-section">
        <div class="section-title">✍️ Organizers</div>
        
        <div class="input-row">
          <div class="input-group">
            <label for="organizer1Desig">Organizer 1 Designation</label>
            <input bind:value={organizer1Desig} id="organizer1Desig" name="organizer1Desig" type="text" placeholder="Enter designation" required  />
          </div>

          <div class="input-group">
            <label for="organizer1">Organizer 1 Signature (.png)</label>
            <input id="organizer1" name="organizer1" type="file" accept=".png" />
          </div>
        </div>

        <div class="input-row">
          <div class="input-group">
            <label for="organizer2Desig">Organizer 2 Designation</label>
            <input bind:value={organizer2Desig} id="organizer2Desig" name="organizer2Desig" type="text" placeholder="Enter designation" required  />
          </div>

          <div class="input-group">
            <label for="organizer2">Organizer 2 Signature (.png)</label>
            <input id="organizer2" name="organizer2" type="file" accept=".png" />
          </div>
        </div>
      </div>

      <!-- Template Selection -->
      <div class="template-section">
        <h2 class="pick-head">Choose Your Template</h2>
        <div class="template-picker">
          <ul class="template-list">
            {#each demoImg as src, i}
              <li>
                <input type="radio"
                       id="choice{i}"
                       name="certificate_choice"
                       value={`Choice${i+1}`}
                       checked={i === 0} />
                <label for="choice{i}">
                  <img src={src} alt={`Template ${i+1}`} />
                </label>
              </li>
            {/each}
          </ul>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="actions">
        <button class="preview" name="action" value="Preview" type="submit" on:click={handleClick} > 👁️ Preview </button>
        <button class="generate" name="action" value="Generate" type="submit" on:click={handleClick} > 🚀 Generate </button>
      </div>
    </form>
  </div>
</div>

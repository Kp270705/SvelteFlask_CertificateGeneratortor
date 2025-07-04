<script>
  /* keep your existing image imports */
  import officeWorkers  from "../assets/Images/Home/officeWorkers.gif";
  import demoCertImg1   from "../assets/Images/Home/demoCertImg1.png";
  import demoCertImg2   from "../assets/Images/Home/demoCertImg2.png";
  import demoCertImg3   from "../assets/Images/Home/demoCertImg3.png";
  import demoCertImg4   from "../assets/Images/Home/demoCertImg4.png";

  const demoImg = [demoCertImg1, demoCertImg2, demoCertImg3, demoCertImg4];

  function handleSubmit () {
    /* e.preventDefault();  // uncomment if you plan to use fetch() instead */
  }
</script>

<!-- ==========  GLOBAL COLOURS  ========== -->
<style>
  :root{
    --bg-page:     #121212;
    --bg-card:     #1e1e1e;
    --bg-input:    #242424;
    --border:      #444;
    --text-main:   #f1f1f1;
    --text-muted:  #c5c5c5;
    --accent-blue: #3b82f6; /* preview outline */
    --accent-green:#22c55e; /* generate button */
    --accent-amber:#facc15; /* preview button */
  }

  body{ background:var(--bg-page); color:var(--text-main); margin:0; }

  /* ==========  WRAPPER / LAYOUT  ========== */
  .wrapper  { max-width:1100px; margin:110px auto 60px; padding:0 1rem; }
  h1.main   { text-align:center; margin-bottom:2.5rem; line-height:1.3; }

  .flex-row { display:flex; gap:2.5rem; flex-wrap:wrap; align-items:flex-start; }

  .illustration         { flex:1 1 340px; }
  .illustration img     { width:100%; border-radius:10px; }

  form{ 
    flex:1 1 420px;
    background:var(--bg-card); 
    border-radius:10px; 
    padding:2rem 2.25rem; 
    box-shadow:0 4px 14px rgba(0,0,0,.6);
  }

  /* ==========  FORM ELEMENTS  ========== */
  label{ display:block; font-weight:600; color:var(--text-muted); margin:1.15rem 0 .4rem; }
  input[type="text"],
  select,
  input[type="file"]{
    width:100%; 
    padding:.7rem .8rem; 
    font-size:1rem; 
    color:var(--text-main);
    background:var(--bg-input); 
    border:1px solid var(--border);
    border-radius:6px;
  }
  input[type="file"]{ padding:.5rem .6rem; }

  input:focus, select:focus{
    border-color:var(--accent-blue);
    outline:none;
    box-shadow:0 0 0 2px rgb(59 130 246 / .45);
  }

  /* ==========  TEMPLATE PICKER  ========== */
  h2.pick-head{ text-align:center; margin-top:2.8rem; font-weight:600; }

  .template-picker { margin-top:1.5rem; overflow-x:auto; padding-bottom:.5rem; }
  .template-list   { display:flex; gap:2rem; list-style:none; padding:0; }

  .template-list li{ position:relative; flex:0 0 auto; }
  .template-list img{
    width:260px; height:170px; border-radius:8px;
    transition:transform .25s, box-shadow .25s;
  }
  .template-list img:hover{
    transform:scale(1.07);
    box-shadow:0 4px 12px rgba(0,0,0,.5);
  }
  .template-list input[type="radio"]{
    position:absolute; top:10px; left:10px; transform:scale(1.25);
    accent-color:var(--accent-blue);
  }

  /* ==========  ACTION BUTTONS  ========== */
  .actions { text-align:center; margin-top:2.5rem; }
  button{
    cursor:pointer; border:none; border-radius:6px; font-weight:600;
    padding:.9rem 2.6rem; margin:0 .6rem; font-size:1rem; transition:opacity .2s;
  }
  .preview { background:var(--accent-amber); color:#000; }
  .generate{ background:var(--accent-green); color:#000; }
  button:hover{ opacity:.9; }

  /* ==========  RESPONSIVE  ========== */
  @media(max-width:760px){
    .wrapper{ margin-top:140px; }
    .flex-row{ flex-direction:column; }
    form{ width:100%; padding:1.75rem; }
  }
</style>

<!-- ==========  MARK‑UP  ========== -->
<div class="wrapper">
  <h1 class="main">Welcome to the Automated Certificate Generator</h1>

  <div class="flex-row">

    <div class="illustration">
      <img src={officeWorkers} alt="Working office illustration" />
    </div>

    <form action="/FormData" method="post" enctype="multipart/form-data"
          on:submit={handleSubmit}>

      <!-- basic info -->
      <label for="eventName">Event name</label>
      <input id="eventName" name="eventName" type="text" required />

      <label for="OrgName">Organisation name</label>
      <input id="OrgName" name="OrgName" type="text" required />

      <label for="certificateType">Certificate type</label>
      <select id="certificateType" name="certificateType" required>
        <option value="" disabled selected>Select type</option>
        <option value="of participation">Certificate of Participation</option>
        <option value="of completion">Certificate of Completion</option>
        <option value="of appreciation">Certificate of Appreciation</option>
        <option value="of recognition">Certificate of Recognition</option>
      </select>

      <!-- assets -->
      <label for="logo">Organisation logo (.png)</label>
      <input id="logo" name="logo" type="file" accept=".png" />

      <label for="logo2">Event logo (.png)</label>
      <input id="logo2" name="logo2" type="file" accept=".png" />

      <label for="formfile">CSV file</label>
      <input id="formfile" name="file" type="file" multiple accept=".csv,text/csv" required />

      <!-- organisers -->
      <label for="Organizer1Desig">Organizer 1 designation</label>
      <input id="Organizer1Desig" name="Organizer1Desig" type="text" required />

      <label for="organizer1">Organizer 1 signature (.png)</label>
      <input id="organizer1" name="organizer1" type="file" accept=".png" />

      <label for="Organizer2Desig">Organizer 2 designation</label>
      <input id="Organizer2Desig" name="Organizer2Desig" type="text" required />

      <label for="organizer2">Organizer 2 signature (.png)</label>
      <input id="organizer2" name="organizer2" type="file" accept=".png" />

      <!-- template chooser -->
      <h2 class="pick-head">Choose a template</h2>
      <div class="template-picker">
        <ul class="template-list">
          {#each demoImg as src, i}
            <li>
              <!-- first radio checked by default -->
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

      <!-- buttons -->
      <div class="actions">
        <button class="preview"  name="action" value="Preview"  type="submit">Preview</button>
        <button class="generate" name="action" value="Generate" type="submit">Generate</button>
      </div>

    </form>

  </div>
</div>

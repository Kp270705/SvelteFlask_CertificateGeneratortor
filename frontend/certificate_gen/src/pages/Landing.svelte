<script>
    import certImg from "../assets/Images/auth/demoCert2.png";
    import { link } from 'svelte-spa-router';
  // console.log(`From Landing and navigate is: ${navigate}`);
</script>

<style>
  section {
    min-height: calc(100vh - 80px);
    padding: 4rem 1.5rem 2rem;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 3rem;
    color: #fff;
    text-align: center;
    background: #1f1f1f;
  }

  .text {
    flex: 1 1 340px;
    max-width: 620px;
  }

  h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }

  p {
    line-height: 1.6;
    margin-bottom: 2rem;
  }

  .buttons a {
    display: inline-block;
    padding: 0.75rem 2.25rem;
    margin-right: 1rem;
    border-radius: 6px;
    text-decoration: none;
    color: #fff;
    font-weight: 600;
    cursor: pointer;
  }

  .primary {
    background: #0d6efd;
  }

  .secondary {
    background: #6c757d;
  }

  .buttons a:hover {
    opacity: 0.85;
  }

  img {
    max-width: 420px;
    width: 100%;
    border-radius: 10px;
  }
</style>

<section>
  <div class="text">
    <h1>Welcome to<br />Certificate Generator</h1>
    <p>
      Welcome to our cutting-edge Certificate Generator! Simplify and streamline
      your certificate-creation process with our automated platform. Generate
      stunning, professional-quality certificates tailored to your needs.
    </p>
    <div class="buttons">
      <a use:link href="/home"><button class="px-8 py-3 bg-indigo-600 text-font-medium rounded-lg hover:bg-indigo-transition-colors hover-lift">Home</button></a>
      <a use:link href="/register"><button class="px-8 py-3 border-2 border-indigo-600 text-indigo-600 font-medium rounded-lg hover:bg-indigo-50 transition-colors hover-lift">Register</button></a>
    </div>
  </div>

  <img src={certImg} alt="Certificate Preview" />
</section>

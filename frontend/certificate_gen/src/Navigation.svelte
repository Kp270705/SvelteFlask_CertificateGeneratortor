<script>
  export let current = "landing";     // page that is currently active
  export let navigate;                // function passed down from parent
</script>

<nav class="navbar">
  <div class="brand" on:click={() => navigate("landing")}>CertificateGen 🖹🖺 </div>

  <ul>
    <li class:active={current === "landing"} on:click={() => navigate("home")}>Home</li>
    <li class:active={current === "about"}   on:click={() => navigate("about")}>About&nbsp;Us</li>
    <li class:active={current === "contact"} on:click={() => navigate("contact")}>Contact</li>
    <li on:click={() => navigate("landing")}>Signout</li>
  </ul>
</nav>

<style>
  .navbar{
    position:fixed;          /* always stick to the very top */
    top:0; left:0; width:100%;
    background:#333;
    display:flex; justify-content:space-between; align-items:center;
    padding:0.75rem 1.5rem;
    box-shadow:0 2px 6px rgba(0,0,0,.25);
    z-index:10;
  }
  .brand{ color:#fff; font-size:1.4rem; font-weight:600; cursor:pointer;}
  ul{ list-style:none; display:flex; gap:1.5rem; margin:0; padding:0;}
  li{ color:#fff; cursor:pointer; font-weight:500;}
  li:hover{ transform:scale(1.05);}
  .active{ text-decoration:underline;}
</style>

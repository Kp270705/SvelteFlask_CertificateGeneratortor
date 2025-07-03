<script>
  import Navigation from "./Navigation.svelte";
  import Landing from "./pages/Landing.svelte";
  import Home from "./pages/Home.svelte";
  import About from "./pages/About.svelte";
  import Contact from "./pages/Contact.svelte";

  let current = "landing";

  const pages = {
    landing: Landing,
    home: Home,
    about: About,
    contact: Contact
  };

  function navigate(page) {
    current = page;
    console.log(`Navigating to ${page}`);
  }
</script>

<Navigation {current} {navigate} />

<!-- Pass navigate prop if current page is Landing -->
<svelte:component this={pages[current]} navigate={navigate} />

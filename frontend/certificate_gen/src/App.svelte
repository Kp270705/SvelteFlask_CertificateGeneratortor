<script>
  import Navigation from "./Navigation.svelte";
  import Landing from "./pages/Landing.svelte";
  import Home from "./pages/Home.svelte";
  import About from "./pages/About.svelte";
  import Contact from "./pages/Contact.svelte";
  import Acknowledgement from "./pages/Acknowledgement.svelte";

  let current = "landing";

  const pages = {
    landing: Landing,
    home: Home,
    about: About,
    contact: Contact
  };

  const routes = {
    '/': Home,
    '/ack': Acknowledgement,
  };

  function navigate(page) {
    current = page;
    console.log(`Navigating to ${page}`);
  }
</script>


<!-- <h2 style="color: lightgreen;">I am h2 of App.svelte </h2> -->
<Navigation {current} {navigate} />

<!-- Pass navigate prop if current page is Landing -->
 <svelte:component this={pages[current]} navigate={navigate} /> <!-- Pass navigate prop to all pages except Landing. -->

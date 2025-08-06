<svelte:head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/base16/google-dark.min.css" />
</svelte:head>



<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, DarkMode } from "flowbite-svelte";
  import { link } from 'svelte-spa-router';
  import { location } from 'svelte-spa-router';

  // importing components: 
  import Darkmode from "../../components/Darkmode/Darkmode.svelte";
  import NavDropdown from "../Dropdown/NavDropdown.svelte";

  // import staric content
  // import CertGen from "../../assets/icons/rocket1.png";
  import CertGen from "../../assets/icons/certGen3.png";

  let pages = [
    { name: "Home",             path: "/home" },
    { name: "About",            path: "/about" },
    { name: "Register",         path: "/register" },
    { name: "Texteditor",       path: "/textedit"},
  ];


  let dropDownRoute = '';

  $: {
    const currentRoute = $location;
    console.log(`current route: ${currentRoute}`);
    dropDownRoute = currentRoute === '/home' ? "Sign-Out" : "Sign-In";
  }

</script>

<Navbar>
  <NavBrand href="/">
    <img src={CertGen} class="me-3 h-12 sm:h-9" alt="Logo" />
    <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Cert Genie</span>
  </NavBrand>
  <NavHamburger />
    <NavUl>
    {#each pages as page}
      <NavLi>
        <a use:link href={page.path} class="block py-2 px-3 text-blue-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700">
          {page.name}
        </a>
      </NavLi>
    {/each}
    <NavLi>
        <NavDropdown {dropDownRoute} />
    </NavLi>
    <NavLi class="mx-5">
        <Darkmode />
    </NavLi>
  </NavUl>
</Navbar>

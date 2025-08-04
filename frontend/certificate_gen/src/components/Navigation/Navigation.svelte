<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from "flowbite-svelte";
  import { link } from 'svelte-spa-router';

  // importing components: 
  import Darkmode from "../../components/Darkmode/Darkmode.svelte";
  import NavDropdown from "../Dropdown/NavDropdown.svelte";

  // import staric content
  // import CertGen from "../../assets/icons/rocket1.png";
  import CertGen from "../../assets/icons/certGen3.png";

  let pages = [
    { name: "Home", path: "/home" },
    { name: "About", path: "/about" },
    { name: "Register", path: "/register" },
  ];

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
        <Darkmode />
        <NavDropdown />
      </NavLi>
  </NavUl>
</Navbar>
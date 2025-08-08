
<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Popover, Avatar } from "flowbite-svelte";
  import { link } from 'svelte-spa-router';
  import { onMount } from 'svelte';
  import { UserCircleHero } from 'svelte-animated-icons';
  import { Tooltip, Button } from "flowbite-svelte";
  import { blur } from "svelte/transition";


  // importing components: 
  import Darkmode from "../../components/Darkmode/Darkmode.svelte";
  import NavDropdown from "../Dropdown/NavDropdown.svelte";
  import UserDetails from "../popover/UserDetails.svelte";

  // import static content
  import CertGen from "../../assets/icons/certGen3.png";
  import routesType from "../../config/backend_routes";
  import { isAuthorized, authRoute  } from "../../stores/authStore";

  let pages = [
    { name: "Home", path: "/home" },
    { name: "About", path: "/about" },
    { name: "Register", path: "/register" }
  ];

  const AuthErrors = {
    TOKEN_EXPIRED: 401,
    MISSING_TOKEN:401,
    INVALID_TOKEN: 422,
  };

  onMount(async () => {
    try {
      const token = localStorage.getItem("jwt_token")
      const res = await fetch(`${routesType.current_route}/resources/token`, {
        headers: (token ? { Authorization: `Bearer ${token}` } : {})
      });
      const data = await res.json();

      if (res.status === 401) {
        console.warn(`❌ Token expired or missing.\n\tError: ${data.error}`);
        isAuthorized.set(false);
        authRoute.set("Sign-In");
      } 

      // this error not occurs usually(for advanced backend)
      else if (res.status === 422) {
        console.warn(`❌ Invalid token (possibly signed out).\n\tError: ${data.error}`);
        isAuthorized.set(false);
        authRoute.set("Sign-In");
      }

      else {
        console.log(`✅ ✅ User authenticated.\n\tUser-Id: ${data.user_id}`)
        isAuthorized.set(true);
        authRoute.set("Sign-Out");
        // window.location.reload
      }

    } catch (err) {
      console.error("Token check failed", err);
    }
  });
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
        <NavDropdown authRoute={$authRoute} />
    </NavLi>
    <NavLi class="mx-5">
      <Darkmode />
    </NavLi>
    {#if $isAuthorized }
    <NavLi class="mx-5">
      <UserCircleHero
        size={40}
        color="#c9cc2e" />
        <UserDetails />
    </NavLi>
    {/if}
  </NavUl>
</Navbar>

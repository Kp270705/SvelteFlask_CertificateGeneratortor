<script>

  import { push } from 'svelte-spa-router';
  import { onMount } from 'svelte';
  import Home from './Home.svelte';
  import Error from '../components/Card/authCard.svelte';
  import accessDenied from "../assets/icons/accessDenied1.png";
  import routesType from '../config/backend_routes.js';

  let isAuthorized = $state(false);

  onMount(async () => {
    try {
      const res = await fetch(`${routesType.current_route}/auth/token`, {
        method:"GET",
        credentials: 'include'  // include cookies if any
      });

      const data = await res.json();

      if (data.message !== "No-Token") {
        isAuthorized = true;
        console.log('user authenticated')
      } else {
        
        push('/login');
      }

    } catch (err) {
      console.error("Token check failed", err);
    }

  });
</script>

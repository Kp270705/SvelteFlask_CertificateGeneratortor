<script>
  import { onMount } from 'svelte';
  import Home from './Home.svelte'; // or wherever your Home.svelte is located
  import { push } from 'svelte-spa-router';

  let isAuthorized = false;
  let loading = true;

  onMount(async () => {
    try {
      const res = await fetch('http://localhost:5000/auth/token', {
        credentials: 'include'  // include cookies if any
      });

      const data = await res.json();

      if (data.message !== "No-token") {
        isAuthorized = true;
      } else {
        alert("Please log in to access the Home page.");
        push('/login');  // redirect to login
      }
    } catch (err) {
      console.error("Token check failed", err);
      alert("Something went wrong. Please try logging in again.");
      push('/login');
    } finally {
      loading = false;
    }
  });
</script>

{#if loading}
  <p class="text-center">Checking authentication...</p>
{:else}
  {#if isAuthorized}
    <Home />
  {/if}
{/if}

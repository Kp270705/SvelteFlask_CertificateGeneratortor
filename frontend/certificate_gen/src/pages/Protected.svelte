<!-- Protected.svelte:  -->

<script>

  import { push } from 'svelte-spa-router';
  import { onMount } from 'svelte';
  import Home from './Home.svelte';
  import Error from '../components/Card/Error.svelte';
  import accessDenied from "../assets/icons/accessDenied1.png";
  import routesType from '../config/backend_routes.js';

  let isAuthorized = false;
  let loading = true;

  // Error card state
  let showError = false;
  let error = '';
  let errorDetail = '';
  let icon = '';
  let btnAction = '';
  let btnRoute = '';
  let btnAction2 = '';
  let btnRoute2 = '';

  const closeError = () => {
    showError = false;
  };

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
        alert("Please log in to access the Home page.");
        push('/login');
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
  <div class={showError ? "blur-sm pointer-events-none select-none transition-all duration-300" : ""}>
    {#if isAuthorized}
      <Home />
    {/if}
  </div>

  {#if showError}
    <div class="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm bg-black/60">
      <Error
        {error}
        {errorDetail}
        {btnAction}
        {btnRoute}
        {btnAction2}
        {btnRoute2}
        {icon}
        {close}
      />
    </div>
  {/if}
{/if}
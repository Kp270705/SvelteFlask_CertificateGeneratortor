<!-- Protected.svelte:  -->

<script>

  import { push } from 'svelte-spa-router';
  import { onMount } from 'svelte';
  import Home from './Home.svelte';
  import { CardPlaceholder, ImagePlaceholder, ListPlaceholder, Skeleton, TestimonialPlaceholder, TextPlaceholder, VideoPlaceholder, WidgetPlaceholder } from "flowbite-svelte";


  import Error from '../components/Card/authCard.svelte';
  import accessDenied from "../assets/icons/accessDenied1.png";
  import routesType from '../config/backend_routes.js';

  let isAuthorized = $state(false);
  let loading = $state(true);

  // Error card state
  let showError = $state(false);
  let error = '';
  let errorDetail = '';
  let iconType = '';
  let btnAction = '';
  let btnRoute = '';
  let btnAction2 = '';
  let btnRoute2 = '';

  const closeError = () => {
    showError = false;
  };

  const AuthErrors = {
    TOKEN_EXPIRED: 401,
    MISSING_TOKEN:401,
    INVALID_TOKEN: 422,
  };


  onMount(async () => {
    const token = localStorage.getItem("jwt_token")
    try {
      const res = await fetch(`${routesType.current_route}/resources/token`, {
        headers: (token ? { Authorization: `Bearer ${token}` } : {})
      });

      const data = await res.json();
      
      if (res.status === 401) {
        console.warn(`❌ Token expired or missing.\n\tError: ${data.error}`);
        isAuthorized = false;
        loading=true
        push('/login');
      } 
      // this error not occurs usually(for advanced backend)
      else if (res.status === 422) {
        console.warn(`❌ Invalid token (possibly signed out).\n\tError: ${data.error}`);
        isAuthorized = false;
        loading = true
        push('/login');
      }

      else if (res.status===200){
        console.log(`✅ ✅ User authenticated.\n\tUser-Id: ${data.user_id}`)
        isAuthorized = true
        loading = false
        push('/home')
      }
    } catch (err) {
      isAuthorized = false
        console.log(`\n\nin catch`)
        console.error("Server issue", err);
        alert("Something went wrong. Please try logging in again.");
        push('/login');
    }
  });
</script>


{#if loading}
  <p class="text-center">Checking authentication...</p>
    <ImagePlaceholder size="lg" class="ml-4" />
    <br> <br> <br> <br> <br>
    <TextPlaceholder class="ml-4" />
    <br> <br> <br>
    <Skeleton size="2xl" class="mt-8 mb-2.5" />
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
        {iconType}
        {close}
      />
    </div>
  {/if}
{/if}
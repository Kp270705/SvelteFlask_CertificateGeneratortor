<!-- Login svelte -->

<script>
  // import static files:
	import invalid from "../../assets/icons/wrong.png"
	import notFound from "../../assets/icons/notFoundCat.png"
	import LoginSuccess from "../../assets/icons/loginSuccessCat.png"
	import serverNotAvailable1 from "../../assets/icons/serverNotAvailable1.png";
  import routesType from "../../config/backend_routes.js";
  import iconChoice from "../../config/iconChoice";
  
  // import svelte-flowbite essentials
  import { Card, Button, Label, Input, Checkbox } from "flowbite-svelte";
  
  // import svelte essentials
	import { push } from 'svelte-spa-router';
	import { link } from 'svelte-spa-router';
  
  // import components:
	import Error from '../Card/Error.svelte';
  import Astronaut from "../../assets/svelteIcons/Astronaut.svelte";

	// define state variables for error defining:
	let showError = $state(false);
	let error = $state('');
	let errorDetail = $state('');
	let btnAction = $state('');
	let btnAction2 = $state('');
	let btnRoute = $state('');
	let btnRoute2 = $state(null);
	let iconType = $state();

  let iconInfo = $state({
    "choice": iconChoice,
    "type": '',
  })

	// handle login:
	async function handleSubmit(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
      const response = await fetch(`${routesType.current_route}/auth/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data),
        credentials: "include",
      });

      const result = await response.json();

      if (response.status === 404) {
        error = result.message;
        errorDetail = result.description;
        showError = true;
        btnAction = "Register"
        btnRoute = "/register"
        btnAction2 = "Login"
        btnRoute2 = "/login"
        iconInfo.type = "notfound"
        return;

      } else if (response.status === 401) {
        error = result.message;
        errorDetail = result.description;
        showError = true;
        btnAction = "Login"
        btnRoute = "/login"
        btnAction2 = null
        btnRoute2 = null
        iconInfo.type = "invalid"
        return;
      } 

	  else if (response.status === 200) {
        error = result.message;
        errorDetail = result.description;
        showError = true;
        btnAction = "Next";
        btnRoute = "/home";
        btnAction2 = null;
        btnRoute2 = null;
        iconInfo.type = "login_success"
        return;

      }
	 
    else if (!response.ok) {
      throw new Error(result.message || `Server error: ${response.status}`);
    }

    } catch (err) {
      console.error("❌ Login error:", err);
      error = "❗ Login Failed";
      errorDetail = `${err.message}. Due to unavailability of server.\n\n\nBuy me a coffee, and I will purchase the best hosting platform.`;
      showError = true;
      btnAction = "Login"
      btnRoute = "/login"
      btnAction2 = null
      btnRoute2 = null
      icon = serverNotAvailable1
    }
  }
</script>


<!-- Centering container -->
<div class="flex items-center justify-center h-full p-4 mt-25">
  <Card class="p-4 sm:p-6 md:p-8 relative w-full max-w-md">
    <div class={`space-y-4 p-6 sm:p-8 md:space-y-6 transition-all duration-300 ${showError ? 'blur-md pointer-events-none' : ''}`}>
      <form class="flex flex-col space-y-6" onsubmit={handleSubmit}>
        <h3 class="text-xl font-medium text-gray-900 dark:text-white">Login in to your account</h3>
        <Label class="space-y-2">
          <span>Email</span>
          <Input type="email" name="email" placeholder="name@company.com" />
        </Label>
        <Label class="space-y-2">
          <span>Your password</span>
          <Input type="password" name="password" placeholder="•••••" required />
        </Label>
        <Button type="submit" class="w-full">Login to your account</Button>
        <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
          Not registered? <a use:link href="/register" class="text-primary-700 dark:text-primary-500 hover:underline">Create account</a>
        </div>
      </form>
    </div>

    {#if showError}
      <div class="fixed inset-0 flex items-center justify-center z-50 bg-black/40 backdrop-blur-sm">
        <Error 
          {error} 
          {errorDetail} 
          {btnAction} 
          {btnAction2} 
          {btnRoute} 
          {btnRoute2}
          {iconInfo} 
          close={() => {
            showError = false;
            error = '';
            errorDetail = '';
            btnAction = '';
            btnAction2 = '';
            btnRoute = '';
            btnRoute2 = '';
            iconInfo = {
              "choice":'',
              "type":''
            };
          }
        } />
      </div>
    {/if}
  </Card>
</div>
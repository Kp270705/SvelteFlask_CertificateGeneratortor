
<!-- Error.svelte:  -->

<script lang="ts">

  // importing static files:
  // for login: 
  import wrongDetailsImg from "../../assets/icons/wrong.png"
	import notFoundImg from "../../assets/icons/userNotFoundCat.png"
	import loginSuccessImg from "../../assets/icons/loginSuccessCat.png"
  
  // for registration:
  import userAlreadyFoundImg from "../../assets/icons/existingUserFoundCat.png"
  import registerSuccessImg from "../../assets/icons/registerSuccess.png"

  // for serverNotAvailable
	import serverNotAvailableImg from "../../assets/icons/serverNotAvailable1.png";

  // js files:
  import iconChoice from "../../config/iconChoice";


  
  // importing flowbite sv files:
  import { Card, Button, Toggle } from "flowbite-svelte";
  import { ArrowRightOutline } from "flowbite-svelte-icons";
  import { Animate } from 'svelte-animate';

  

  // importing sv essentials:
  import { link } from 'svelte-spa-router';

    

  // importing sv-flowbite and kwaii illustrations:
  // sv-flowbite:
  // import userNotFoundIllus from "../../assets/illustrations/flowbiteSvIllustrations/UserNotFound.svelte";
  import serverNotAvailableIlus from "../../assets/illustrations/flowbiteSvIllustrations/ServerNotAvailable.svelte";

  // kawaii:
  import loginSuccessIllus from "../../assets/illustrations/svKawaii/LoginSuccess.svelte";
  import registerSuccessIllus from "../../assets/illustrations/svKawaii/RegisterSuccess.svelte";
  import userNotFoundIllus from "../../assets/illustrations/svKawaii/UserNotFound.svelte";
  import wrongDetailsIllus from "../../assets/illustrations/svKawaii/WrongDetails.svelte";
  import userAlreadyFoundIllus from "../../assets/illustrations/svKawaii/UserAlreadyFound.svelte";


  
  // variables: 
  const kwaiiIcons = {

    // for login:
    "userNotFound":            userNotFoundIllus,
    "wrongDetails":            wrongDetailsIllus,
    "loginSuccess":            loginSuccessIllus,
    
    // for register:
    "userAlreadyFound":        userAlreadyFoundIllus,
    "registerSuccess":         registerSuccessIllus,
    
    // server not available:
    "serverNotAvailable":      serverNotAvailableIlus,

  }

  const images = {

    // for login:
    "loginSuccess":            loginSuccessImg,
    "not-found":                notFoundImg,
    "wrongDetails":             wrongDetailsImg,
    
    // for register:
    "userAlreadyFound":         userAlreadyFoundImg,
    "registerSuccess":          registerSuccessImg,

    // server not available:
    "serverNotAvailable":       serverNotAvailableImg,
  }
  
  // exporting variables: 
  export let error;
  export let errorDetail;
  export let btnAction;
  export let btnAction2;
  export let btnRoute;
  export let btnRoute2;
  export let iconType;
  console.log(`\n\nicon choice: ${iconType}`)
  export let close = () => {};

</script>


<!-- <Animate
  animations={[{ action: "bounce" }]}
> -->
<Animate
trigger="both"
  animations={[{ action: "headShake" }]}
>

<div class="animate-fade-in-down transition-all duration-300">
  <Card>

    <!-- Conditional icon rendering -->
    <div class="flex justify-center mb-4">
      {#if iconChoice === 'illustrations'}
        <svelte:component this={kwaiiIcons[iconType]} size="160" color="#62a0ea" mood="excited" />
      {:else}
        <img src={ images[iconType]  } alt="Status icon" class="w-40 h-40 object-contain" />
      {/if}
    </div>
    
    <div class="m-6">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{error}</h5>
      <p class="mb-3 leading-tight font-normal text-gray-700 dark:text-gray-400">{errorDetail}</p>
      <a use:link href={btnRoute}>
        <Button class="w-40" onclick={() => { close() }}>
          {btnAction}
        </Button>
      </a>
      {#if btnAction2 !== null}
        <a use:link href={btnRoute2}>
          <Button class="w-40" onclick={() => { close() }}>
            {btnAction2}
          </Button>
        </a>
      {/if}
    </div>
  </Card>
</div>
</Animate>
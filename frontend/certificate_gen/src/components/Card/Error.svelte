
<script>

  import { Card, Button, Toggle } from "flowbite-svelte";
  import { ArrowRightOutline } from "flowbite-svelte-icons";
  import { link } from 'svelte-spa-router';

  let iconInfo = {
    "choice":'',
    "type":''
  }
  export let error;
  export let errorDetail;
  export let btnAction;
  export let btnAction2;
  export let btnRoute;
  export let btnRoute2;
  export default iconInfo ;

  import Astronaut from "../../assets/svelteIcons/Astronaut.svelte";

  const kwaiiIcons = [
    {res_type: "login_success", kwaii_icon: Astronaut}, 
    {res_type: "notfound", kwaii_icon: Astronaut}, 
    {res_type: "invalid", kwaii_icon: Astronaut}, 
  ]
  const images = [
    {res_type: "login_success", kwaii_icon: Astronaut}, 
    {res_type: "notfound", kwaii_icon: Astronaut}, 
    {res_type: "invalid", kwaii_icon: Astronaut}, 
  ]

  export let close = () => {};

  let vCard = false;
</script>

<div class="animate-fade-in-down transition-all duration-300">
  <Card reverse={vCard}>

    <!-- Conditional icon rendering -->
    <div class="flex justify-center mb-4">
      {#if iconInfo.choice === 'component'}
        iconInfo.type 
      {:else}
        <img src={} alt="Status icon" class="w-40 h-40 object-contain" />
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
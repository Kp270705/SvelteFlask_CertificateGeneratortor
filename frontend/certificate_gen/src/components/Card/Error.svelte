<script>
  import { Card, Button, Toggle } from "flowbite-svelte";
  import { ArrowRightOutline } from "flowbite-svelte-icons";
  import { link } from 'svelte-spa-router';

  export let error;
  export let errorDetail;
  export let btnAction;
  export let btnAction2;
  export let icon;
  export let btnRoute;
  export let btnRoute2;


  export let close = () => {};

  let vCard = false;
</script>


<div class="animate-fade-in-down transition-all duration-300">
  <Card img={icon} reverse={vCard}>
    <div class="m-6">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{error}</h5>
      <p class="mb-3 leading-tight font-normal text-gray-700 dark:text-gray-400">{errorDetail}</p>
        <a use:link href={btnRoute}>
            <Button class="w-40"
            onclick={()=>{ close() }}>
                {btnAction}<ArrowRightOutline class="ms-2 h-6 w-6 text-white" />
            </Button>
        </a>
        {#if btnAction2 !== null}
            <a use:link href={btnRoute2}>
                <Button class="w-40"
                onclick={()=>{ close() }}>
                    {btnAction2}<ArrowRightOutline class="ms-2 h-6 w-6 text-white" />
                </Button>
            </a>
        {/if}
    </div>
  </Card>
</div>





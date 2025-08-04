<script>
    // import svelte-flowbite essentials
    import { Button, Dropdown, DropdownItem } from "flowbite-svelte";
    import { ChevronDownOutline } from "flowbite-svelte-icons";

    // import svelte essentials
	import { push } from 'svelte-spa-router';
	import { link } from 'svelte-spa-router';

    async function signOut(e){
        e.preventDefault();
        try {
        const response = await fetch("http://localhost:5000/auth/logout", {
            credentials: "include",
        });
        if (response.status === 200){
            console.log('200')
            push('/login')
        }
        } catch(err){
            alert(err)
        }

    }

</script>

<!-- <Button>Dropdown button<ChevronDownOutline class="ms-2 h-6 w-6 text-white dark:text-white" /></Button> -->
<ChevronDownOutline class="ms-2 h-6 w-6 text-white dark:text-white" />
<Dropdown simple>
  <DropdownItem>
    <Button onclick={signOut} class="text-primary-700 dark:text-primary-500 hover:underline">Signout</Button>
  </DropdownItem>
</Dropdown>
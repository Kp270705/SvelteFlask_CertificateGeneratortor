<script>
    // import svelte-flowbite essentials
    import { Button, Modal, P, Dropdown, DropdownItem } from "flowbite-svelte";
    import { ChevronDownOutline } from "flowbite-svelte-icons";
    import { ExclamationCircleOutline } from "flowbite-svelte-icons";
    import { slide } from "svelte/transition";

    let popupModal = $state(false);

    import { Drawer, CloseButton, Label, Input, Textarea } from "flowbite-svelte";
    import { InfoCircleSolid, UserAddOutline, CalendarEditSolid } from "flowbite-svelte-icons";


    // import svelte essentials
	import { push } from 'svelte-spa-router';
	import { link } from 'svelte-spa-router';

    // import components: 


    // import static files:
    import routesType from "../../config/backend_routes";
    

    // export let authRoute;
    let {authRoute} = $props()

    async function signOut(e){
        e.preventDefault();
        try {
        const response = await fetch(`${routesType.current_route}/auth/logout`, {
            credentials: "include",
        });
        if (response.status === 200){
            console.log('200')
            localStorage.removeItem("jwt_token");
            authRoute = "Sign-In"
            push('/login')
        }
        } catch(err){
            alert(err)
        }
    }

    function handleClick(e) {
    if (authRoute === "Sign-Out") {
      signOut(e);
    } else {
      push('/login');
    }
  }

</script>

<div>
    <p class="flex items-center ml-2 mt-2 text-blue-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700">Options</p>
    <ChevronDownOutline class="ms-2 h-6 w-6 text-black dark:text-white" />
    <Dropdown simple>
    <DropdownItem>
        <Button onclick={() => (popupModal = true)}>
        {authRoute}
        </Button>
        <Modal form bind:open={popupModal} size="xs" transition={slide} permanent>
        <div class="text-center">
            <ExclamationCircleOutline class="mx-auto mb-4 h-12 w-12 text-gray-400 dark:text-gray-200" />
            <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">Are you sure you want to delete this product?</h3>
            <div class="space-x-2">
            <Button type="submit" value="yes" color="red" onclick={handleClick} >Yes, I'm sure</Button>
            <Button type="submit" value="no" color="alternative">No, cancel</Button>
            </div>
        </div>
        </Modal>
            
    </DropdownItem>
    </Dropdown>
</div>
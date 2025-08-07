<script>
    // import svelte-flowbite essentials
    import { Button, Dropdown, DropdownItem } from "flowbite-svelte";
    import { ChevronDownOutline } from "flowbite-svelte-icons";

    // import svelte essentials
	import { push } from 'svelte-spa-router';
	import { link } from 'svelte-spa-router';

    // import components: 


    // import static files:
    import routesType from "../../config/backend_routes";
    

    export let authRoute;

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
        <Button
        onclick={handleClick}
        class="w-full text-white bg-orange-600 hover:bg-orange-700 focus:ring-4 focus:outline-none focus:ring-orange-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-orange-500 dark:hover:bg-orange-600 dark:focus:ring-orange-800"
        >
        {authRoute}
        </Button>
    </DropdownItem>
    </Dropdown>
</div>
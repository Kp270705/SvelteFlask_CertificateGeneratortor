
<script>
  import { Popover, Button, Avatar } from "flowbite-svelte";
  import user from "../../assets/icons/user2.png";
  import FormDrawer from "../Drawer/FormDrawer.svelte";
  import routesType from "../../config/backend_routes";
  let hidden3 = $state(true);
  let token = $state('')
  let res = $state(null)
  let data = $state()

  let userName = $state('')
  let socialMediaLink = $state('')
  let userEmail = $state('')
  let userHobbies = $state('')

//   conat data2 = new FormData()


  // Use $effect for async operations
  $effect(() => {
    async function fetchData() {
      token = localStorage.getItem("jwt_token");
      
        try {
          res = await fetch(`${routesType.current_route}/auth/get-profile`, {
            headers: (token ? { Authorization: `Bearer ${token}` } : {})
          });

            data = await res.json();
            if (res.status===200){
                console.log(`Data get successfully...`)   
            userName = data.profile.userName
            userEmail = data.userEmail
            userHobbies = data.profile.userHobbies
            socialMediaLink = data.profile.socialMediaLink
            }
        } catch(err) {
          console.log(err);
        }
    }
    fetchData();
  });

</script>


<Popover class="w-64 bg-white text-sm font-light text-gray-500 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400">
  <div class="p-3">
    <div class="mb-2 flex items-center justify-between">
      <Avatar href="/" src={user} alt="Jese Leos" />
      <Button size="xs" onclick={()=>{hidden3=false}}>Edit Details</Button>
    </div>
    <div class="text-base leading-none font-semibold text-gray-900 dark:text-white">
      <a href="/">{userName}</a>
    </div>
    <div class="mb-3 text-sm font-normal">
      <a href="/" class="hover:underline">{userEmail}</a>
    </div>
    <div class="mb-4 text-sm font-light">
     <!-- {userHobbies} -->
     <!-- <br>  -->
     <strong>Social profile:</strong>
      <a href={socialMediaLink} class="text-primary-600 dark:text-primary-500 hover:underline">Your profile</a>
    </div>
    <ul class="flex text-sm font-light">
      <li class="me-2">
        <a href="/" class="hover:underline">
          <span class="font-semibold text-gray-900 dark:text-white">799</span>
          <span>Following</span>
        </a>
      </li>
      <li>
        <a href="/" class="hover:underline">
          <span class="font-semibold text-gray-900 dark:text-white">3,758</span>
          <span>Followers</span>
        </a>
      </li>
    </ul>
  </div>
</Popover>

<FormDrawer bind:hidden3 />
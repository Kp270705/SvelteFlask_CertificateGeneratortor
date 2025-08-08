<script>
  import { Drawer, Button, CloseButton, Label, Input, Textarea, P, A, Checkbox } from "flowbite-svelte";
  import { InfoCircleSolid } from "flowbite-svelte-icons";
  import { Footer, FooterCopyright, FooterLinkGroup, FooterBrand, FooterLink } from "flowbite-svelte";

  import routesType from "../../config/backend_routes";
  import user from "../../assets/icons/user2.png";
  
  let { hidden3 = $bindable(true) } = $props()

  // user details:


  async function editUserDetails(e){

    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    const token = localStorage.getItem("jwt_token")
    console.log(`token is: ${token}`)

    try {
      const response = await fetch(`${routesType.current_route}/auth/update-profile`, {
        method: 'POST',
        headers: {
            'Content-Type': `application/json`,
            'Authorization': `Bearer ${token}`  // your token here
        },
        body: JSON.stringify(data),
        credentials: "include",
        })

      const result = await response.json();
      console.log(`result is: ${result.message}`)
    } catch(err){
        console.log(err)
    }
  }

</script>


 <Drawer bind:hidden={hidden3} class="!w-[26rem] flex flex-col h-full">
  <!-- Header -->
  <div class="flex items-center justify-between">
    <h5
      id="drawer-label" class="mb-6 inline-flex items-center text-base font-semibold text-gray-500 uppercase dark:text-gray-400"
    >
      <InfoCircleSolid class="me-2.5 h-5 w-5" /> Edit your details
    </h5>
    <CloseButton class="mb-4 dark:text-white" />
  </div>

  <!-- Main content wrapper -->
  <div class="flex-1 overflow-y-auto">
    <form action="#" onsubmit={editUserDetails} class="space-y-6">
      <div>
        <Label for="userName" class="mb-2 block">Your Name</Label>
        <Input id="userName" name="userName" required placeholder="your name..." />
      </div>
      <div>
        <Label for="socialMediaLink" class="mb-2 block">Your social link</Label>
        <Input id="socialMediaLink" name="socialMediaLink" required placeholder="give your #public_profile_link..." />
      </div>
      <div>
        <Label for="userHobbies" class="mb-2">Your Hobbies</Label>
        <Textarea id="userHobbies" placeholder="Your hobbies..." rows={4} name="userHobbies" class="w-full" />
      </div>
      <Button type="submit" class="w-full">Update details</Button>
    </form>

    <div class="mt-6 space-y-1 border-t pt-4">
      <P class="text-sm text-gray-500 dark:text-gray-400">
        For any details contact:
        <A href="/" class="text-primary-600 dark:text-primary-500 hover:underline">https://github.com/Kp270705</A>
      </P>
      <P class="text-sm text-gray-500 dark:text-gray-400">
        <A href="/" class="text-primary-600 dark:text-primary-500 hover:underline">8979963277</A>
      </P>
    </div>
  </div>

  <!-- Footer pinned at bottom -->
  <Footer footerType="logo" class="mt-auto border-t pt-4">
    <div class="flex flex-col items-center gap-4 sm:flex-row sm:justify-between">
      <FooterBrand href="https://flowbite.com" src={user} alt="Flowbite Logo" name="Flowbite" />
      <FooterLinkGroup class="flex flex-wrap justify-center gap-3 text-sm text-gray-500 dark:text-gray-400">
        <FooterLink href="/">About</FooterLink>
        <FooterLink href="/">Privacy Policy</FooterLink>
        <FooterLink href="/">Licensing</FooterLink>
        <FooterLink href="/">Contact</FooterLink>
      </FooterLinkGroup>
    </div>
    <hr class="my-4 border-gray-200 dark:border-gray-700" />
    <FooterCopyright href="/" by="Flowbite™" />
  </Footer>
</Drawer>

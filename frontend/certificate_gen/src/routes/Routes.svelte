<!-- Logic of All routes is here: -->

<script>
  // importing svelte essentials
  import Router from 'svelte-spa-router';

  // importing components
  import TestCard from '../components/auth/Test.svelte';
  import Login from '../components/auth/Login.svelte';
  import Register from '../components/auth/Register.svelte';

  // importing pages:
  import About from '../pages/About.svelte';
  import Acknowledgement from '../pages/Acknowledgement.svelte';
  import Landing from '../pages/Landing.svelte';
  import Protected from '../pages/Protected.svelte';

  // export let isLogin
  const routes = {
    '/': Landing,
    '/home': Protected,
    '/about': About,
    '/register': Register,
    '/login': Login,
    '/card': TestCard,
    '/acknowledgement': Acknowledgement, // <-- Route added
  };
</script>


<Router {routes} />

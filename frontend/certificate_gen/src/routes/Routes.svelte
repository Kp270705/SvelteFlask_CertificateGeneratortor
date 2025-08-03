<script>
  import Router from 'svelte-spa-router';

  import Home from '../pages/Home.svelte';
  import About from '../pages/About.svelte';
  import Register from '../components/Signup/Signup.svelte';
  import Login from '../components/Login/Login.svelte';
  import Acknowledgement from '../pages/Acknowledgement.svelte';

  const routes = {
    '/': Home,
    '/about': About,
    '/login': Login,
    '/register': Register,
    '/acknowledgement': Acknowledgement, // <-- Route added
  };
</script>

<Router {routes} />

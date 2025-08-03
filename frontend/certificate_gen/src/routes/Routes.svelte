<script>
  import Router from 'svelte-spa-router';

  // import Home from '../pages/Home.svelte';
  import Protected from '../pages/Protected.svelte';
  import About from '../pages/About.svelte';
  import Register from '../components/auth/Register.svelte';
  import Login from '../components/auth/Login.svelte';
  import Acknowledgement from '../pages/Acknowledgement.svelte';
  import Landing from '../pages/Landing.svelte';

  const routes = {
    '/': Landing,
    '/home': Protected,
    '/about': About,
    '/login': Login,
    '/register': Register,
    '/acknowledgement': Acknowledgement, // <-- Route added
  };
</script>

<Router {routes} />

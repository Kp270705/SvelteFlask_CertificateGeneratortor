import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [tailwindcss(), svelte()],
  server: {
    cors: true,
    allowedHosts: ['b579d3eedfba.ngrok-free.app'],
  }
});

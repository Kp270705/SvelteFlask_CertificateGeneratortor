// src/stores/authStore.js
import { writable } from 'svelte/store';

export const isAuthorized = writable(false);
export const authRoute = writable('Sign-In');

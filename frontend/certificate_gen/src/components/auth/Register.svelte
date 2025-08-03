<script lang="ts">
	import { Section, Register } from 'flowbite-svelte-blocks';
	import { link } from 'svelte-spa-router';
	import { Button, Checkbox, Label, Input } from 'flowbite-svelte';
	import { push } from 'svelte-spa-router';

	async function handleSubmit(e) {
		e.preventDefault();

		const form = e.target;
		const formData = new FormData(form);
		const data = Object.fromEntries(formData.entries());

		try {
			const response = await fetch("http://localhost:5000/auth/register", {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify(data),
				credentials: "include",
			});

			const result = await response.json();
			if (!response.ok) {
				throw new Error(result.error || `Server responded with ${response.status}`);
			}

			console.log("✅ Backend Response:", result);
			alert("🎉 user registered successfully!");
			push('/login');
		} catch (error) {
			console.error("❌ Register...Submission failed:", error);
			alert("❗" + error.message);
		}
	}


</script>

<Section name="register">
	<Register href="/">
		{#snippet top()}
			<img class="mr-2 h-8 w-8" src="/images/logo.svg" alt="logo" />
			Flowbite
		{/snippet}
		<div class="space-y-4 p-6 sm:p-8 md:space-y-6">
			<form class="flex flex-col space-y-6" on:submit={handleSubmit}>
				<h3 class="p-0 text-xl font-medium text-gray-900 dark:text-white">Change Password</h3>
				<Label class="space-y-2">
					<span>Your email</span>
					<Input type="email" name="email" placeholder="name@company.com" required />
				</Label>
				<Label class="space-y-2">
					<span>Your password</span>
					<Input type="password" name="password" placeholder="•••••" required />
				</Label>
				
				<Button type="submit" class="w-full1">Register</Button>
				<p class="text-sm font-light text-gray-500 dark:text-gray-400">
					Already have an account? <a use:link href="/login" class="text-primary-600 dark:text-primary-500 font-medium hover:underline">Login</a>
				</p>
			</form>
		</div>
	</Register>
</Section>
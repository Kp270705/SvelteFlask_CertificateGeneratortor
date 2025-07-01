<script>
  let backendMessage = "";
  let backendMessage2 = "";
  let backendMessage2b = "";
  let name = "Kunal";
  import { onMount } from "svelte";
  // Fetch a message from backend on mount
  onMount(async () => {

    const res = await fetch("http://localhost:5000/api/hello");
    const data = await res.json();
    backendMessage = data.message;

    const res2 = await fetch("http://localhost:5000/api/testApi");
    const data2 = await res2.json();
    console.log("Response from testApi:", data2);
    backendMessage2 = data2.test_message;

    const res2b = await fetch("http://localhost:5000/api/testApi2");
    const data2b = await res2b.json();
    console.log("Response from testApi2:", data2b);
    backendMessage2b = data2b.test_message2;
    
  });


  async function sendName() {
    const res = await fetch("http://localhost:5000/api/send", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name })
    });
    const result = await res.json();
    console.log("Response from backend:", result);
    console.log("Name: ", result.data.name);
  }
</script>

<h1>Certificate Generator</h1>
<p>{backendMessage}</p>
<hr>
<p>{backendMessage2}</p>
<hr>
<p>{backendMessage2b}</p>
<hr>

<input bind:value={name} placeholder="Enter your name" />
<button on:click={sendName}>Send to backend</button>

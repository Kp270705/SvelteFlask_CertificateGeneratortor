<script>
  import { onMount } from "svelte";

  let name = "Kunal";
  let messages = {
    hello: "",
    testApi: "",
    testApi2: ""
  };
  const endpoints = [
    { key: "hello", url: "http://localhost:5000/api/hello", field: "message" },
    { key: "testApi", url: "http://localhost:5000/api/testApi", field: "test_message" },
    { key: "testApi2", url: "http://localhost:5000/api/testApi2", field: "test_message2" }
  ];

  onMount(async () => {
    await Promise.all(endpoints.map(async (ep) => {
      const res = await fetch(ep.url);
      const data = await res.json(); // data is json type, and it have a field with the name of ep.field.
      console.log(data); // data is object type
      messages[ep.key] = data[ep.field];
    }));
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
    // console.log("Name: ", result.data.name);
  }
</script>

<h1>Certificate Generator</h1>

<hr>
<p>{messages.hello}</p>
<hr>
<p>{messages.testApi}</p>
<hr>
<p>{messages.testApi2}</p>
<hr>

<input bind:value={name} placeholder="Enter your name" />
<button on:click={sendName}>Send to backend</button>

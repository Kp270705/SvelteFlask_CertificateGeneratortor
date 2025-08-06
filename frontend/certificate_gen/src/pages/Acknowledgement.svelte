<script>

    // export let navigate;
    export let userName = "User";

    import Hurrah from "../assets/Images/acknowledgement/ack1.gif";

    let selectedOptions = {
        download: false,
        send: false
    };

    async function downloadZip() {
        try {
            const response = await fetch("http://localhost:5000/api/download-zip", {
                method: "GET",
                credentials: "include",
            });

            if (!response.ok) {
                const result = await response.json();
                throw new Error(result.error || "Download failed");
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "certificates.zip";
            a.click();
            window.URL.revokeObjectURL(url);
        } catch (err) {
            alert("❌ " + err.message);
        }
    }

    async function sendCertificates() {
        try {
            const res = await fetch("http://localhost:5000/api/send-mails", {
                method: "POST",
            });

            const result = await res.json();
            if (!res.ok) throw new Error(result.error || "Failed to send mails");

            alert("✅ Emails sent successfully!");
        } catch (err) {
            alert("❌ " + err.message);
        }
    }

    function handleSubmit() {
        if (selectedOptions.download) {
            downloadZip();
        }
        if (selectedOptions.send) {
            sendCertificates();
        }
        if (!selectedOptions.download && !selectedOptions.send) {
            alert("❗ Please select at least one option to proceed.");
        }
    }

</script>



<div class="acknowledgement-page">
    <div class="floating-elements">
        <div class="floating-element">🎉</div>
        <div class="floating-element">✨</div>
        <div class="floating-element">🏆</div>
        <div class="floating-element">🎊</div>
        <div class="floating-element">🎈</div>
        <div class="floating-element">⭐</div>
    </div>
    
    <div class="content-wrapper">
        <h1 class="success-title">
            🎉 <span class="title-white">Certificates Created</span> <span class="title-yellow">Successfully!</span>
        </h1>
        <p class="success-subtitle">
            Hi <span class="username">{userName}</span>, your certificates have been generated with success!
        </p>
        
        <div class="gif-container">
            <img src="{Hurrah}" alt="Success celebration" class="gif-image" />
        </div>

        <div class="options-container">
            <div class="option-card" class:selected={selectedOptions.download}>
                <label class="option-label">
                    <input 
                        type="checkbox" 
                        bind:checked={selectedOptions.download} 
                        class="option-checkbox"
                    />
                    <span class="option-icon">📦</span>
                    <span class="option-text">Download ZIP of all certificates</span>
                </label>
            </div>
            
            <div class="option-card" class:selected={selectedOptions.send}>
                <label class="option-label">
                    <input 
                        type="checkbox" 
                        bind:checked={selectedOptions.send} 
                        class="option-checkbox"
                    />
                    <span class="option-icon">✉️</span>
                    <span class="option-text">Send certificates to recipients</span>
                </label>
            </div>
            <!-- <button on:click={goBack} class="proceed-btn">⬅️ Back</button>  -->

        </div>

        <button class="proceed-btn" on:click={handleSubmit}> Proceed </button>
    </div>
</div>

<style>
    /* Reset any potential margin/padding constraints */
    :global(body) {
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }
    
    .acknowledgement-page {
        width: 100vw;
        min-height: 100vh;
        margin: 0;
        padding: 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        box-sizing: border-box;
    }

    .acknowledgement-page::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 80%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
        pointer-events: none;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .content-wrapper {
        width: 100%;
        max-width: 1200px;
        padding: 2rem;
        text-align: center;
        position: relative;
        z-index: 1;
        box-sizing: border-box;
    }

    .success-title {
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 1.5rem;
        text-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        line-height: 1.2;
        width: 100%;
    }

    .title-white {
        color: white;
    }

    .title-yellow {
        color: #ffeaa7;
        animation: yellowGlow 2s ease-in-out infinite alternate;
    }

    @keyframes yellowGlow {
        0% { text-shadow: 0 8px 16px rgba(0, 0, 0, 0.3), 0 0 20px rgba(255, 234, 167, 0.3); }
        100% { text-shadow: 0 8px 16px rgba(0, 0, 0, 0.3), 0 0 30px rgba(255, 234, 167, 0.8); }
    }

    .success-subtitle {
        font-size: 1.8rem;
        color: white;
        margin-bottom: 3rem;
        font-weight: 600;
        text-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        width: 100%;
    }

    .username {
        background: linear-gradient(45deg, #ffeaa7, #fab1a0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }

    .gif-container {
        margin: 3rem 0;
        position: relative;
        display: flex;
        justify-content: center;
        width: 100%;
    }

    .gif-image {
        width: 90vw;
        max-width: 800px;
        height: 500px;
        object-fit: cover;
        border-radius: 2rem;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
        border: 6px solid rgba(255, 255, 255, 0.9);
        animation: imageGlow 2s ease-in-out infinite alternate;
    }

    @keyframes imageGlow {
        0% { 
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4), 0 0 0 rgba(255, 255, 255, 0.9);
            transform: scale(1);
        }
        100% { 
            box-shadow: 0 40px 80px rgba(0, 0, 0, 0.5), 0 0 50px rgba(255, 255, 255, 0.6);
            transform: scale(1.02);
        }
    }

    .options-container {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
        margin: 3rem 0;
        width: 100%;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }

    .option-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border: 3px solid rgba(255, 255, 255, 0.5);
        border-radius: 1.5rem;
        padding: 1.8rem;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        width: 100%;
        box-sizing: border-box;
    }

    .option-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        border-color: #667eea;
    }

    .option-card.selected {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-color: #667eea;
        color: white;
        transform: translateY(-3px);
    }

    .option-card.selected::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        animation: shimmer 2s infinite;
    }

    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }

    .option-label {
        display: flex;
        align-items: center;
        gap: 1rem;
        font-size: 1.3rem;
        font-weight: 700;
        cursor: pointer;
        position: relative;
        z-index: 1;
    }

    .option-checkbox {
        width: 24px;
        height: 24px;
        accent-color: #667eea;
        transform: scale(1.3);
        cursor: pointer;
    }

    .option-icon {
        font-size: 1.8rem;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
    }

    .option-text {
        flex: 1;
        text-align: left;
        color: darkblue;
    }

    .proceed-btn {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 1.5rem 3rem;
        font-size: 1.4rem;
        font-weight: 800;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.5);
        position: relative;
        overflow: hidden;
        margin-top: 2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .proceed-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.5s;
    }

    .proceed-btn:hover::before {
        left: 100%;
    }

    .proceed-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 20px 50px rgba(102, 126, 234, 0.7);
    }

    .proceed-btn:active {
        transform: translateY(-1px);
    }

    .floating-elements {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        overflow: hidden;
    }

    .floating-element {
        position: absolute;
        font-size: 3rem;
        opacity: 0.7;
        animation: float 6s ease-in-out infinite;
    }

    .floating-element:nth-child(1) {
        top: 10%;
        left: 10%;
        animation-delay: 0s;
    }

    .floating-element:nth-child(2) {
        top: 15%;
        right: 10%;
        animation-delay: 1s;
    }

    .floating-element:nth-child(3) {
        bottom: 25%;
        left: 15%;
        animation-delay: 2s;
    }

    .floating-element:nth-child(4) {
        bottom: 15%;
        right: 15%;
        animation-delay: 3s;
    }

    .floating-element:nth-child(5) {
        top: 40%;
        left: 5%;
        animation-delay: 4s;
    }

    .floating-element:nth-child(6) {
        top: 50%;
        right: 5%;
        animation-delay: 5s;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-30px) rotate(10deg); }
        66% { transform: translateY(-15px) rotate(-10deg); }
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
        .content-wrapper {
            padding: 1rem;
        }
        
        .success-title {
            font-size: 2.5rem;
        }
        
        .success-subtitle {
            font-size: 1.3rem;
        }
        
        .gif-image {
            width: 95vw;
            max-width: 500px;
            height: 350px;
        }
        
        .option-label {
            font-size: 1.1rem;
        }
        
        .option-card {
            padding: 1.5rem;
        }
        
        .proceed-btn {
            padding: 1.2rem 2rem;
            font-size: 1.2rem;
        }
        
        .floating-element {
            font-size: 2rem;
        }
    }

    @media (max-width: 480px) {
        .success-title {
            font-size: 2rem;
        }
        
        .success-subtitle {
            font-size: 1.1rem;
        }
        
        .gif-image {
            width: 90vw;
            max-width: 400px;
            height: 280px;
        }
        
        .option-label {
            font-size: 1rem;
        }
        
        .options-container {
            gap: 1rem;
        }
    }
</style>





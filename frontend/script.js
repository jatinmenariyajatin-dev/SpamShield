document.getElementById('checkBtn').addEventListener('click', async () => {
    const messageText = document.getElementById('messageInput').value.trim();
    const resultDiv = document.getElementById('result');

    //Validation check
    if (!messageText) {
        alert('Please enter a message first!');
        return;
    }

    //loading state UI
    resultDiv.style.display = 'block';
    resultDiv.className = 'result-box'; 
    resultDiv.style.backgroundColor = '#eee';
    resultDiv.style.color = '#333';
    resultDiv.innerText = 'Analyzing...';

    try {
        //Make HTTP POST request to local Flask API
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: messageText })
        });

        const data = await response.json();

        //Update UI based on API response
        if (response.ok) {
            if (data.label === 'Spam') {
                resultDiv.className = 'result-box spam';
                resultDiv.innerHTML = `🚨 ALERT: SPAM (${data.confidence} Match)`;
            } else {
                resultDiv.className = 'result-box ham';
                resultDiv.innerHTML = `✅ SAFE: HAM (${data.confidence} Match)`;
            }
        } else {
            resultDiv.innerText = `Error: ${data.error || 'Server issue'}`;
        }

    } catch (error) {
        console.error('Error connecting to backend:', error);
        resultDiv.innerText = 'Error: Cannot connect to Python backend.';
    }
});
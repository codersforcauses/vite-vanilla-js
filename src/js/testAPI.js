export async function callApi1() {
    try {
        const response = await fetch("http://localhost:8000/api/getFunction/");
        const data = await response.json();
        document.getElementById("api1Response").innerText = data.message;
    } catch (error) {
        console.error("Error calling API 1:", error);
    }
}

export async function callApi2() {
    try {
        const response = await fetch("http://localhost:8000/api/postFunction", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text: "Hello from Vite!",
            }),
        });
        const data = await response.json();
        document.getElementById("api2Response").innerText = data.message;
    } catch (error) {
        console.error("Error calling API 2:", error);
    }
}

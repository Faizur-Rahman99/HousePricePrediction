const form = document.getElementById("prediction-form");
const result = document.getElementById("result");
const button = document.getElementById("predict-btn");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const data = {
        MedInc: parseFloat(document.getElementById("MedInc").value),
        HouseAge: parseFloat(document.getElementById("HouseAge").value),
        AveRooms: parseFloat(document.getElementById("AveRooms").value),
        AveBedrms: parseFloat(document.getElementById("AveBedrms").value),
        Population: parseFloat(document.getElementById("Population").value),
        AveOccup: parseFloat(document.getElementById("AveOccup").value),
        Latitude: parseFloat(document.getElementById("Latitude").value),
        Longitude: parseFloat(document.getElementById("Longitude").value)
    };

    button.disabled = true;
    button.innerText = "Predicting...";

    result.innerHTML = `
        <h3>⏳ Predicting...</h3>
    `;

    try {

        const response = await fetch(
            "https://housepriceprediction-lyyr.onrender.com/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        if (!response.ok) {
            throw new Error("Prediction request failed.");
        }

        const prediction = await response.json();

        button.disabled = false;
        button.innerText = "Predict Price";

        const price = prediction.predicted_price * 100000;

        result.innerHTML = `
            <div class="prediction-card">
                <h2>🏠 Estimated House Price</h2>
        
                <h1>$${price.toLocaleString()}</h1>
        
                <p>Predicted using the Random Forest Regression model.</p>
            </div>
        `;

        console.log(prediction);

    } catch (error) {

        console.error(error);

        button.disabled = false;
        button.innerText = "Predict Price";

        result.innerHTML = `
            <div class="prediction-card">
                <h2>⚠ Prediction Failed</h2>
        
                <p>
                    Unable to contact the prediction server.
                    Please try again.
                </p>
            </div>
        `;
    }

});
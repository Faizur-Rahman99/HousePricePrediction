const form = document.getElementById("prediction-form");
const result = document.getElementById("result");

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

    result.innerHTML = "Predicting...";

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

        result.innerHTML = `
            <h3>Predicted House Price</h3>
            <p><strong>${prediction.predicted_price}</strong></p>
            <p>${prediction.unit}</p>
        `;

        console.log(prediction);

    } catch (error) {

        console.error(error);

        result.innerHTML = `
            <p style="color:red;">
                Failed to connect to the prediction API.
            </p>
        `;
    }

});
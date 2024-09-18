// URLs for fetching the data
const firstURL = 'https://statfin.stat.fi/PxWeb/sq/4e244893-7761-4c4f-8e55-7a8d41d86eff';
const secondURL = 'https://statfin.stat.fi/PxWeb/sq/5e288b40-f8c8-4f1e-b3b0-61b86ce5c065';

// Function to get the datasets from the APIs
async function fetchData() {
    try {
        const firstDataSet = await fetch(firstURL);
        const firstData = await firstDataSet.json();

        const secondDataSet = await fetch(secondURL);
        const secondData = await secondDataSet.json();

        // Populate the table with the data
        pushToTable(firstData, secondData);
    } catch (e) {
        console.log(" Error occurred while fetching data: ", e);
    }
}

// Function to populate the datatable
function pushToTable(firstData, secondData) {
    const tbody = document.getElementById("tbody");
    const municipalityData = firstData.dataset.dimension.Alue.category.label;
    const populationData = firstData.dataset.value;
    const employmentData = secondData.dataset.value;

    /* Then we loop through the first dataset by using Object.keys() to get the
    municipality values and the Object.values() is replaced by the value in the key-value pair*/ 
    Object.keys(municipalityData).forEach((key, value) => {
        const municipality = municipalityData[key];
        const population = populationData[value];
        const employment = employmentData[value];
        const percentage = ((employment / population) * 100).toFixed(2);

        // Creating a new row
        const row = document.createElement("tr");

        /* Check whether the row is even or odd. +1 is added because for example 
        the first row has an index of 0 so it makes it even but it should be odd*/
        if ((value + 1) % 2 === 0) {
            row.className = "even";
        } else {
            row.className = "odd";
        }

        const firstCell = document.createElement("td");
        firstCell.innerText = municipality;

        const secondCell = document.createElement("td");
        secondCell.innerText = population;

        const thirdCell = document.createElement("td");
        thirdCell.innerText = employment;

        const fourthCell = document.createElement("td");
        fourthCell.innerText = percentage + "%";

        row.appendChild(firstCell);
        row.appendChild(secondCell);
        row.appendChild(thirdCell);
        row.appendChild(fourthCell);

        // Add the corresponding class based on the employment percentage
        if (percentage > 45) {
            row.className = "over";
        } else if (percentage < 25) {
            row.className = "under";
        }

        // Append the row
        tbody.appendChild(row);

    });

}
// Call the fetchData function
fetchData();

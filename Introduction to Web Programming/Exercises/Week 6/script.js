const url = 'https://statfin.stat.fi/PxWeb/api/v1/en/StatFin/synt/statfin_synt_pxt_12dy.px';
const submitButton = document.getElementById("submit-data");
const jsonQuery = {
    "query": [
        {
            "code": "Vuosi",
            "selection": {
                "filter": "item",
                "values": [
                    "2000",
                    "2001",
                    "2002",
                    "2003",
                    "2004",
                    "2005",
                    "2006",
                    "2007",
                    "2008",
                    "2009",
                    "2010",
                    "2011",
                    "2012",
                    "2013",
                    "2014",
                    "2015",
                    "2016",
                    "2017",
                    "2018",
                    "2019",
                    "2020",
                    "2021"
                ]
            }
        },
        {
            "code": "Alue",
            "selection": {
                "filter": "item",
                "values": ["SSS"]
            }
        },
        {
            "code": "Tiedot",
            "selection": {
                "filter": "item",
                "values": [
                    "vaesto"
                ]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
};

submitButton.addEventListener("click", () => {
    // To prevent page reloading on submitting form
    event.preventDefault();
    municipalityChart();
})

const fetchData = async () => {
    const res = await fetch(url, {
        method: 'POST',
        headers: {'content-type': 'application/json'},
        body: JSON.stringify(jsonQuery)
    });

    if(!res.ok) {
        return;
    }

    const data = await res.json();

    return data;
};

const buildChart = async () => {
    const data = await fetchData();
    const labels = Object.values(data.dimension.Vuosi.category.label);
    const values = Object.values(data.value);
    const areas = Object.values(data.dimension.Alue.category.label);
    let year = labels[labels.length - 1]; // Keep track of the next year

    const chartData = {
        labels: labels,
        datasets: [{
            name: areas[0],
            values: values
        }]
    }

    const chart = new frappe.Chart("#chart", {
        title: `Population growth in ${areas[0]}`,
        data: chartData,
        type: "line",
        height: 450,
        colors: ["#eb5146"]
    })

    // Estimating the data
    document.getElementById("add-data").addEventListener("click", () => {
        year++;
        newValue = calculateEstimatedValue(values);
        chart.addDataPoint(year.toString(), [newValue]);
        values.push(newValue);
    });
};

// Functions to build charts for single municipalities
const municipalityChart = async () => {
    // Store the user input and reset the search field
    const name = document.getElementById("input-area").value.toLowerCase();
    document.getElementById("input-area").value = "";

    const res = await fetch(url, {
        method: "GET",
        headers: {"content-type": "application/json"}
    });

    if(!res.ok) {
        return;
    }

    const data = await res.json();
    // Get the valueTexts
    const valueTexts = data.variables[1].valueTexts.map(text => text.toLowerCase());
    // Find the index
    const index = valueTexts.indexOf(name);

    const key = data.variables[1].values[index];
    // Finally edit the jsonQuery to corresponding user search
    jsonQuery.query[1].selection.values[0] = key;

    buildChart();
};

const calculateEstimatedValue = (values) => {
    let newValue = 0;
    for (let i = 1; i < values.length; i++) {
        newValue += (values[i] - values[i - 1]);
    }
    newValue = (newValue / (values.length - 1)) + values[values.length - 1];
    return Math.round(newValue);
};

if (document.readyState === "loading") {

    document.addEventListener("DOMContentLoaded", buildChart());

} else {

    buildChart();

};

// Switch to birth and death chart
document.getElementById('navigation').addEventListener('click', () => {
    window.location.href = 'newchart.html';
});

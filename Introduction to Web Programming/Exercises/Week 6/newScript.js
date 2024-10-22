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
                "values": []
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
};

const fetchData = async () => {
    const url = 'https://statfin.stat.fi/PxWeb/api/v1/en/StatFin/synt/statfin_synt_pxt_12dy.px';
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
    //Fetch both births and deaths
    jsonQuery.query[2].selection.values = ["vm01"];
    const births = await fetchData(); 

    jsonQuery.query[2].selection.values = ["vm11"];
    const deaths = await fetchData();

    const labels = Object.values(births.dimension.Vuosi.category.label);
    const areas = Object.values(births.dimension.Alue.category.label);

    const chartData = {
        labels: labels,
        datasets: [{
            name: "Births",
            values: births.value
        },
        {
            name: "Deaths",
            values: deaths.value
        }]
    }

    const chart = new frappe.Chart("#chart", {
        title: `Births and deaths in ${areas[0]}`,
        data: chartData,
        type: "bar",
        height: 450,
        colors: ["#63d0ff", "#363636"]
    })
};

if (document.readyState === "loading") {

    document.addEventListener("DOMContentLoaded", buildChart());

} else {

    buildChart();

}

// Switch back to population growth chart
document.getElementById('navigation').addEventListener('click', () => {
    window.location.href = 'index.html';
});

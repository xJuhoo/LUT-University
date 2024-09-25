const firstUrl = "https://geo.stat.fi/geoserver/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=tilastointialueet:kunta4500k&outputFormat=json&srsName=EPSG:4326";
const secondUrl = "https://statfin.stat.fi/PxWeb/sq/4bb2c735-1dc3-4c5e-bde7-2165df85e65f";
const thirdUrl = "https://statfin.stat.fi/PxWeb/sq/944493ca-ea4d-4fd9-a75c-4975192f7b6e";

async function fetchData() {
    const firstData = await fetch(firstUrl);
    const geoData = await firstData.json();
    
    const secondData = await fetch(secondUrl);
    const positiveData = await secondData.json();

    const thirdData = await fetch(thirdUrl);
    const negativeData = await thirdData.json();

    createMap(geoData, positiveData, negativeData);
};

// Function to initialize the map (from week 5 lecture videos)
const createMap = (geoData, positiveData, negativeData) => {
    let map = L.map("map", {
        minZoom: -3
    });

    let geoJson = L.geoJSON(geoData, {
        /* Here we need to pass in the feature and/or the layer in our functions or otherwise
        they will be undefined.*/
        onEachFeature: (feature, layer) => getFeature(feature, layer, positiveData, negativeData),
        style: (feature) => getStyle(feature, positiveData, negativeData)
    }).addTo(map);

    let osm = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 20,
        weight: 2,
        attribution: "© OpenStreetMap",
    }).addTo(map);

    // Fitting the map to the GeoJSON data
    map.fitBounds(geoJson.getBounds())
};

const getFeature = (feature, layer, positiveData, negativeData) => {
    if (!feature.properties.name) return;
    console.log(feature.properties.name);

    /* We need the index of the municipalities right after "KU" to find information
    from the second and third datasets*/
    const id = "KU" + feature.properties.kunta;

    // Find the correct values
    const index = positiveData.dataset.dimension.Tuloalue.category.index[id];
    positiveMig = positiveData.dataset.value[index];
    negativeMig = negativeData.dataset.value[index];

    layer.bindPopup(
        `<ul>
            <li>Name: ${feature.properties.name}</li>
            <li>Positive migration: ${positiveMig}</li>
            <li>Negative migration: ${negativeMig}</li>
        </ul>`
    );

    layer.bindTooltip(feature.properties.name);
};

const getStyle = (feature, positiveData, negativeData) => {
    if (!feature.properties.name) return;

    // Here we do the same steps as in the getFeature() function
    const id = "KU" + feature.properties.kunta;

    const index = positiveData.dataset.dimension.Tuloalue.category.index[id];
    positiveMig = positiveData.dataset.value[index];
    negativeMig = negativeData.dataset.value[index];

    const hue = calculateHue(positiveMig, negativeMig);

    // Return the calculated color
    return { color: `hsl(${hue}, 75%, 50%)`, fillOpacity: 0.3 };
};

// To calculate the hue
const calculateHue = (positiveMig, negativeMig) => Math.min((positiveMig / negativeMig) ** 3 * 60, 120);

fetchData();

// Find the container
const container = document.querySelector(".container");
// Choose five random breeds
const breeds = ["beagle", "labrador", "husky", "elkhound", "whippet"];

// Function to fetch the data
const fetchData = async (breed) => {
    let txtData, imgData;
    try {
        const txtResponse = await fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${breed}`);
        txtData = await txtResponse.json();

        const imgResponse = await fetch(`https://dog.ceo/api/breed/${breed}/images/random`);
        imgData = await imgResponse.json();
    } catch (error) {
        console.log("Error occurred while fetching data: ", error);
        return;
    }

    return [txtData, imgData];
}

const createItem = async (breed) => {
    const data = await fetchData(breed);

    if (!data) {
        console.log("Something went wrong...");
        return;
    }

    // Creating the HTML element
    const item = document.createElement("div");
    item.className = "wiki-item";

    const header = document.createElement("h1");
    header.className = "wiki-header";
    // Found a way to write the breed so that only the first letter is in uppercase from:
    // https://stackoverflow.com/questions/36996698/how-do-i-lowercase-any-string-and-then-capitalize-only-the-first-letter-of-the-w
    header.textContent = breed.charAt(0).toUpperCase() + breed.slice(1);
    item.appendChild(header);

    const content = document.createElement("div");
    content.className = "wiki-content";

    const text = document.createElement("p");
    text.className = "wiki-text";
    text.textContent = data[0].extract;
    content.appendChild(text);

    const imgContainer = document.createElement("div");
    imgContainer.className = "img-container";

    const img = document.createElement("img");
    img.className = "wiki-img";

    img.src = data[1].message;
    imgContainer.appendChild(img);
    content.appendChild(imgContainer);

    // Append content to main item
    item.appendChild(content);

    // Append item to the container
    container.appendChild(item);
}
// Function to run the program (needs to be async function, otherwise the breeds might load in different orders)
const generate = async () => {
    // Iterate through the list of breeds and generate a wiki item for each
    for (const breed of breeds) {
        await createItem(breed);
    }
}

// Make sure that the page is loaded before execution
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", generate);
} else {
    generate();
}

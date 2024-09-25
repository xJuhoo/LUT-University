const button = document.getElementById("submit-data");
const showContainer = document.getElementById("show-container")
const url = "https://api.tvmaze.com/search/shows?q=";

button.addEventListener("click", () => {
    event.preventDefault();
    // Clear previous results
    showContainer.innerHTML = "";
    fetchData();
} )

async function fetchData() {
    const query = document.getElementById("input-show").value;
    try {
        let search = url + query;
        let response = await fetch(search);
        let data = await response.json();

        createShows(data);
    } catch (e) {
        console.log(" Error occurred while fetching data: ", e);
    }
}

function createShows(data) {
    /* Since the API already returns an array, Object.values() is not needed and we can loop through 
     the array right away */
    data.forEach(function(item) {

        // Creating a div for each tvshow
        const tvShow = document.createElement("div");
        tvShow.className = "show-data";

        // Get the show's image if available
        let img = document.createElement("img");
        if (item.show.image && item.show.image.medium) {
            img.src = item.show.image.medium;
            tvShow.appendChild(img);
        }

        // Create a div for the show's information
        const showInformation = document.createElement("div");
        showInformation.className = "show-info";

        // Create the title element for the show's name
        const showTitle = document.createElement("h1");
        showTitle.innerText = item.show.name;
        showInformation.appendChild(showTitle);

        // Check if the show has a summary
        if (item.show.summary) {
            let summary = document.createElement("p")
            summary.innerHTML = item.show.summary; // Already in HTML format
            showInformation.appendChild(summary);
        }

        // Add the information div (with title and summary) to the main div
        tvShow.appendChild(showInformation);

        // Finally, we add the complete div to the container
        showContainer.appendChild(tvShow);
    });
}

document.getElementById("submit-data").addEventListener("click", function() {
    event.preventDefault();
    // Print something to check if we got this far
    console.log("Data has been submitted.");

    const table = document.getElementById("datatable");
    const userName = document.getElementById("input-username").value;
    const email = document.getElementById("input-email").value;
    const isAdmin = document.getElementById("input-admin").checked ? "X" : "-";
    const image = document.getElementById("input-image");

    let exists = false;

    // Loop through table rows to check for existing user
    // Using Array.from() method from https://www.w3schools.com/jsref/jsref_from.asp
    let rows = Array.from(table.rows).slice(1); // Slice to exclude the labels
    for (let i = 0; i < rows.length; i++) {
        let cells = rows[i].cells;
        if (cells[0].innerHTML === userName) {
            cells[1].innerHTML = email;
            cells[2].innerHTML = isAdmin;
            addImage(cells[3], image);
            exists = true;
            break;
        }
    }
    // If the user doesn't already exist, add a new data row
    if (!exists) {
        let newDataRow = table.insertRow();
        newDataRow.insertCell().innerHTML = userName;
        newDataRow.insertCell().innerHTML = email;
        newDataRow.insertCell().innerHTML = isAdmin;
        newDataRow.insertCell().innerHTML = "";
        addImage(newDataRow.cells[3], image);
    }
});

// Function to add images
function addImage(target, file) {
    // Clearing any previous images
    target.innerHTML = "";

    // Check if the file exists
    if (file.files.length) {
        // Create a new image
        let image = document.createElement("img");
        image.width = 64;
        image.height = 64;
        image.src = URL.createObjectURL(file.files[0]);
        target.appendChild(image);
    }
};

// Clearing the HTML table
document.getElementById("empty-table").addEventListener("click", function() {
    let table = document.getElementById("datatable");
    // Found a simple way to delete the table from here: 
    // https://stackoverflow.com/questions/7271490/delete-all-rows-in-an-html-table
    while (table.rows.length > 1) {
        table.deleteRow(1);
    }
});
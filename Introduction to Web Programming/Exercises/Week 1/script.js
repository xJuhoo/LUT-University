document.getElementById("my-button").addEventListener("click", function() {
    console.log("hello world");
    // Change the header 
    document.getElementById("h1").innerText = "Moi maailma";
});

// This part I did similar to what was shown in the lecture videos
document.getElementById("add-data").addEventListener("click", function() {
    const listItems = document.getElementById("my-list");
    let newText = document.createElement("li");
    newText.innerText = document.getElementById("list-text").value
    listItems.appendChild(newText);
});
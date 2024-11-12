// When a new user data is submitted
document.getElementById("userForm").addEventListener("submit", async function() {
  event.preventDefault()

  const name = document.getElementById("name").value
  const email = document.getElementById("email").value
  try {
      const response = await fetch("http://localhost:3000/users", {
          method: "POST",
          headers: {
              "Content-type": "application/json"
          },
          body: JSON.stringify({ name, email })
      })
      const result = await response.json()
      // To display the message on the screen
      alert(result.message);
      document.getElementById("name").value = ""
      document.getElementById("email").value = ""
  } catch (error) {
      console.log("An error occurred while fetching data: ", error)
  }
})

// For fetching users
document.getElementById("getUsers").addEventListener("click", async function() {
  try {
    const response = await fetch("http://localhost:3000/users")
    const data = await response.json()
    // Get the userlist
    const userList = document.getElementById("userList")
    userList.innerHTML = ""
    // Iterate through the users and add them to the list
    data.users.forEach((user) => {
      const item = document.createElement("li")
      item.textContent = `${user.name} - ${user.email}`
      userList.appendChild(item)
    })
  } catch (error) {
    console.error("An error occurred while fetching data: ", error)
  }
})

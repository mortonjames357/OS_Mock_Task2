// Function to scroll down to view the products on the home page
function goToProducts(){
    window.scrollTo(0, 1060)
}

// Function for a button to scroll back to the top of the page
function backToTop(e){
    e.preventDefault()
    window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
}

// Function to apply all dark mode styling
function darkModeToggle(){
    console.log("clicked")
    // Get the document root
    const root = document.documentElement;
    // Get the body 
    const body = document.getElementsByTagName("BODY")[0];
    // Get the value of backgound color in body
    var value = getComputedStyle(body).getPropertyValue('--backgroud-color');

    if (value == "#242424"){
        // Set values back to origional
        root.style.setProperty('--backgroud-color', '#FFFBF8')
        root.style.setProperty('--font-color', '#242424')
        root.style.setProperty('--table-color', 'lightgray')
        root.style.setProperty('--input-color', 'white')
        // Change Image
        document.getElementById('titleImg').src="../static/imgs/RolsaTechWhiteLogo.png"
    }
    else {
        // Update the CSS variable
        root.style.setProperty('--backgroud-color', '#242424');
        root.style.setProperty('--font-color', '#FFFBF8')
        root.style.setProperty('--table-color', '#3b3b3b')
        root.style.setProperty('--input-color', '#242424')
        // Change Image
        document.getElementById('titleImg').src="../static/imgs/RolsaTechLogo.png"
    }

}

// Event listener for dark mode button
document.getElementById('darkModeBtn').addEventListener("click", darkModeToggle);


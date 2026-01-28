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

    // Update the CSS variable
    root.style.setProperty('--backgroud-color', '#242424');
    root.style.setProperty('--font-color', '#FFFBF8')
    root.style.setProperty('--table-color', '#3b3b3b')
    root.style.setProperty('--input-color', '#242424')

    // Change Image
    document.getElementById('titleImg').src="../static/imgs/RolsaTechLogo.png"

}

// Event listener for dark mode button
document.getElementById('darkModeBtn').addEventListener("click", darkModeToggle);


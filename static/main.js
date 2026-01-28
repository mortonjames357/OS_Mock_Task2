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
}

// Function to change position of btn when it hover over the footer (get x/y of footer)
function darkModeBtnChange(){

}


// Event listener for dark mode button
document.getElementById('darkModeBtn').addEventListener("click", darkModeToggle);


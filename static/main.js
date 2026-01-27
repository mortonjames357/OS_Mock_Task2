function goToProducts(){
    window.scrollTo(0, 900)
}

function backToTop(e){
    e.preventDefault()
    window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
}
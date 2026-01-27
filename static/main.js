function goToProducts(){
    window.scrollTo(0, 1060)
}

function backToTop(e){
    e.preventDefault()
    window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
}
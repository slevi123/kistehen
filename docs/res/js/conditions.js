
window.onload = function(){
    let agreement = document.getElementById("conditions");
    if (document.cookie=="accepted=true"){
        agreement.style.display = "none";
    } else {
        agreement.children[1].addEventListener("click", ()=>{
            document.cookie="accepted=true";
            agreement.style.display = "none";
        })
    }
}
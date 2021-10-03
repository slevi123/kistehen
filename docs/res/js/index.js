function select_signup(){
    console.log("register")
    document.getElementById("login").style.display = "none";
    document.getElementById("signup").style.display = "";
}

function select_login(){
    console.log("login")
    document.getElementById("login").style.display = "";
    document.getElementById("signup").style.display = "none";
}

// function next_regiszter(){
//     document.getElementById("").style.visibility = "hidden";
//     document.getElementById("register-2").style.visibility = "visible";
// }
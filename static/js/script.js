/*These functions handles removing flash message and x hover effect*/

let exit = document.querySelector("#exit");
let messages = document.querySelector("#messages");

function handleClick(event) {
    event.target.remove();
    messages.remove();
}

function handleMouseover() {
    exit.classList.add("hover-effect");
}

function handleMouseout() {
    exit.classList.remove("hover-effect");
}

exit.addEventListener("click", handleClick);
exit.addEventListener("mouseover", handleMouseover);
exit.addEventListener("mouseout", handleMouseout);
const buttonsSection = document.querySelector(".buttons-section")


eel.expose(move);               // Expose this function to Python
eel.expose(readyToPlay);
function say_hello_js(x) {
    console.log("Hello from " + x);
}


function init_update() {
    eel.init_update()
}


function move(progress) {

    var elem = document.getElementById("progress-bar");
    var width = 1;
    document.getElementById("update-client").disabled = true;
    if (width >= 100) {
        clearInterval(id);
    } else {
        width = progress;
        elem.style.width = width + "%";
    }

}

//disable the download button, enable the play button.
function readyToPlay() {

    document.getElementById("update-client").disabled = true;
    document.getElementById("play").disabled = false;

    console.log("trying to do it")
}
eel.say_hello_py("Javascript butt!");  // Call a Python function
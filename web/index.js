const buttonsSection = document.querySelector(".buttons-section")


eel.expose(say_hello_js);               // Expose this function to Python
function say_hello_js(x) {
    console.log("Hello from " + x);
}


var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("progress-bar");
    var width = 1;
    var id = setInterval(frame, 10);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
        readyToPlay();
      } else {
        width++;
        elem.style.width = width + "%";
      }
    }
  }
}

//disable the download button, enable the play button.
function readyToPlay() {

    document.getElementById("update-client").disabled = true;
    document.getElementById("play").disabled = false;

    console.log("trying to do it")
}
eel.say_hello_py("Javascript butt!");  // Call a Python function
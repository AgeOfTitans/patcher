const buttonsSection = document.querySelector(".buttons-section")


eel.expose(say_hello_js);               // Expose this function to Python
function say_hello_js(x) {
    console.log("Hello from " + x);
}



eel.say_hello_py("Javascript butt!");  // Call a Python function
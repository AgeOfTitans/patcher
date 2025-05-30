const buttonsSection = document.getElementById("buttons-section")
let manifest;
let client_version;
let current_version;
let updateButton = document.getElementById("update-client")

async function loadVersionInfo() {
    manifest = await eel.get_manifest()();
    client_version = await eel.get_version()();
    current_version = await eel.get_current_version(manifest)();

    eel.printf("Latest version.")

    console.log("Latest version:", current_version);

    console.log({ client_version, current_version })
    if (!client_version) {
        console.log("herp")
        return;
    }

    document.getElementById("client-version").innerHTML = client_version
    document.getElementById("current-version").innerHTML = current_version

    if (client_version == current_version){
        readyToPlay();
        return;
    }
    
    document.getElementById("update-client").disabled = false;
    document.getElementById("update-client").innerHTML = `Update`
    
}

loadVersionInfo();

function init_update() {
    eel.init_update(manifest, current_version)
}

/**
 * 
 * @param {int} progress Percent complete.  Should be < 100
 */
function move(progress) {
    var elem = document.getElementById("progress-bar");
    var width = 1;
    updateButton.disabled = true;
    if (width >= 100) {
        clearInterval(id);
    } else {
        width = progress;
        elem.style.width = width + "%";
    }

}

/**
 * Patcher has finished, game is ready to play.
 */
function readyToPlay() {
    updateButton.disabled = true;
    document.getElementById("play").disabled = false;
    updateButton.value = `Up to Date!`
    document.querySelector(".client-version").value = current_version



}



//exports to python
eel.expose(move);
eel.expose(readyToPlay);

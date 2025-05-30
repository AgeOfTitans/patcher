import math
import eel
import os
import sys
import subprocess
from src.update import deltas, download
from src.file import eqemupatcher as file
from packaging import version


@eel.expose
def get_version():
    return file.get_local_version()


@eel.expose
def get_manifest():
    manifest_link = file.get_manifest_link()
    manifest = download.fetch_manifest(manifest_link)
    return manifest


@eel.expose
def get_current_version(manifest):
    versions = manifest.get("versions", [])
    if not versions:
        return "0.0.0"
    sorted_versions = sorted(
        (v.get("version", "0.0.0") for v in versions),
        key=version.parse,
        reverse=True
    )
    return sorted_versions[0]\


@eel.expose
def steam_download():
    # TODO Before release move download folder to be CWD and not ROF2
    script_path = os.path.join("src", "steam_client", "steam_download.py")

    # Wrap the full command in double quotes for `start`, and escape inner quotes correctly
    command = f'python {script_path}'

    subprocess.Popen([
        "cmd.exe", "/c",
        f'start cmd /k {command}'
    ])


@eel.expose
def init_update(manifest, client_version):
    print("beep boop update go brrr")
    eel.move(1)  # Set progress to 1%
    delta_list = deltas.get_deltas(manifest, os.getcwd(), client_version)
    delta_count = len(delta_list)
    progress = 0

    for delta in delta_list:
        src_link, dest_file = download.get_download_link(manifest, delta)
        if download.download(src_link, dest_file):
            progress = progress + 1
            eel.move(math.ceil(100 * progress / delta_count))  # ceil to prevent rounding issues
    file.set_local_version(get_current_version(manifest))
    eel.readyToPlay()


@eel.expose
def printf(message):
    print(message)

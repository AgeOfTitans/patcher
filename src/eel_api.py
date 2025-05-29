import math
import eel
import os
from src.update import deltas, download


@eel.expose  # Expose this function to Javascript
def init_update():
    print("beep boop update go brrr")
    eel.move(1)  # Set progress to 1%
    manifest = deltas.get_remote_manifest()
    delta_list = deltas.get_deltas(manifest, os.getcwd())
    delta_count = len(delta_list)
    progress = 0

    for delta in delta_list:
        src_link, dest_file = download.get_download_link(manifest, delta)
        if download.download(src_link, dest_file):
            progress = progress + 1
            eel.move(math.ceil(100 * progress / delta_count))  # nudge to prevent rounding issues

    eel.readyToPlay()

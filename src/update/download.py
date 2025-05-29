import time
import os
import urllib.parse


def get_download_link(manifest, delta, base_dir=os.getcwd()):
    base_url = manifest['base_url']

    if not base_url.endswith('/'):
        base_url += '/'

    if 'dl=0' in base_url:
        base_url = base_url.replace('dl=0', 'dl=1')

    encoded_path = urllib.parse.quote(delta['path'])
    src_link = base_url + encoded_path
    dest_file = os.path.join(base_dir, delta['path'])

    return src_link, dest_file


def download(src_link, dest_file):
    print(f"Mock downloading from {src_link} to {dest_file}...")
    time.sleep(1)  # 100 ms delay
    return True

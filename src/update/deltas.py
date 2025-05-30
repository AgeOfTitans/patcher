import os, json, hashlib, requests
from packaging.version import Version


DROPBOX_LINK = \
    "https://www.dropbox.com/scl/fi/mapee6h9vfxieyloyrnbp/manifest.json?rlkey=9u48xl49b1ifo5ivo3brrfdw3&st=piznwa1v&dl=1"


def get_remote_manifest():
    r = requests.get(DROPBOX_LINK)
    r.raise_for_status()
    return r.json()


def hash_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def get_deltas(manifest, local_base_dir, current_version="0.0.0"):
    file_map = {}

    # Only apply versions newer than current_version
    for version_entry in manifest['versions']:
        if Version(version_entry['version']) <= Version(current_version):
            continue

        for path, file_entry in version_entry['files'].items():
            if file_entry.get("delete"):
                file_map.pop(path, None)
                local_path = os.path.join(local_base_dir, path)
                if os.path.exists(local_path):
                    try:
                        os.remove(local_path)
                    except Exception as e:
                        print(f"Error deleting {local_path}: {e}")
                continue

            file_map[path] = [path, file_entry]

    out_of_sync_files = []

    for path, entry in file_map.items():
        local_path = os.path.join(local_base_dir, path)

        if not os.path.exists(local_path):
            out_of_sync_files.append(entry)
            continue

        local_hash = hash_file(local_path)
        if local_hash != entry[1]['hash']:
            out_of_sync_files.append(entry)

    return out_of_sync_files

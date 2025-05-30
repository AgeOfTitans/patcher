import time
import os
import urllib.parse
import requests
import json
import zipfile
import io


def fetch_manifest(manifest_link):
    if not isinstance(manifest_link, str) or "dropbox.com" not in manifest_link:
        raise ValueError("Invalid manifest_link: expected a Dropbox URL.")

    # Normalize the Dropbox link to ensure it ends with '?raw=1'
    if "?dl=0" in manifest_link:
        manifest_link = manifest_link.replace("?dl=0", "?raw=1")
    elif "?dl=1" in manifest_link:
        manifest_link = manifest_link.replace("?dl=1", "?raw=1")
    elif "?raw=1" not in manifest_link:
        if "?" in manifest_link:
            manifest_link += "&raw=1"
        else:
            manifest_link += "?raw=1"

    try:
        response = requests.get(manifest_link)
        response.raise_for_status()
        # Check if it's a zip file (starts with "PK")
        if response.content[:2] == b'PK':
            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                # Look for a .json file inside
                json_files = [name for name in z.namelist() if name.endswith('.json')]
                if not json_files:
                    raise ValueError("ZIP archive does not contain a .json file.")

                with z.open(json_files[0]) as manifest_file:
                    return json.load(manifest_file)

        # If not ZIP, try to parse raw response
        return json.loads(response.text)
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to fetch manifest: {e}")
    except json.JSONDecodeError:
        raise ValueError("Manifest is not valid JSON.")


def get_download_link(manifest, delta, base_dir=os.getcwd()):
    base_url = manifest['base_url']

    if not base_url.endswith('/'):
        base_url += '/'

    if 'dl=0' in base_url:
        base_url = base_url.replace('dl=0', 'dl=1')

    encoded_path = urllib.parse.quote(delta[0])
    src_link = base_url + encoded_path
    dest_file = os.path.join(base_dir, delta[0])

    return src_link, dest_file


def download(src_link, dest_file, timeout=30):
    if not src_link.lower().startswith(("http://", "https://")):
        raise ValueError(f"Invalid source link: {src_link}")

    try:
        # Ensure destination directory exists
        os.makedirs(os.path.dirname(dest_file), exist_ok=True)

        print(f"Downloading from {src_link} to {dest_file}...")
        with requests.get(src_link, stream=True, timeout=timeout) as response:
            response.raise_for_status()
            with open(dest_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

        print(f"Downloaded {dest_file} successfully.")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")
        return False
    except OSError as e:
        print(f"File write error: {e}")
        return False

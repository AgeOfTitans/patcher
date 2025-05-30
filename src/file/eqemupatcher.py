import configparser
import os
import json
import requests


def set_local_version(version, ini_path="eqemupatcher.ini"):
    config = configparser.ConfigParser()

    # Read existing file if it exists
    if os.path.exists(ini_path):
        config.read(ini_path)

    # Ensure DEFAULT section exists
    if "DEFAULT" not in config:
        config["DEFAULT"] = {}

    # Set version
    config["DEFAULT"]["version"] = version

    # Write back to the file
    with open(ini_path, "w") as configfile:
        config.write(configfile)

    print(f"✅ Version set to {version} in {ini_path}")


def get_local_version(ini_path="eqemupatcher.ini"):
    if not os.path.exists(ini_path):
        raise FileNotFoundError(f"Expected {ini_path} but it does not exist.")

    config = configparser.ConfigParser()
    config.read(ini_path)

    if not config.has_option("DEFAULT", "version"):
        raise KeyError("Missing 'version' in eqemupatcher.ini.")

    return config.get("DEFAULT", "version")


def get_manifest_link(ini_path="eqemupatcher.ini"):
    if not os.path.exists(ini_path):
        raise FileNotFoundError(f"Expected {ini_path} but it does not exist.")

    config = configparser.ConfigParser()
    config.read(ini_path)

    if not config.has_option("DEFAULT", "manifest_link"):
        raise KeyError("Missing 'manifest_link' in eqemupatcher.ini.")

    return config.get("DEFAULT", "manifest_link")

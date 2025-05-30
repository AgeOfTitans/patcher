import configparser
import os
import json
import requests


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

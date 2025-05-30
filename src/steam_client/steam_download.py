import os
import subprocess
import sys


def check_steamctl():
    try:
        subprocess.run(["steamctl", "--version"], check=True)
        print("✅ steamctl is already installed.")
        return True
    except FileNotFoundError:
        print("\n⚠️  steamctl is required to securely download game files from Steam.")
        print("It uses official Steam login and supports Steam Guard verification.")
        print("More info: https://github.com/ValvePython/steamctl\n")
        consent = input("Would you like to install steamctl now via pip? (Y/n): ").strip().lower()
        if consent in ("", "y", "yes"):
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "steamctl"])
                print("✅ steamctl installed successfully.")
                return True
            except subprocess.CalledProcessError:
                print("❌ Failed to install steamctl. Please install it manually and try again.")
                return False
        else:
            print("❌ Cannot continue without steamctl.")
            return False


def download_steam_depot(app_id, depot_id, manifest_id=None, output_dir="./ROF2"):
    command = f'steamctl depot download --app {app_id} --depot {depot_id} -o "{output_dir}"'
    if manifest_id:
        command += f" --manifest {manifest_id}"
        # print(command)

    subprocess.run(command, check=True)


if __name__ == '__main__':
    good_to_go = check_steamctl()
    if good_to_go:
        download_steam_depot(app_id=205710, depot_id=205711, manifest_id="1926608638440811669")
    exit(0)

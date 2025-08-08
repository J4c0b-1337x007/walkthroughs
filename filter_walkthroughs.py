import os
import shutil
import argparse

# רשימת מכונות OffSec
offsec_machines = {
    "ClamAV", "Pelican", "Payday", "Snookums", "Bratarina", "Pebbles", "Nibbles", "Hetemit",
    "ZenPhoto", "Nukem", "Cockpit", "Clue", "Extplorer", "Postfish", "Hawat", "Walla", "Apex",
    "Sorcerer", "Sybaris", "Peppo", "Hunit", "Readys", "Astronaut", "Bullybox", "Marketing",
    "Exfiltrated", "Fanatastic", "QuackerJack", "Wombo", "Flu", "Roquefort", "Levram", "Mzeeav",
    "LaVita", "Xposedapi", "Zipper", "Fired", "Scrutiny", "SPX", "Vmdak", "Mantis", "BitForge",
    "WallpaperHub", "Zab", "SpiderSociety", "Kevin", "Internal", "Algernon", "Jacko", "Craft",
    "Squid", "Nickel", "MedJed", "Billyboss", "Shenzi", "AuthBy", "Slort", "Hepet", "DVR4",
    "Mice", "Monster", "Fish", "Compromised"
}

folders = ["linux", "windows"]
output_folder = "private_machines"

parser = argparse.ArgumentParser(description="Filter and optionally delete OffSec walkthroughs")
parser.add_argument("--delete", action="store_true", help="Delete the OffSec walkthroughs from original folders")
args = parser.parse_args()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith(".md"):
            machine_name = os.path.splitext(filename)[0].strip()
            if machine_name in offsec_machines:
                src = os.path.join(folder, filename)
                dst = os.path.join(output_folder, filename)
                shutil.copy2(src, dst)
                print(f"[+] Copied: {filename} → {output_folder}/")

                if args.delete:
                    os.remove(src)
                    print(f"[x] Deleted from original: {filename}")

if args.delete:
    print("\n🧹 Cleanup complete! OffSec machines removed from linux/ and windows/")
else:
    print("\n✅ Done. Files copied — nothing deleted.")
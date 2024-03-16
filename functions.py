import os

def get_paths():
    print("\n")
    downloadFolderPath = input("Download folder path: ")
    print("\n")
    if downloadFolderPath == "":
        downloadFolderPath = r"C:\Users\datha\Downloads"  # Use raw string literal

    modsPath = input("MC mod folder path: ")
    print("\n")
    if modsPath == "":
        modsPath = r"C:\Users\datha\AppData\Roaming\.minecraft\mods"  # Use raw string literal
    return downloadFolderPath, modsPath

def extract_mods(downloadFolderFiles,downloadFolderPath):
    mods = []
    for file in downloadFolderFiles:
        print(f"Looking at file '{file}'\n")
        if file.endswith(".jar"):
            mods.append(os.path.join(downloadFolderPath, file))  # Construct file path
            print(f"Added file '{file}' to mods list\n")
        print(f'Found mods: {mods}\n')
    return mods

def move_mods(mods,modsPath):
    for mod in mods:
        os.replace(mod, os.path.join(modsPath, os.path.basename(mod)))
        print(f"Moved mod '{os.path.basename(mod)}'\n")  
import os

def get_paths():
    print("\n")
    downloadFolderPath = input("Download folder path(click enter if creator): ")
    print("\n")
    if downloadFolderPath == "":
        downloadFolderPath = r"C:\Users\datha\Downloads"  # Use raw string literal

    modsPath = input("MC mod folder path(click enter if creator): ")
    print("\n")
    if modsPath == "":
        modsPath = r"C:\Users\datha\AppData\Roaming\.minecraft\mods"  # Use raw string literal
    return downloadFolderPath, modsPath

def extract_mods(downloadFolderFiles,downloadFolderPath):
    mods = []
    modNames = []
    for file in downloadFolderFiles:
        print(f"Looking at file '{file}' to see if it's a mod" )
        if file.endswith(".jar"):
            mods.append(os.path.join(downloadFolderPath, file))  # Construct file path
            modNames.append(file.strip(".jar"))
    if mods == []:
        print("No mods found\n")
    else:
        print(f'Found mods: {modNames}\n')
    return mods

def move_mods(mods,modsPath):
    for mod in mods:
        os.replace(mod, os.path.join(modsPath, os.path.basename(mod)))
        print(f"Moved mod '{os.path.basename(mod)}'\n")  
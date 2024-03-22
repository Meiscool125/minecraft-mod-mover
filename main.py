from functions import *
downloadFolderPath, modsPath = get_paths()
downloadFolderFiles = os.listdir(downloadFolderPath)
mods = extract_mods(downloadFolderFiles,downloadFolderPath)
if mods != []:
    move_mods(mods,modsPath)
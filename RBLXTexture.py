import os

#Paths
Textures=os.path.dirname(__file__)+"\\Tx\\*.*"
Path=os.path.expanduser("~")+"\\AppData\\Local\\Roblox\\Versions\\"
print(Path)

Versions=[]
RBLXPlrDir=""

#Get an array of all roblox directories/files in the Path.
RobloxDir=os.listdir(Path)

#Loop through the array & add the ones with "version" at the start to another array.
for x in RobloxDir:
    if x[:7]=="version":
        Versions.append(x)

#Loop through the "version" directory array & find the folder with "RobloxPlayerBeta.exe" in it.
for x in Versions:
    if os.path.exists(Path+x+"\\RobloxPlayerBeta.exe"):
        RBLXPlrDir=x #Store this directory.

if RBLXPlrDir=="":
    print("Roblox Player Directory not found.\nCould not replace textures.")
else:
    print("Roblox Player Directory found.\n[ " + RBLXPlrDir + " ]\n\nReplacing textures...")
    #Copy & overwrite Roblox textures with my own with a Windows terminal command.
    os.system("xcopy " + '"' + Textures + '" "'+ Path+RBLXPlrDir + '" /E /Y')
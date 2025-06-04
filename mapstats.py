import os

def setgamepath():
    tfpaths=["D:\\SteamLibrary\\steamapps\\common\\Team Fortress 2","C:\\Program Files (x86)\\Steam\\steamapps\\common\\Team Fortress 2"]
    path=""
    for tfpath in tfpaths:
        if os.path.exists(tfpath):
            if input("is this the correct game directory: "+tfpath+" (Y/N)\n").lower()=="y":
                path=tfpath
    if path=="":
        path = input("TF2 directory not found. Please enter your tf2 install directory. \nexample: C:\\Program Files (x86)\\Steam\\steamapps\\common\\Team Fortress 2 \n")
        if os.path.exists(path):
            print("directory found succesfully")
        else:
            print("directory not found")
            input("press enter to exit program")
            exit()
    if os.path.exists(path):
        with open("gamepath.txt","w") as file:
            file.write(path)

if os.path.exists("gamepath.txt"):
    with open("gamepath.txt","r") as file:
        path=file.readline()
        #print(path)
else:
    setgamepath()

def readfile():
    global maps,viewedamounts
    respath=path+"//tf//media//viewed.res"
    with open(respath,"r") as file:
        lines = file.readlines()
    lines = [line.strip('",\n,"\t"') for line in lines]
    for line in lines:
        if line=="{"or line=="}":
            lines.remove(line)
    del lines[0],lines[-1]
    maps=[]
    lines = [line.removeprefix('viewed"\t\t"') for line in lines]
    viewedamounts=[]
    for line in lines:
        if line.isdigit():
            viewedamounts.append(line)
        else:
            maps.append(line)
    #print(viewedamounts,maps)

if os.path.exists(path+"//tf//media//viewed.res"):
    print("viewed.res file found! loading map data...")
    readfile()
    print("\nMap Data:")
    gamemodes=[]
    for i in range(len(maps)):
        print(maps[i]+":  "+viewedamounts[i])
        gamemodes.append(maps[i].split("_")[0])
    counts=[]
    for gamemode in list(dict.fromkeys(gamemodes)):
        counts.append(gamemodes.count(gamemode))
    gamemodes = list(dict.fromkeys(gamemodes))
    print("\nGamemode Data:")
    for i in range(len(counts)):
        print(gamemodes[i]+":    "+str(counts[i]))
    viewedamounts=[int(viewedamount) for viewedamount in viewedamounts]
    print("\nStatistics:")
    print("Your most played map is "+maps[viewedamounts.index(max(viewedamounts))]+", which you played "+str((sum(viewedamounts)/(max(viewedamounts))))+"% of the time.")
    print("Your most played gamemode is "+gamemodes[counts.index(max(counts))]+", which you played "+str((sum(counts)/(max(counts))))+"% of the time.")
    input("")
else:
    if input("viewed.res file not found. would you like to change your game directory").lower()=="y":
        setgamepath()
    else:
        input("make sure you have the file in your installation of TF2. press enter to exit the program")
        exit()
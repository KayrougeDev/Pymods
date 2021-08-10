import pathlib

class Mod:
    def __init__(self, gameName, newTexture, modName):
        self.gameName = gameName
        self.modDir = pathlib.Path()
        self.modName = modName
        self.modDir = self.modDir / "mods"
        self.modDir.mkdir(parents=True, exist_ok=True)
        self.newTexture = self.get_mod_foler() / newTexture
        with open(self.modDir / "pymods-info.txt", "w") as file:
            file.write("Pymods Info\n")
            file.write("Version: 1.0.0\n")
            file.write("Author: Terminal Software\n")
            file.write("Game: {}\n".format(gameName))
            file.close()

    def get_mod_foler(self):
        return self.modDir / self.modName

    def get_mod_new_texture(self):
        return self.newTexture

    def get_name(self):
        return self.modName





class ModLoader:
    def set_mod_to_load(self, mod):
        self.mod = mod

    def get_mod_to_load(self):
        return self.mod

    def load(self, loadEvent):
        print("Load {} mod".format(self.mod.get_name()))
        loadEvent()
        print("{} finish loaded".format(self.mod.get_name()))

from mods import Mod, ModLoader


theMod = Mod("test", "tt", "testmod")

print(theMod.get_mod_foler())
print()
print(theMod.get_mod_new_texture())
print()
print(theMod.get_name())
print()
print()
print()

def test():
    print("salut mon pote")

modLoader = ModLoader()

modLoader.set_mod_to_load(theMod)

modLoader.load(test)

import fontforge
import os

F = fontforge.open("src/data/fonts/SIXTY.TTF")
save_path = "src/data/files/dataset/"
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
for name in F:
    if name not in characters:
        continue
    # Check if a folder with the character name exists
    if not os.path.exists(save_path + name):
        os.makedirs(save_path + name)
    filename = name + ".png"
    save_path = save_path + filename

    F[name].export(filename)

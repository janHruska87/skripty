# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import img2pdf
import pathlib

def start(basePath):
    if pathlib.Path(base_path).exists():
        print("Soubor/Cesta existuje...")
        files = os.listdir(basePath)
        printAllFiles(files)
    else:
        print("Cesta, nebo soubor neexistuje...")


def printAllFiles(files):
    images = list()
    for file in files:
        if file.endswith("jpg"):
            images.append(base_path + file)
            print("Nacten soubor: " + base_path + file)

    with open(base_path + "output.pdf",mode="w",encoding="utf-8") as f:
        f.write(img2pdf.convert(images))
        print("Zapisuji soubor:" + base_path + "output.pdf")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_path = "C:\\Users\\janhr\\OneDrive\\Plocha\\PDF z obrazku\\"
    start(base_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

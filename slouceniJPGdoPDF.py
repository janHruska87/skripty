# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import img2pdf
import pathlib



def start(basePath):
    images = [os.path.join(basePath, f) for f in os.listdir(basePath) if f.endswith('.jpg')]
    printAllFiles(images)


def printAllFiles(images):
    with open(base_path + "output.pdf",mode="wb") as f:
        f.write(img2pdf.convert(images))
        print("Zapisuji soubor:" + base_path + "output.pdf")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_path = "C:\\Users\\janhr\\OneDrive\\Plocha\\PDF z obrazku\\"
    start(base_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

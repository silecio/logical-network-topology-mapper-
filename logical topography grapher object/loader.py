##Loader
from yaml import *
from tkinter import *
from tkinter import filedialog


def loader():
    Data = filedialog.askopenfiles(mode = 'r', initialdir = "\Test_multifile_script\logical topography grapher object\data")
    x = Data[0]
    b = x.read()
    print(b)



from doctest import DocFileTest
import win32clipboard as clipboard
from tkinter import filedialog
import numpy as np
import pandas as pd

def toClipboardForExcel(array):
    """
    Copies an array into a string format acceptable by Excel.
    Columns separated by \t, rows separated by \n
    """
    # Borrowed from https://stackoverflow.com/a/22488567. Works only in Windows.
    # Create string from array. 
    line_strings = []
    for line in array:
        line_strings.append("\t".join(line.astype(str)).replace("\n",""))
    array_string = "\r\n".join(line_strings)

    # Put string into clipboard (open, clear, set, close)
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardText(array_string)
    clipboard.CloseClipboard()

file_path = filedialog.askopenfilename()

df = pd.read_csv(file_path)  


intensity_background = df[['Intensity_MeanIntensity_Masked_Background_w_Islet']]
intensity_islet = df[['Intensity_MeanIntensity_Masked_Islet']]

background_mean = intensity_background.mean(axis=0)
background_std = intensity_background.std(axis=0)
islet_mean = intensity_islet.mean(axis=0)
islet_std = intensity_islet.std(axis=0)

print(f'Background: {background_mean} {background_std} Islet: {islet_mean} {islet_std}')
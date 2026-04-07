import tkinter as tk
import tkinter.messagebox
from tkinter import simpledialog
import os
import re

n = 0
text = ''
def start():
    answer = simpledialog.askinteger("", "input the already exist cfg(named ch{i} {i}=1,2,...) number：")
    global n
    n = int(answer)
    cfgRename()

def wetherContinue():
    wetherCon = tkinter.messagebox.askyesno('',message='Continue input more crosshaircode?')
    if wetherCon == False:
        autoexec()
    return wetherCon

def autoexec():
    global text
    text = "copy following texts to autoexec.cfg\n\n\nalias switchCrosshair ch1"
    for i in range(1,n):
        text += f"alias ch{i} 'exec ch{i};alias switchCrosshair ch{i+1}"
    text += f"alias ch{n} 'exec ch{n};alias switchCrosshair ch1"
    text += "bind 8 switchCrosshair"
    autoexecFile = tkinter.messagebox.showinfo('autoexec',text)

def cfgRename():
    global n
    n += 1
    code = simpledialog.askstring('CS2 crosshaircode',show=None,prompt='Please input CS2 crosshaircode:')
    cfg(code)
    try:
        outputName = "ch" + str(n) + ".cfg"
        os.rename("output.cfg", outputName)
    except Exception as error:
        tkinter.messagebox.showerror("Error", error)
    while wetherContinue():
        n += 1
        code = simpledialog.askstring('CS2 crosshaircode',show=None,prompt='Please input CS2 crosshaircode:')
        cfg(code)
        try:
            outputName = "ch" + str(n) + ".cfg"
            os.rename("output.cfg", outputName)
        except Exception as error:
            tkinter.messagebox.showerror("Error", error)

DICTIONARY = "ABCDEFGHJKLMNOPQRSTUVWXYZabcdefhijkmnopqrstuvwxyz23456789"

def decodeCrosshair(code):
    crosshairCode = re.compile(r'^CSGO(-[\w]{5}){5}$')
    mo = crosshairCode.search(code)
    if mo is None:
        tkinter.messagebox.showerror("Invalid crosshair code", "Please input crosshair code again")
    crosshairCode = mo.group()[4:].replace("-", "")

    big = 0
    for c in reversed(crosshairCode):
        big = big * len(DICTIONARY) + DICTIONARY.index(c)
    all_bytes = big.to_bytes((big.bit_length() + 7) // 8, 'little')
    if len(all_bytes) == 18:
        all_bytes += b'\x00'
    decoded = all_bytes[::-1][:18]
    return decoded

class CrosshairInfo:
    def __init__(self, bytes_data: bytes):
        self.style = (bytes_data[14] & 0xF) >> 1
        self.has_center_dot = bool((bytes_data[14] >> 4) & 1)
        self.length = bytes_data[15] / 10.0
        self.thickness = bytes_data[13] / 10.0
        self.gap = (int.from_bytes([bytes_data[3]], 'big', signed=True)) / 10.0
        self.has_outline = bool(bytes_data[11] & 8)
        self.outline = bytes_data[4] / 2.0
        self.red = bytes_data[5]
        self.green = bytes_data[6]
        self.blue = bytes_data[7]
        self.has_alpha = bool((bytes_data[14] >> 4) & 4)
        self.alpha = bytes_data[8]
        self.split_distance = bytes_data[9]
        self.inner_split_alpha = (bytes_data[11] >> 4) / 10.0
        self.outer_split_alpha = (bytes_data[12] & 0xF) / 10.0
        self.split_size_ratio = (bytes_data[12] >> 4) / 10.0
        self.is_t_style = bool((bytes_data[14] >> 4) & 8)

    def toConsoleCommands(self) :
        lines = [
            "cl_crosshairusealpha 1",
            f"cl_crosshairthickness {self.thickness:.6f}",
            f"cl_crosshairstyle {self.style}",
            f"cl_crosshairsize {self.length:.6f}",
            "cl_crosshairgap_useweaponvalue false",
            f"cl_crosshairgap {self.gap:.6f}",
            f"cl_crosshairdot {'true' if self.has_center_dot else 'false'}",
            f"cl_crosshaircolor_r {self.red}",
            f"cl_crosshaircolor_g {self.green}",
            f"cl_crosshaircolor_b {self.blue}",
            "cl_crosshaircolor 5",
            f"cl_crosshairalpha {self.alpha}",
            "cl_crosshair_recoil false",
            f"cl_crosshair_outlinethickness {self.outline:.6f}",
            "cl_crosshair_friendly_warning 1",
            f"cl_crosshair_dynamic_splitdist {self.split_distance}",
            f"cl_crosshair_dynamic_splitalpha_outermod {self.outer_split_alpha:.6f}",
            f"cl_crosshair_dynamic_splitalpha_innermod {self.inner_split_alpha:.6f}",
            f"cl_crosshair_dynamic_maxdist_splitratio {self.split_size_ratio:.6f}",
            f"cl_crosshair_drawoutline {'true' if self.has_outline else 'false'}",
            f"cl_crosshair_t {'true' if self.is_t_style else 'false'}",
        ]
        return "\n".join(lines)


def cfg(crosshairCodeInput):
    try:
        code = decodeCrosshair(crosshairCodeInput)
        info = CrosshairInfo(code)
        with open("output.cfg", "w") as f:
            f.write(info.toConsoleCommands())
    except Exception as error:
        tkinter.messagebox.showerror("Invalid crosshair code", "Please input crosshair code again")

window = tk.Tk()
window.geometry('500x300')
window.title('SwichCrosshair')
textIn = tk.Label(window,text='About This:\n'
                              ' It allows player switch their CS2 sharing crosshair into cfg file, \n'
                              'which can be use to swtich crosshair in match. Generate code in autoexec.cfg',width=100,height=3,)
textIn.pack()
startButton = tk.Button(window,text='Start',command=start,width=10,bg='black',fg='white',activebackground='white')
startButton.pack()
window.mainloop()

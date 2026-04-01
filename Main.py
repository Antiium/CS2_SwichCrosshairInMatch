import re
import os
crosshairCodeInput = input("Please input crosshair code: ")
DICTIONARY = "ABCDEFGHJKLMNOPQRSTUVWXYZabcdefhijkmnopqrstuvwxyz23456789"

def decodeCrosshair(code):
    crosshairCode = re.compile(r'^CSGO(-[\w]{5}){5}$')
    mo = crosshairCode.search(code)
    if mo is None:
        print("Invalid crosshair code\nplz input crosshair code again")
        raise ValueError("Invalid crosshair code")
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

try:
    code = decodeCrosshair(crosshairCodeInput)
    info = CrosshairInfo(code)
    print(info.toConsoleCommands())
    with open("output.cfg", "w") as f:
        f.write(info.toConsoleCommands())
except Exception as error:
    print(f"解析失败: {error}")
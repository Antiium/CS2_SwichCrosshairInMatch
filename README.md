English | [中文](README_CN.md)



# CS2 Switch Crosshair In Match

This project can convert CS2 crosshair sharing codes into cfg files that can be used to change the crosshair in-game.

## How it works
It will first decode the cs2 crosshair sharing code. Then, an cfg file is generated, which contains crosshair-related data that the game can recognize.
After enter multiple CS2 crosshair codes. The code will output multiple cfg files containing crosshair information. After the player enters the last crosshair code, a piece of code will be generated for the player to write into the autoexec.cfg file, enabling the function of automatically switching crosshairs with a single key press in the game.

## Support Inviorment

Windows - u can directly run  SwitchCrosshair.exe file

linux & macOS directly run main.py

## How to use it

### For Windows

1. Downlode latest releases
2. Put SwitchCrosshair.exe into a floader
3. Run SwitchCrosshair.exe
4. Follow the requirement
5. Move the generated .cfg file in the folder to the location of the autoexec.cfg file

   (Detailed path instructions are provided below)
7. Paste the text it asked u to copy to autoexec.cfg

### For linux & macOS

1. Downlode **main.py** and **cfgGenerater.py**
2. Run **main.py**
3. Follow the requirement
4. Move the generated .cfg file in the folder to the location of the autoexec.cfg file

   (Detailed path instructions are provided below)
5. Paste the text it asked u to copy to autoexec.cfg

### The Path of autoexec.cfg

    \steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg\autoexec.cfg
    
  you can find it through steam: library-cs2-manage-brose local files

  Ps. if autoexec doesn't exist, just create it

<img width="652" height="481" alt="image" src="https://github.com/user-attachments/assets/30c4cde4-fc2e-4a81-b850-aad79cd14cd3" />


[English](README.md) | 中文

# CS2 游戏内一键更换准星

该项目可以将 CS2 准星共享代码转换为 cfg 文件，进而可以在游戏中一键更改准星。

## 工作原理

它首先会解码 CS2 准星共享代码。然后生成一个包含游戏可识别的准星相关数据的 cfg 文件。在输入多个 CS2 准星代码后，代码会输出多个包含准星信息的 cfg 文件。玩家输入最后一个准星代码后，会生成一段代码供玩家写入 autoexec.cfg 文件，从而启用游戏中一键自动切换准星的功能。

## 支持环境

Windows-直接运行 SwitchCrosshair.exe 文件

Linux 和 macOS 直接运行 main.py

## 如何使用
### Windows
1. 下载最新版本
2. 将 SwitchCrosshair.exe 放倒一个文件夹中
3. 运行 SwitchCrosshair.exe
4. 遵循弹窗要求操作
5. 将文件夹中生成的 .cfg 文件放倒 autoexec.cfg 所在的文件夹中

   （这个文件夹的具体文件详见下文）
7. 将生成的要求复制的文本复制到 autoexec.cfg 文件中

### linux & macOS
1. 下载 main.py and cfgGenerater.py
2. 运行 main.py
3. 遵照弹窗要求操作
4. 将文件夹中生成的 .cfg 文件放倒 autoexec.cfg 所在的文件夹中

   （这个文件夹的具体文件详见下文）
5. 将生成的要求复制的文本复制到 autoexec.cfg 文件中

### autoexec.cfg 的路径
  \steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg\autoexec.cfg   

您可以通过 Steam 找到它：库-cs2-属性-打开本地文件）

Ps. 如果 autoexec 不存在，则创建它


<img width="652" height="481" alt="image" src="https://github.com/user-attachments/assets/30c4cde4-fc2e-4a81-b850-aad79cd14cd3" />

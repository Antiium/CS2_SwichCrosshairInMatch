# CS2 游戏内一键更换准星

该项目可以将 CS2 准星共享代码转换为 cfg 文件，进而可以在游戏中一键更改准星。

## 工作原理

它首先会解码 CS2 准星共享代码。然后生成一个包含游戏可识别的准星相关数据的 cfg 文件。在输入多个 CS2 准星代码后，代码会输出多个包含准星信息的 cfg 文件。玩家输入最后一个准星代码后，会生成一段代码供玩家写入 autoexec.cfg 文件，从而启用游戏中一键自动切换准星的功能。

## 环境要求

python3

## 如何使用

1. 将这两个文件放到一个文件夹中
2. 打开 main.py
3. 遵照请求
4. 输入 CS 十字准星代码
5. 复制它要求你复制的内容
6. 将其粘贴到 autoexec.cfg 文件中

  (**\steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg\autoexec.cfg** 

您可以通过 Steam 找到它：库-cs2-属性-打开本地文件）

<img width="652" height="481" alt="image" src="https://github.com/user-attachments/assets/30c4cde4-fc2e-4a81-b850-aad79cd14cd3" />

[如果 autoexec 不存在，则创建它]

7. 将这些 ch{i} 复制到同一文件夹

XD
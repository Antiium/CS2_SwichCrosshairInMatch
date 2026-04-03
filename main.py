import cfgGenerater as cfg
import os
print("input the already exist cfg(named ch{i} {i}=1,2,...) number:")
n = int(input())
m = "2"
while m == "2":
    n += 1
    cfg.cfg()
    try:
        outputName = "ch" + str(n) + ".cfg"
        os.rename("output.cfg", outputName)
    except Exception as error:
        print(f"error: {error}")
    m = input(print("If that's all press[1],else press[2]"))
def autoexec():
    print("copy following texts to autoexec.cfg\n\n\n")
    print("alias switchCrosshair ch1")
    for i in range(1,n):
        print(f"alias ch{i} 'exec ch{i};alias switchCrosshair ch{i+1}",)
    print(f"alias ch{n} 'exec ch{n};alias switchCrosshair ch1")
    print("bind 8 switchCrosshair")
autoexec()
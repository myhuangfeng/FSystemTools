import os
from pathlib import Path
from time import sleep

systemlist = """
欢迎使用 FSystemTools 系统工具!

(1) 挂载映像到系统
(2) 删除已挂载或已释放的映像
(3) 释放映像到系统
(4) 转换 WIM 为 ESD
(5) 扩展功能: 强制删除文件
(6) 转换 ESD 为 WIM
(7) 查看系统信息
"""

os.system("cls")
os.system("color 17")
start_if = True

while start_if:
    print(systemlist)
    userinput = int(input("请选择序号:"))

    if(userinput == 1):
        os.system("cls")
        userinput_mount = input("选择要挂载的映像文件:")
        os.system(f"dism /get-wiminfo /wimfile:\"{userinput_mount}\"")
        userinput_mount2 = input("请选择索引号:")
        userinput_mount3 = input("请选择输出路径:")
        os.system(f"dism /mount-wim /wimfile:\"{userinput_mount}\" /index:{userinput_mount2} /mountdir:\"{userinput_mount3}\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***成功!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31m如果出现错误，请自行查找原因。\033[0m")
        os.system("pause")

    elif(userinput == 2):
        os.system("cls")
        userinput_delete = input("输入要删除的已释放或已挂载映像目录:")
        os.system(f"dism /unmount-wim /mountdir:\"{userinput_delete}\" /discard")
        delete_if = input("是否已卸载？如果未卸载，请按回车继续；否则按E退出:")
        if(delete_if == 'E' or delete_if == 'e'):
            print("\033[32m**********\033[0m")
            print("\033[32m***成功!***\033[0m")
            print("\033[32m**********\033[0m")
            print("\033[31m如果出现错误，请自行查找原因。\033[0m")
            os.system("pause")
            exit()
        userinput_formet = input("是否格式化？N的话启动强制删除（不推荐）(Y/N)：")
        if(userinput_formet == 'Y' or userinput_formet == 'y'):
            userinput_formatinput = input("输入指定要格式化的分区(如：D盘输入D而不是D:)：")
            os.system(f"powershell Format-Volume -DriveLetter {userinput_formatinput} -FileSystem NTFS -Force -Confirm:$false")
            print("\033[32m**********\033[0m")
            print("\033[32m***成功!***\033[0m")
            print("\033[32m**********\033[0m")
            os.system("pause")
        else:
            input("请稍等，确认后请按回车键继续。")
            os.system(f"takeown /f \"{userinput_delete}\" /r /d y && icacls \"{userinput_delete}\" /grant administrators:F /t")
            os.system(f"rd /s /q \"{userinput_delete}\"")
            print("\033[32m**********\033[0m")
            print("\033[32m***成功!***\033[0m")
            print("\033[32m**********\033[0m")
            print("\033[31m如果出现错误，请自行查找原因。\033[0m")
            os.system("pause")

    elif(userinput == 3):
        os.system("cls")
        userinput_release = input("请输入要释放的映像文件路径:")
        os.system(f"dism /get-wiminfo /wimfile:\"{userinput_release}\"")
        userinput_release2 = input("请选择索引号:")
        userinput_release3 = input("请选择输出路径:")
        os.system(f"dism /apply-image /imagefile:\"{userinput_release}\" /index:{userinput_release2} /applydir:\"{userinput_release3}\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***成功!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31m如果出现错误，请自行查找原因。\033[0m")
        os.system("pause")

    elif(userinput == 4):
        os.system("cls")
        userinput_wte = input("请输入要转换的文件路径:")
        sleep(5)
        path = Path(userinput_wte)
        new_path = path.with_suffix(".esd")
        path.rename(new_path)
        print("\033[32m**********\033[0m")
        print("\033[32m***成功!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31m如果出现错误，请自行查找原因。\033[0m")
        os.system("pause")

    elif(userinput == 5):
        os.system("cls")
        userinput_del = input("要强制删除的文件夹或文件路径(如：G:\\Users ):")
        input("请稍等，完成后请按回车键继续。")
        os.system(f"takeown /f \"{userinput_del}\" /r /d y && icacls \"{userinput_del}\" /grant administrators:F /t")
        os.system(f"rd /s /q \"{userinput_del}\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***成功!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31m如果出现错误，请自行查找原因。\033[0m")
        os.system("pause")
    
    elif(userinput == 6):
        os.system("cls")
        userinput_etw = input("请输入要转换的文件路径:")
        sleep(5)
        path2 = Path(userinput_etw)
        new_path2 = path2.with_suffix(".wim")
        path2.rename(new_path2)
        print("\033[32m**********\033[0m")
        print("\033[32m***成功!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31m如果出现错误，请自行查找原因。\033[0m")
        os.system("pause")

    elif(userinput == 7):
        os.system("cls")
        os.system("systeminfo")
        print("\033[32m**********\033[0m")
        print("\033[32m***成功!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31m如果出现错误，请自行查找原因。\033[0m")
        os.system("pause")

    os.system("cls")
    os.system("color 17")
    too_start = input("返回主菜单(z) / 退出(e):")
    if(too_start == "z" or too_start == "Z"):
        os.system("cls")
        os.system("color 17")
        start_if = True
    else:
        start_if = False
import os
from pathlib import Path
from time import sleep

systemlist = """
Welcome To FSystemTools!

(1) Mount Image To System.
(2) Delete the mounted or released image.
(3) Release Image To System.
(4) Convert WIM to ESD.
(5) Extension: Force Delete File.
(6) Convert ESD to WIM.
(7) View System Information.
"""

os.system("cls")
os.system("color 17")
start_if = True

while start_if:
    print(systemlist)
    userinput = int(input("Select serial number:"))

    if(userinput == 1):
        os.system("cls")
        userinput_mount = input("Select image file to mount:")
        os.system(f"dism /get-wiminfo /wimfile:\"{userinput_mount}\"")
        userinput_mount2 = input("Please select an index:")
        userinput_mount3 = input("Please select the output path:")
        os.system(f"dism /mount-wim /wimfile:\"{userinput_mount}\" /index:{userinput_mount2} /mountdir:\"{userinput_mount3}\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there is an error, please find out the reason yourself.\033[0m")
        os.system("pause")

    elif(userinput == 2):
        os.system("cls")
        userinput_delete = input("Delete the released or mounted image directory:")
        os.system(f"dism /unmount-wim /mountdir:\"{userinput_delete}\" /discard")
        delete_if = input("Has it been uninstalled? If not, press Enter; otherwise, press E to exit:")
        if(delete_if == 'E' or delete_if == 'e'):
            print("\033[32m**********\033[0m")
            print("\033[32m***win!***\033[0m")
            print("\033[32m**********\033[0m")
            print("\033[31mIf there is an error, please find out the reason yourself.\033[0m")
            os.system("pause")
            exit()
        input("Please wait a moment. You may, please press the Enter key.")
        os.system(f"takeown /f \"{userinput_delete}\" /r /d y && icacls \"{userinput_delete}\" /grant administrators:F /t")
        os.system(f"rd /s /q \"{userinput_delete}\\*.*\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there is an error, please find out the reason yourself.\033[0m")
        os.system("pause")

    elif(userinput == 3):
        os.system("cls")
        userinput_release = input("Please enter the release image directory:")
        os.system(f"dism /get-wiminfo /wimfile:\"{userinput_release}\"")
        userinput_release2 = input("Please select an index:")
        userinput_release3 = input("Please select the output path:")
        os.system(f"dism /apply-image /imagefile:\"{userinput_release}\" /index:{userinput_release2} /applydir:\"{userinput_release3}\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there is an error, please find out the reason yourself.\033[0m")
        os.system("pause")

    elif(userinput == 4):
        os.system("cls")
        userinput_wte = input("Please enter the file path to convert:")
        sleep(5)
        path = Path(userinput_wte)
        new_path = path.with_suffix(".esd")
        path.rename(new_path)
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there is an error, please find out the reason yourself.\033[0m")
        os.system("pause")

    elif(userinput == 5):
        os.system("cls")
        userinput_del = input("Folder or file path to be forcibly deleted:")
        input("Please wait a moment. You may, please press the Enter key.")
        os.system(f"takeown /f \"{userinput_del}\" /r /d y && icacls \"{userinput_del}\" /grant administrators:F /t")
        os.system(f"rd /s /q \"{userinput_del}\\*.*\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there is an error, please find out the reason yourself.\033[0m")
        os.system("pause")
    
    elif(userinput == 6):
        os.system("cls")
        userinput_etw = input("Please enter the file path to convert:")
        sleep(5)
        path2 = Path(userinput_etw)
        new_path2 = path2.with_suffix(".wim")
        path2.rename(new_path2)
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there is an error, please find out the reason yourself.\033[0m")
        os.system("pause")

    elif(userinput == 7):
        os.system("cls")
        os.system("systeminfo")
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there is an error, please find out the reason yourself.\033[0m")
        os.system("pause")

    os.system("cls")
    os.system("color 17")
    too_start = input("Main Menu(z) / Exit(e):")
    if(too_start == "z" or too_start == "Z"):
        os.system("cls")
        os.system("color 17")
        start_if = True
    else:
        start_if = False
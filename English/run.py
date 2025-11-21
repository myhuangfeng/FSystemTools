import os
from pathlib import Path
from time import sleep

systemlist = """
Welcome to FSystemTools System Utilities!

(1) Mount image to system
(2) Delete mounted or released image
(3) Release image to system
(4) Convert WIM to ESD
(5) Extended function: Force delete files
(6) Convert ESD to WIM
(7) View system information
"""

os.system("cls")
os.system("color 17")
start_if = True

while start_if:
    print(systemlist)
    userinput = int(input("Please select an option:"))

    if(userinput == 1):
        os.system("cls")
        userinput_mount = input("Select the image file to mount:")
        os.system(f"dism /get-wiminfo /wimfile:\"{userinput_mount}\"")
        userinput_mount2 = input("Please select index number:")
        userinput_mount3 = input("Please select output path:")
        os.system(f"dism /mount-wim /wimfile:\"{userinput_mount}\" /index:{userinput_mount2} /mountdir:\"{userinput_mount3}\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there are any errors, please troubleshoot yourself.\033[0m")
        os.system("pause")

    elif(userinput == 2):
        os.system("cls")
        userinput_delete = input("Enter the mounted or released image directory to delete:")
        os.system(f"dism /unmount-wim /mountdir:\"{userinput_delete}\" /discard")
        delete_if = input("Has it been unmounted? If not, press Enter to continue; otherwise press E to exit:")
        if(delete_if == 'E' or delete_if == 'e'):
            print("\033[32m**********\033[0m")
            print("\033[32m***win!***\033[0m")
            print("\033[32m**********\033[0m")
            print("\033[31mIf there are any errors, please troubleshoot yourself.\033[0m")
            os.system("pause")
            exit()
        userinput_formet = input("Format? If N, force deletion will be initiated (not recommended) (Y/N):")
        if(userinput_formet == 'Y' or userinput_formet == 'y'):
            userinput_formatinput = input("Enter the partition to format (e.g., for D drive enter D not D:):")
            os.system(f"powershell Format-Volume -DriveLetter {userinput_formatinput} -FileSystem NTFS -Force -Confirm:$false")
            print("\033[32m**********\033[0m")
            print("\033[32m***win!***\033[0m")
            print("\033[32m**********\033[0m")
            print("\033[31mIf there are any errors, please troubleshoot yourself.\033[0m")
            os.system("pause")
        else:
            input("Please wait, press Enter to continue after confirmation.")
            os.system(f"takeown /f \"{userinput_delete}\" /r /d y && icacls \"{userinput_delete}\" /grant administrators:F /t")
            os.system(f"rd /s /q \"{userinput_delete}\"")
            print("\033[32m**********\033[0m")
            print("\033[32m***win!***\033[0m")
            print("\033[32m**********\033[0m")
            print("\033[31mIf there are any errors, please troubleshoot yourself.\033[0m")
            os.system("pause")

    elif(userinput == 3):
        os.system("cls")
        userinput_release = input("Please enter the image file path to release:")
        os.system(f"dism /get-wiminfo /wimfile:\"{userinput_release}\"")
        userinput_release2 = input("Please select index number:")
        userinput_release3 = input("Please select output path:")
        os.system(f"dism /apply-image /imagefile:\"{userinput_release}\" /index:{userinput_release2} /applydir:\"{userinput_release3}\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there are any errors, please troubleshoot yourself.\033[0m")
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
        print("\033[31mIf there are any errors, please troubleshoot yourself.\033[0m")
        os.system("pause")

    elif(userinput == 5):
        os.system("cls")
        userinput_del = input("Folder or file path to force delete (e.g., G:\\Users):")
        input("Please wait, press Enter to continue after completion.")
        os.system(f"takeown /f \"{userinput_del}\" /r /d y && icacls \"{userinput_del}\" /grant administrators:F /t")
        os.system(f"rd /s /q \"{userinput_del}\"")
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there are any errors, please troubleshoot yourself.\033[0m")
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
        print("\033[31mIf there are any errors, please troubleshoot yourself.\033[0m")
        os.system("pause")

    elif(userinput == 7):
        os.system("cls")
        os.system("systeminfo")
        print("\033[32m**********\033[0m")
        print("\033[32m***win!***\033[0m")
        print("\033[32m**********\033[0m")
        print("\033[31mIf there are any errors, please troubleshoot yourself.\033[0m")
        os.system("pause")

    os.system("cls")
    os.system("color 17")
    too_start = input("Return to main menu(z) / Exit(e):")
    if(too_start == "z" or too_start == "Z"):
        os.system("cls")
        os.system("color 17")
        start_if = True
    else:
        start_if = False
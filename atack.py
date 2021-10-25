import pyautogui
import time

filename = input("Çıktı Dosya Adı=> ")
username = input("Kullanıcı Adı=> ")


def readFile():
    file = open(filename + ".txt", "r")
    lines = file.readlines()
    for index, line in enumerate(lines):
        pyautogui.typewrite(username)
        pyautogui.press("enter")
        pyautogui.typewrite(line)
        print("(" + str(index) + ")=>", line)
    file.close()


def timer(run):
    for i in range(5):
        print(str(5 - i) + " Saniye içerisinde başlatılacak.")
        time.sleep(1)
    run()


timer(readFile)

import pyautogui
import time
import GUI
from PIL import Image
import pytesseract


def clickgrifo():
    global buttongrifolocation
    buttongrifolocation = pyautogui.locateCenterOnScreen("prueba/GRIFO.png", confidence=.8, grayscale=True)


def cincok():
    global buttoncincolocation
    buttoncincolocation = pyautogui.locateCenterOnScreen("prueba/5k.png", confidence=.8, grayscale=True)


def veintek():
    global buttonveintelocation
    buttonveintelocation = pyautogui.locateCenterOnScreen("prueba/20k.png", confidence=.8, grayscale=True)


def cienk():
    global buttoncienlocation
    buttoncienlocation = pyautogui.locateCenterOnScreen("prueba/100k.png", confidence=.8, grayscale=True)


def quinientosk():
    global buttonquinientoslocation
    buttonquinientoslocation = pyautogui.locateCenterOnScreen("prueba/500k.png", confidence=.8, grayscale=True)


def jugar():
    buttonjugarlocation = pyautogui.locateCenterOnScreen("prueba/JUGAR.png", confidence=.8, grayscale=False)
    buttonjugarx, buttonjugary = buttonjugarlocation
    pyautogui.click(buttonjugarx, buttonjugary)


def leersaldo():
    global saldo
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"
    path = "C:/Users/soyju/Desktop/BOT LDLC/BOTCASINO/prueba/saldo.png"
    titles = pyautogui.getAllTitles()

    window = pyautogui.getWindowsWithTitle('MONOPOLY Poker')[0]
    left, top = window.topleft
    right, bottom = window.bottomright
    pyautogui.screenshot(path)
    im = Image.open(path)
    im = im.crop((left + 100, top + 50, right - 1140, bottom - 820))
    im.save(path)

    saldo = pytesseract.image_to_string(im, config='digits')
    saldo = (int("".join(ele for ele in saldo if ele.isdigit())))


def main():
    x = GUI.fichamin
    y = GUI.fichamin
    leersaldo()
    print("Saldo disponible: ", saldo)
    clickgrifo()
    buttongrifox, buttongrifoy = buttongrifolocation
    cincok()
    buttoncincox, buttoncincoy = buttoncincolocation
    veintek()
    buttonveintex, buttonveintey = buttonveintelocation
    cienk()
    buttoncienx, buttoncieny = buttoncienlocation
    quinientosk()
    buttonquinientosx, buttonquinientosy = buttonquinientoslocation
    try:
        while True:
            if saldo < x:
                exit("No hay suficiente saldo para realizar la apuesta")
            while x != 0:
                print("Fichas restantes para realizar la apuesta: ", x)
                if x / 500000 >= 1:
                    pyautogui.click(buttonquinientosx, buttonquinientosy)
                    x -= 500000
                elif x / 100000 >= 1:
                    pyautogui.click(buttoncienx, buttoncieny)
                    x -= 100000
                elif x / 20000 >= 1:
                    pyautogui.click(buttonveintex, buttonveintey)
                    x -= 20000
                elif x / 5000 >= 1:
                    pyautogui.click(buttoncincox, buttoncincoy)
                    x -= 5000
                pyautogui.click(buttongrifox, buttongrifoy)

            time.sleep(1)
            jugar()
            time.sleep(7)

            saldoantiguo = saldo
            leersaldo()
            print("Saldo registrado:", saldo)
            if saldoantiguo > saldo:
                y = y * 2
                x = y
                if GUI.fichamax != "":
                    if y > int(GUI.fichamax):
                        exit("Máx apuesta alcanzada")
            else:
                x = GUI.fichamin
                y = GUI.fichamin
    except KeyboardInterrupt:
        exit("Tecla presionada")
        pass


if __name__ == "__main__":
    main()

import pyscreenshot
from PIL import Image
from pytesseract import pytesseract
import re
import os
from time import gmtime, strftime
import time

def notification():
    for i in range(3):
        os.system('afplay /System/Library/Sounds/Glass.aiff')

def archiveTriggedImage(image):
    imageName = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    image.save('triggered_image/ctshk-{}.png'.format(imageName))

def monitoringHandler(num):
    print("{} - start screen monitoring...".format(num))
    screenshot=pyscreenshot.grab()
    print(screenshot)
    screenshot.save('ctshk.png')

    image_path = "ctshk.png"
    text = pytesseract.image_to_string(Image.open(image_path), lang='eng')

    regExpression = '[0-1][0-9]\/03\/\d{4}'
    latestDates = re.findall(regExpression, text)

    if len(latestDates) > 0:
        print("triggering notification")
        notification()
        archiveTriggedImage(screenshot)

if __name__ == "__main__":
    notification()
    num = 1
    while True:
        monitoringHandler(num)
        time.sleep(1)
        num = num + 1
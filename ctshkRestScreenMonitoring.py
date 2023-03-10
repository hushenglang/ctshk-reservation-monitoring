import requests
import re
import os
import time

def notification():
    for i in range(3):
        os.system('afplay /System/Library/Sounds/Glass.aiff')

def archiveTriggedLog(logTitle, logContent):
    fileName = time.strftime("%Y%m%d-%H%M%S")
    with open("triggered_log/"+fileName+'.txt', 'w') as f:
        f.write(str(logTitle))
        f.write(logContent)

def validateHTMLTextContainDate(htmlText):
    regExpression = '[0-9][0-9]\/[0-9][0-9]\/\d{4}'
    htmlLatestDates = re.findall(regExpression, htmlText)
    print(htmlLatestDates)

def monitoringHandler(num):
    print("{} - start ctshk rest reservation monitoring...".format(num))
    url = "https://www.ctshk.com/pass/change1.jsp"
    cookie_jar = {"JSESSIONID": "0000K-7q7hLlB3TJ8ZdVoSr_dXm:-1",
                  "pll_language": "zh",
                  "_ga": "GA1.1.1242780874.1678023586",
                  "_ga_G5RX4FKE3N": "GS1.1.1678185753.6.1.1678231468.0.0.0"
                  }
    payload = {'bknum': '[Your Reservation number]',
               'bthDate': '[yyyymmdd]'}
    res = requests.post(url, cookies=cookie_jar, data=payload)
    html_text = res.text
    validateHTMLTextContainDate(html_text)
    regExpression2 = '[0-1][0-9]\/03\/\d{4}'
    htmlLatestDates2 = re.findall(regExpression2, html_text)
    if len(htmlLatestDates) > 0:
        print("triggering notification")
        print(htmlLatestDates)
        print(htmlLatestDates2)
        notification()
        archiveTriggedLog(htmlLatestDates, html_text)

if __name__ == "__main__":
    num = 1
    while True:
        monitoringHandler(num)
        time.sleep(0.5)
        num = num + 1
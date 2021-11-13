from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:/Users/basti/OneDrive/Desktop/Covid_Notification/icon.ico",
        timeout = 5
    )

def getData(url):
    r = requests.get(url)
    return r.text
    
if __name__ == "__main__":
    while True:
        # notifyMe("Hey!", "Lets stop this virus outbreak")
        myHtmlData = getData('https://www.sscadda.com/coronavirus-in-india-check-state-wise-report-latest-updates')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify())
        myDataStr = " "
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[2:]
        itemList = myDataStr.split("\n\n")

        states = ['Odisha', 'Telangana', 'Maharashtra']
        for item in itemList[0:36]:
            dataList = item.split("\n")
            if dataList[0] in states:
                print(dataList)
                nTitle = 'Cases of covid-19'
                nText = f"State : {dataList[0]}  \nConfirmed cases : {dataList[1]} \nRecoveries : {dataList[2]} \nDeaths : {dataList[3]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)
            
    


    

    



    
    

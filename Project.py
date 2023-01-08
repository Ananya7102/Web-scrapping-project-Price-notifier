import requests
from bs4 import BeautifulSoup
import smtplib
import time

while True:
    re = requests.get('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
    res = re.content
    soup = BeautifulSoup(res, 'html.parser')
    #print(soup.prettify())
    price = float(soup.find('p', class_='price_color').text[1:])

    if price < 60:
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        print(smt)
        smt.ehlo()
        smt.starttls()
        smt.login("ananyagupta.ke@gmail.com", "ogksglgahbudfxtf")
        message = "Buy the book Sapiens a brief Human History\n Price dropped to "+str(price)
        smt.sendmail('ananyagupta.ke@gmail.com',
                     'ananya7102@gmail.com',
                     f"Subject: Price notifier\n\n ,{message}")
        smt.quit()
        
    time.sleep(24*60*60)




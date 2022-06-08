#import libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import pandas as pd
import csv

def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
  
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    product = soup2.find(id='productTitle').get_text() 

    price = soup2.find('span', {'class':'a-offscreen'}).get_text()

    number_of_ratings = soup2.find(id='acrCustomerReviewText').get_text()

    price = price.strip()[1:]

    price = float(price)

    product = product.strip()

    number_of_ratings = number_of_ratings.strip()

    number_of_ratings = number_of_ratings.removesuffix('ratings')

    number_of_ratings = float(number_of_ratings)

    today = datetime.date.today()

    header_row = ['Product', 'Price','Date','Number_Of_Ratings']

    data = [product,price,today,number_of_ratings]

    with open('Amazon_Web_Scraped_Dataset.csv', 'a+',newline = '', encoding = 'UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    if (price > 14):
        send_mail()


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',587)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('tamarapreyejumbo@gmail.com','Gambit4175_')
    
    subject = "Just testing out this function"
    body = "Hey it works!!!"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'tamarapreyejumbo@gmail.com',
        msg
     
    )

df = pd.read_csv('Amazon_Web_Scraped_Dataset.csv')
print(df)

while(True):
    check_price()
    time.sleep(5)
# import required files and modules

import requests
from bs4 import BeautifulSoup
import smtplib
import time

# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# send a request to fetch HTML of the page
response = requests.get('https://www.amazon.in/dp/B08M8KCRQ4/ref=cm_sw_r_wa_apa_i_Sfl2FbWHXP2NX?psc=1', headers=headers)

# create the soup object
soup = BeautifulSoup(response.content, 'html.parser')

# change the encoding to utf-8
soup.encode('utf-8')

#print(soup.prettify())

# function to check if the price has dropped below 20,000
def check_price():
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  #print(price)

  #converting the string amount to float
  converted_price = float(price[0:5])
  print(converted_price)
  if(converted_price < 5000):
    send_mail()

  #using strip to remove extra spaces in the title
  print(title.strip())




# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('<AMAZON-LOGIN-MAIL-ID>', '<PASSWORD>')

  subject = 'Price Fell Down'
  body = "Check the amazon link https://www.amazon.in/dp/B08M8KCRQ4/ref=cm_sw_r_wa_apa_i_Sfl2FbWHXP2NX?psc=1 "

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    '<AMAZON-LOGIN-MAIL-ID>',
    'RECEIVERS-MAIL-ID>',
    msg
  )
  #print a message to check if the email has been sent
  print('Hey Email has been sent')
  # quit the server
  server.quit()

#loop that allows the program to regularly check for prices
while(True):
  check_price()
  time.sleep(60 * 60)


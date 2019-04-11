#! python3

from bs4 import BeautifulSoup
import requests, smtplib

getPage = requests.get('http://vietnamcafe.us/menu/#appetizer')
getPage.raise_for_status()
page = BeautifulSoup(getPage.text, 'html.parser')
appetizer_page = page.select_one('#appetizer')
#print(appetizer_page)
appetizer_name = appetizer_page.find_all('div',class_="av-catalogue-title")

food_need = 'Goi Ga'
count = 0
for list in appetizer_name:
    appetizer = (list.text).split('.')[1].lstrip().rstrip()
    if appetizer == food_need:
       count = count + 1 
    #print(appetizer)


count = 1
if count > 0:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('Your Email Address', 'Password')
    subject = 'vietnam cafe appetizer'
    msg ="The Appetizer is available"
    message = 'Subject: {}\n\n{}'.format(subject,msg)
    conn.sendmail('recipient Email Address','recipient Email Address', message)
    #conn.sendmail(from_entry.get(),to_entry.get(),msg_entry.get())
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')

    #send e-mail alert
    print("The Goi Ga Appeizer is available")
else:
    print("The Goi Ga Appeizer is not available")


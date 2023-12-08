import requests
from bs4 import BeautifulSoup
import smtplib


def SendEmail(item_name, current_price, target_price ,email_address):
    subject =f"Price Drop Alert: {item_name}"
    body =f"The Price of {item_name} has dropped to {current_price}. Time to buy it."

    sender_email ="your_email@gmail.com"
    sender_password ="your_password"
    receiver_email =email_address

    server =smtplib.SMTP("smtp.gmail.com" ,587)
    server.starttls()
    server.login(sender_email,sender_password)


    message =f"Subject: {Subject}\n\n{body}"
    server.sendmail(sender_email,receiver_email,message)

    server.quit()

def track_price(url, item_name, target_price, email_address):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    current_price_str = soup.find('span', {'class': 'current-price'}).text
    current_price = float(current_price_str.replace('$', '').replace(',', ''))

    if current_price < target_price:
        send_email(item_name, current_price, target_price, email_address)
        print(f"Email notification sent. Price of {item_name} dropped to {current_price}.")

url = "https://example.com/product-page"
item_name = "Example Product"
target_price = 100.0
email_address = "your_email@example.com"

track_price(url, item_name, target_price, email_address)


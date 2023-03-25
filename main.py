import requests
from bs4 import BeautifulSoup
import smtplib


MY_EMAIL = "Your Email id"
PASSWORD = "Password"

URL = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/ref=dp_fod_3?pd_rd_w=OhCgB&content-id=amzn1.sym.68174014-ed7a-4e35-badd-6d3576b85c0b&pf_rd_p=68174014-ed7a-4e35-badd-6d3576b85c0b&pf_rd_r=41TSE2Q9RA3RPTRZ9GVG&pd_rd_wg=gLGAt&pd_rd_r=271f9724-6923-41a0-893a-5644cb2e9d50&pd_rd_i=B075CWJ3T8&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
content = response.text

soup = BeautifulSoup(content, "html.parser")
soup.getText()

price =soup.find(name="span", class_="a-offscreen")
price_without_currency = price.text.split("$")[1]
float_price = float(price_without_currency)
print(float_price)



title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if float_price < BUY_PRICE:
    message = f"{title} is now {float_price}"
    encoded = message.encode('utf-8')

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{encoded}\n{URL}"
        )
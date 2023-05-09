import requests
from bs4 import BeautifulSoup

def main(args):
    ticker = args["ticker"]
    url = f"https://seekingalpha.com/symbol/{ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the stock price element
    price = soup.find("span", class_="rr-T6 V-gY V-hf V-hk").text.strip()

    # Find the stock change % element
    change = soup.find("span", class_="rr-ju rr-Uc V-gS V-g5 V-hk V-hZ V-if V-iq").text.strip()

    # Return the scraped data as a dictionary
    return {
        "body": {"ticker": ticker.upper(), "price": price, "change": change}
    }
import requests
from twilio.rest import Client

STCK_Endpoint = "https://www.alphavantage.co/query"
my_api_key = "your_api_key"
API_KEY_NEWS = "api_key_news"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Twilio
account_sid = "account_sid"
auth_token = "auth_token"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": my_api_key
}

stock_response = requests.get(STCK_Endpoint, params=parameters)
stock_data = stock_response.json()
dates = stock_data["Time Series (Daily)"]
news_url = "https://newsapi.org/v2/everything"

parameters = {
    "q": COMPANY_NAME,
    "sortBy": "popularity",
    "apiKey": API_KEY_NEWS,
}

news_response = requests.get(news_url, params=parameters)
news_data = news_response.json()

articles = news_data["articles"]

a_list = []

for arti in articles:
    arti_date = arti["publishedAt"][0:10]
    arti_desc = arti["description"]
    news_dict = {
        "date": arti_date,
        "article": arti_desc,
    }
    a_list.append(news_dict)
# print(a_list)
d_list = []

for day in dates:
    closed_prices = float(dates[day]["4. close"])
    closed_prices_dict = {
        "date": day,
        "price": closed_prices,
    }
    d_list.append(closed_prices_dict)
# print(d_list)
# a = len(d_list) - 1
a = 7
# b = len(d_list) - 2
b = 8
first = d_list[a]["price"]
second = d_list[b]["price"]


def do_math(num1, num2):
    per = num1 / 100
    calc = num1 - num2
    res = calc / per
    return round(res, 2)


result = do_math(first, second)

if result > 5:
    for i in a_list:
        if d_list[a]["date"] == i["date"]:
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                    body=f"Stock has decreased with {result}%💹, reason:{i['article']}🙆🏽‍♂️",
                    from_="+13464897117",
                    to="+4522220857"
                )
        print(f"Stock price has decreased with {result} percent, and the reason: {i['article']}.")
elif result < 5:
    for i in a_list:
        if d_list[a]["date"] == i["date"]:
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                    body=f"Stock has decreased with {result}%🔻, reason:{i['article']}🤷🏽‍♂️",
                    from_="+13464897117",
                    to="+4522220857"
                )
        print(f"Stock price has increased with {result} percent, and the reason: {i['article']}")

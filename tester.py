import requests

# url = 'http://localhost:8080/costOfEquity'
url = "https://costofequity-a7qpzjn6yq-an.a.run.app/costOfEquity"
params = {
    'ticker': '4563.T',
    'premium': '0.1',
    # 'yfinance': 'True',
    # 'beta': '0.5',
    # 'riskFreeRate': '0.1',
    # 'freq': 'W',
    # 'period': '365'
}

response = requests.get(url, params=params)
# print(response.content)
print(response.json())
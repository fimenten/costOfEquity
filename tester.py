import requests

url = 'http://localhost:8080/costOfEquity'
params = {
    'ticker': '4563.T',
    'premium': '1.5',
    # 'yfinance': 'True',
    # 'beta': '0.5',
    # 'riskFreeRate': '0.1',
    # 'freq': 'W',
    # 'period': '365'
}

response = requests.get(url, params=params)

print(response.json())
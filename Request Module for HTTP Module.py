import requests
r=requests.get("https://financialmodelingprep.com.api/company/price/AAPL")
print(r.text)
print(r.status_code)
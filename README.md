# 💱 Currency Converter (using CurrencyAPI.com)

A simple Python program to **list currencies, check exchange rates, and convert between currencies** using the [CurrencyAPI](https://currencyapi.com/docs).

---

## 🚀 Features
- Fetches and displays a list of available currencies (with names, codes, and symbols).
- Retrieves latest exchange rates.
- Converts any amount between two currencies.
- CLI-based interactive tool.

---

## 🛠️ Installation

1. Clone this repository:

Optional

```js
   git clone https://github.com/YOUR_USERNAME/currency-converter-api.git
   cd currency-converter-api
 ```

## Install dependencies:

```js
pip install -r requirements.txt.
```

## 📄 requirements.txt

```js
currencyapicom
requests
```

Add your CurrencyAPI key inside currency_converter.py:

```js
API_key = "YOUR_API_KEY_HERE"
```

## ▶️ Usage

Run the program:

```js

python.exe currency_converter.py

```


You will see:

```js

Welcome to the currency converter
List - Lists of the different currencies
Convert - Convert from one currency to another
```

Example:

```js
Enter a command (q to quit): list
USD - United States Dollar - $
EUR - Euro - €
JPY - Japanese Yen - ¥
...

Enter a command (q to quit): convert
Enter a base id: USD
Enter a currency to be convert to: EUR
Enter the amount in USD: 100
100 USD is equal to 91.23 EUR with rate: 0.9123

```

## Demo 



https://github.com/user-attachments/assets/d0bbf220-7e2a-4157-9a20-12f08d1ac4c1




## 📦 Dependencies

currencyapicom
 – Currency API client

requests
 – HTTP requests

pprint
 – for better output formatting

## ⚠️ Note

You need a valid API key from CurrencyAPI
.

Free plans have limits (250 requests/month at the time of writing).

   


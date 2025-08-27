import currencyapicom  # as per the website of the api https://currencyapi.com/docs/currencies
from requests import get
from pprint import PrettyPrinter

# to have a nice display of the dictionnary to get from the APi

# mini program to convert currency using API, it can get the ratio, convert amount


printer = PrettyPrinter()

base_url = "https://api.currencyapi.com/"
API_key = "your_api_key"

def get_currency():

    client = currencyapicom.Client('your_api_key')
    result = client.currencies()
    return result


def print_currencies(currencies):
    for code, info in currencies['data'].items():
        name = info.get('name')
        code = info.get('code')
        symbol = info.get('symbol',"")  # safely get the symbol

        print(f"{code} - {name} - {symbol}")



# to get the currency ratio, we can use the module from the website as the way we get the currency above
"""
import currencyapicom

client = currencyapicom.Client('YOUR-API-KEY')
result = client.latest()
print(result)
"""

# but for this demonstration of get API, we're going to use the get method

def exchange_rate(currency): # those variables in the function are gonna be the IDs

    endpoint = f"v3/latest?apikey={API_key}"

    url = base_url + endpoint

    #print(url)

    data = get(url).json()

    if len(data) == 0:
        print("Invalid currencies")
        return None

    elif currency not in data.get('data'):

        return None



    else:




        rate = data.get('data')[currency].get('value')

        return rate




def convert(currency1, currency2, amount):
    rate1 = exchange_rate(currency1)
    rate2 = exchange_rate(currency2)

    if rate1 == False or rate2 == False:
        print("\n One of the currency entered is invalid !!")
        return None

    elif rate1 == False and rate2 == False:
        print("\n The currencies you have provided are not valid !!!")
        return None

    elif rate1 == None or rate2 == None:
        return None


    else:


        try:
            amount = float(amount)
        except:
            print("Invalid amount.")
            return

        rate = 1/rate1 * rate2
        converted_amount = round(rate * amount, 4)


        return converted_amount, rate

def main():
    data = get_currency()

    print("Welcome to the currency converter")
    print("List - Lists of the different currencies")
    print("Convert - Convert from one currency to another")
    print()


    while True:
        command = input("Enter a command (q to quit) :").lower()

        if command == 'q':
            break
        elif command == "list":
            currencies = get_currency()
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base id: ").upper()
            currency2 = input("Enter a currency to be convert to : ").upper()
            amount = input(f"Enter the amount in {currency1} :")

            if currency1 == None or currency2 == None:
                exit()

            else:

                convert(currency1, currency2, amount)

                if convert(currency1, currency2, amount) == None:
                    print("Conversion failed. Please try again.\n")
                else:
                    converted_amount, rate = convert(currency1, currency2, amount)


                    print(f"{amount} {currency1} is equal to {converted_amount} {currency2} with rate: {rate}")


if __name__ == '__main__':
    main()









import requests
api_key='4d3441ff3b77dc371771b30b'



url=f'https://v6.exchangerate-api.com/v6/4d3441ff3b77dc371771b30b/latest/USD'

response=requests.get(url)

data=response.json()
# rate=data['conversion_rate']

# print(rate)

# amount=float(input('Enter the amount'))


# converted_amount=amount*rate

# print(converted_amount)

i=data['conversion_rates'].keys()

print(i)
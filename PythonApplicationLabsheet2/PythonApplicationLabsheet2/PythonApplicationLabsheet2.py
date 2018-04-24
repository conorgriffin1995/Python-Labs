# Garys answer
euro_rates = {'usd': 1.22339, 'gbp': 0.87582, 'aud': 1.417, 'cad': 1.56900}

def convert_from_euro(value, to_currency):
        return value * euro_rates[to_currency]

def convert_to_euro(from_currency, value):
    return value * (1 / euro_rates[from_currency])

print (convert_from_euro(100, 'usd'))
print (convert_to_euro('usd', 100))


# function to convert a currency amount in euros to amount in usd, gbp, cad
def convertEuros():
	while True:
		try:
			print("Converter from Euros to USD$, GBP£, CAD$")
			amount = float(input("Enter amount to convert: €"))
			print("Enter currency '$' or '£' or 'CAD$' :")
			currency = input()
			if(currency == "$"):
				sum = amount * 1.22339	
				print("Converted to USD = $", sum)
			elif(currency == "£"):
				sum = amount * 0.87582
				print("Converted to GBP = £", sum)
			elif(currency == "CAD$"):
				sum = amount * 1.56900
				print("Converted to CAD = $", sum)
			else:
				print("Currency not recognised, try again..")
				continue
		except ValueError as valerr:
			print(valerr)
			continue
		else:
			break		
convertEuros()	

# function to convert a currency amount in us dollars to amount in eur, gbp, cad
def convertDollars():
	while True:
		try:
			print("Converter from Dollars to EUR€, GBP£, CAD$")
			amount = float(input("Enter amount to convert: $"))
			print("Enter currency '€' or '£' or 'CAD$' :")
			currency = input()
			if(currency == "€"):
				sum = amount * 0.81726
				print("Converted to EUR = €", sum)
			elif(currency == "£"):
				sum = amount * 0.71576
				print("Converted to GBP = £", sum)
			elif(currency == "CAD$"):
				sum = amount * 1.28239
				print("Converted to CAD = $", sum)
			else:
				print("Currency not recognised, try again..")
				continue
		except ValueError as valerr:
			print(valerr)
			continue
		else:
			# amount was successfully parsed
			break
convertDollars()

# bank account
euro_account = []

# function balance
def balance(trans):
	return sum(trans)

# + debit
def debit(amount, account):
	if(amount > 0):
		account.append(amount)
	else:
		raise ValueError("Invalid Attempt")

# - credit
def credit(amount, account):
	if(amount > 0):
		if(amount <= balance(account)):
			account.append(-amount)
		else:
			raise ValueError("Insufficient funds")
	else:
		raise ValueError("Invalid Attempt")

debit(100, euro_account)	# debit
debit(200, euro_account)	# debit
credit(50, euro_account)	# credit

print("EURO ACCOUNT TRANSACTIONS: ", euro_account)
print("BALANCE: €", balance(euro_account))	# print balance euro account

# MY WAY
# convert to dollars
dollar_account = []				# us dollar account
for i in euro_account:
	dollar_account.append(i * 0.82)	# add transactions in dollars

print("DOLLAR ACCOUNT TRANSACTIONS: ", dollar_account)
print("BALANCE: $", balance(dollar_account))	# print balance dollar account

# GARYS WAY OF DOING IT
# convert to dollars
dollars = map(lambda euro: convert_from_euro(euro, 'usd'), euro_account)
print (list(dollars))

# format the account
from functools import reduce
def formatEuro(a, b):
	output = ''
	if b < 0:
		output += 'credit: '
	else:
		output += 'debit: '
	return str(a) + output + str(b) + ' '
output = reduce(formatEuro, euro_account, '')
print("Euro Account: ",output)

def formatDollar(a, b):
	output = ''
	if b < 0:
		output += 'credit: '
	else:
		output += 'debit: '
	return str(a) + output + str(b) + ' '
output = reduce(formatEuro, dollar_account, '')
print("Dollar Account: ",output)

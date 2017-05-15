balance = 5000
annualInterestRate = 0.18
backup = balance
epsilon = 0.2
lower = balance / 12.0
upper = balance * (1 + annualInterestRate / 12)**12 / 12
payment = (lower + upper) / 2
while True:
   balance = backup
   for i in range(1, 13):
   	unPaidBalance = balance - payment
   	interest = annualInterestRate / 12 * unPaidBalance
   	balance = unPaidBalance + interest
   print("upper: " + str(upper))
   print("lower: " + str(lower))
   print("balance: " + str(balance))
   print("payment: " + str(payment))
   if abs(balance) < epsilon:
	break
   elif balance < 0:
	upper = payment
   else:
      	lower = payment
   payment = (lower + upper) / 2
   raw_input("continue?")
print("Lowest payment: " + str(round(payment, 2)))


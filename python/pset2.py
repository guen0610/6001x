annualInterestRate = 0.18
balance = 5000
monthlyPaymentRate = 0.02
totalPaid = 0

for i in range(1, 13):
   minPayment = balance * monthlyPaymentRate 
   unPaidBalance = balance - minPayment
   interest = annualInterestRate / 12 * unPaidBalance
   balance = unPaidBalance + interest
   totalPaid += minPayment
   print("Month: " + str(i))
   print("Minimum monthly payment: " + str(round(minPayment, 2)))
   print("Remaining balance: " + str(round(balance, 2)))
print("Total paid: " + str(round(totalPaid, 2)))
print("Remaining balance: " + str(round(balance, 2)))

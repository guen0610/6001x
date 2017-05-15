annualInterestRate = 0.18
backup = balance
totalPaid = 0
fixedPayment = 0
while balance > 0:
   balance = backup
   fixedPayment += 10
   for i in range(1, 13):
   	unPaidBalance = balance - fixedPayment
   	interest = annualInterestRate / 12 * unPaidBalance
   	balance = unPaidBalance + interest
print("Lowest payment: " + str(round(fixedPayment, 2)))


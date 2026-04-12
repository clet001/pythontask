principal =  int(input("Input Principal"))
annualinterestrate = float(input("Input Annual Interest Rate"))
duration = int(input("Duration"))

monthlypayment = 0

monthlypayment = principal * annualinterestrate * (1 + annualinterestrate) ** duration // (1 + annualinterestrate) ** duration - 1


print("Your monthly payment is: ", monthlypayment)

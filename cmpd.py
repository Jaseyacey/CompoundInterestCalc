principalinput = input("Enter principal: ")
annualrateinput = input("Enter annual rate: ")
numberoftimescompoundedinput = input(
    "Enter number of times that the interest is compounded per year: ")
yearsinput = input("Time in years: ")
monthlycontributioninput = input("Enter monthly contribution amount: ")

# Convert entered input from strings into integers
principal = int(principalinput)
annualrate = (int(annualrateinput))/100
numberoftimescompounded = int(numberoftimescompoundedinput)
years = int(yearsinput)
monthlycontribution = int(monthlycontributioninput)

# calculate compound interest plus the principal
preliminarynumber = (1 + (annualrate/numberoftimescompounded))
# print ("Preliminary number:", preliminarynumber)
raisedtopower = (numberoftimescompounded * years)
# print ("Raised to power:", raisedtopower)
compoundinterestplusprincipal = principal * (preliminarynumber**raisedtopower)
print("The compound interest plus the principal is: ",
      compoundinterestplusprincipal)

# Now calculate the future value with deposits made at the end of the period
# Using formula: Monthly Payment × ( ( ( (1 + r/n)^(nt) ) - 1 ) / (r/n) )
# r = annual interest rate
# n = number of compounds per period (usually in months)
# t = time the money is invested (usually in years)

oneplus = (1+(annualrate/numberoftimescompounded))
raisedtopower2 = ((numberoftimescompounded*years))
ratedividedbynumberoftimes = annualrate/numberoftimescompounded
halfdone = (((oneplus**raisedtopower2)-1)/ratedividedbynumberoftimes)
futurevaluewithdeposits = monthlycontribution*halfdone
print("Future value with deposits: ", futurevaluewithdeposits)
totalamount = compoundinterestplusprincipal + futurevaluewithdeposits
print("Total Amount:", totalamount)

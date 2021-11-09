A = int(input("Enter the shopping amount of customer"))
if A > 25000 :
    P = A - (A / 5)
    print(f"The category of the customer is GOLD and the payable amount is {P}")
elif 10000 <= A >= 2500 :
    P = A - (A / 10)
    print(f"The category of the customer is SILVER and the payable amount is {P}")
else :
    P = A - (A / 20)
    print(f"The category of the customer is BRONZE and the payable amount is {P}")

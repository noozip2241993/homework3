change = int(input("Enter your payment: "))
quarters = int(change//25)
dimes = int((change- 25*quarters)//10)
pennies= int((change - 25*quarters - 10*dimes))
print("Your change is:")
print(f'{quarters} quarters')
print(f'{dimes} dimes')
print(f'{pennies} pennies')
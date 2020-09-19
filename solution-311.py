SENTINEL = -1
total_miles = 0

total_gallon = 0

while True:
    gallon = float(input("Enter the gallons used (-1 to end): "))
    if gallon == SENTINEL:
        break
    miles = float(input("Enter the miles driven: "))
    mile_gallon= miles/gallon
    print(f'The miles/gallon for this tank was {mile_gallon:6f}')
    total_miles =total_miles + miles
    total_gallon = total_gallon + gallon
    
  
print(f'The overall average miles/gallon was {total_miles/total_gallon:.6f}')

SENTINEL = -1
total_miles_gallon = 0

mile_gallon_counter = 0

while True:
    gallon = float(input("Enter the gallons used (-1 to end): "))
    if gallon == SENTINEL:
        break
    miles = float(input("Enter the miles driven: "))
    mile_gallon= miles/gallon
    print(f'The miles/gallon for this tank was {mile_gallon:6f}')
    total_miles_gallon =total_miles_gallon+mile_gallon
    mile_gallon_counter = mile_gallon_counter + 1
    
  
print(f'The overall average miles/gallon was {total_miles_gallon/mile_gallon_counter:.6f}')

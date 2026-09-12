electricity_unit = int(input('Enter Electricity Unit: '))

if electricity_unit > 0 and electricity_unit <= 100:
    bill = 50 + 3*electricity_unit
elif electricity_unit >=101 and electricity_unit <= 300:
    bill = 100 + 5*electricity_unit
elif electricity_unit >=301 and electricity_unit <= 500:
    bill = 150 + 7.50*electricity_unit
elif electricity_unit >500:
    bill = 250 + 10*electricity_unit
print(f"Electricity Bill : {bill} Rupees")
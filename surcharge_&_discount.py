print("=========SURCHARGE AND DICOUNT RULE===========")
user=input('Enter user: ')
base_fee=float(input('Enter base fee: '))
final_fee = base_fee

if user=="student":
     cgpa=float(input("Enter cgpa: "))
     if cgpa>=8.5:
          final_fee=final_fee - (base_fee*.20)
     elif cgpa>7.5 and cgpa<8.49:
          final_fee = final_fee - (base_fee*.10)
elif user=="faculty" or user=="staff":
     service_year=int(input('Enter year of service: '))  
     if service_year>10:
          final_fee = final_fee - (base_fee*.15)
vehicle=input("Enter vehicle type: ")
if vehicle=="two wheeler":
     final_fee = final_fee + 200
elif vehicle == "four wheeler":
     final_fee = final_fee + 600
     if user=="student":
          final_fee=final_fee+150
elif vehicle == None:
     final_fee=final_fee + 0

print(f"Final Fee : {final_fee}")
           

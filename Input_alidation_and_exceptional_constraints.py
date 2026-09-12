
cgpa = float(input('Enter CGPA: '))
Electricity_unit =int(input('Enter Electricity Unit: '))
Service = int(input('Enter Year of Service: '))
try:
    if cgpa>0.0 and cgpa<10.0:
        raise
    print(f"CGPA:{cgpa}")
    if Electricity_unit >= 0:
        raise
    print(f"Electricity Bill:{5*Electricity_unit}")
    if Service >0 :
        raise
    print(f"Service of Year:{Service}")
except:
    print("ERROR")
finally:
    print("Bye")

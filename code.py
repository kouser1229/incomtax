ai=int(input("Enter annual income:"))
hra=int(input("Enter house rent:"))
ded=int(input("enter deduction amount:"))
tax=ai-(hra+ded)
print("Tax is:",tax)
if(tax<300000):
    print("no tax")
elif(tax>300000 and tax<600000):
    print("10% of interest on tax")
    print("Total incometax to be paid by an employee:",0.1*tax)
elif(tax>60000 and tax<100000):
    print("15% of interest on tax")
    print("Total incometax to be paid by an employee:",0.15*tax)
elif(tax>1000000):
    print("20% of interest on tax")
    print("Total incometax to be paid by an employee:",0.2*tax)
else:
    print("Total incometax to be paid by an employee:",tax)

loan = int(input("Enter your loan amount : "))
roi = float(input("Enter rate of interest : "))
tennure = int(input("Enter the tenure in month : "))

bundle = loan + (loan*0.02)

interest = (bundle*roi)*(tennure/12)
print(bundle)






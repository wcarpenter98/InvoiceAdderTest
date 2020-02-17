#Zach's Invoice Adder for Onedrive

file = open(r"/Users/williamcarpenter/Desktop/AddNumber.txt", "r")

line = file.read()

line = line.rstrip()
line = line.replace("\n", "")
line = line.rstrip()
print(line)
line = line.split()
#line = line.split("$")

#print (line.split("$"))
#line = line.remove('$')

line = ([s.replace('$', '') for s in line]) # remove all the 8s
print(line)

total = sum([int(num) for num in line])
print("---------------------------Below--is--6.5% sales tax---------------------------")
print("The total without sales tax is " + str(total))




salesTaxTotal = 0.065 * total

print("Sales tax is " + str(salesTaxTotal))

totalDisplay = total + salesTaxTotal
print("Overall total is " + str(totalDisplay))

      

print("---------------------------Below--is--7.0% sales tax---------------------------")
print("The total without sales tax is " + str(total))


salesTaxTotal = 0.07 * total

print("Sales tax is " + str(salesTaxTotal))

totalDisplay = total + salesTaxTotal
print("Overall total is " + str(totalDisplay))


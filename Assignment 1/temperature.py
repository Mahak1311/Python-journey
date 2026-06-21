'''Ask the user for a temperature in Celsius (string input).
Convert it to float ,then calculate and print temperature in Fahrenheit.
Conversion formula:Fahrenheit Temp=(Celsius Temp∗(9/5))+32'''
temp = int(input("Enter temperature in Celsius: "))
a = float(temp)
fahrenheit = float(((a*(9/5)) +32))
print("The temperature in fehrenheit = " ,fahrenheit)
#converts inches into centimeters and vice-versa based on what user wants
value = input("Enter value in either inch or cm: ")
def convert(value):
  if "inch" in value:
    num = float(value.replace("inch", "").strip()) #replaced inch with space coz when multiplying python needs only numbers and not words
    return 2.5 * num

  elif "cm" in value:
    num = float(value.replace("cm", "").strip())
    return num/2.5
print(convert(value))



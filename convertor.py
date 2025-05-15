def celsius_to_Fahrehenite(celsius):
  Fahrehenite=(celsius*9/5)+32
  return Fahrehenite
celsius_input = float(input("enter temperature : "))
Fahrehenite_output = celsius_to_Fahrehenite(celsius_input)
print(f"{celsius_input}degree in celsius = {Fahrehenite_output} degree in fahrehenite")    
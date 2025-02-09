#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = 80

  tempC = round((tempF-32) / 1.8, 1) #Round to 1 decimal place 

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()

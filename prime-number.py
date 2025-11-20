def primeTest(x):
    if x <= 1:
      return "非質數"
    elif x == 2:
      return "質數"
    elif x % 2 == 0:
      return "非質數"
    
    for i in range(3, int(x**0.5+1)):
      if x%i == 0:
        return "非質數"
    
    return "質數"

while True:
  inputNumber = int(input("請輸入整數："))
  if inputNumber == -999:
    break
  print(inputNumber, "為", primeTest(inputNumber),sep="")
import XLibrary
Num = int(input("Dame un numero a calcular la serie de numeros de collatz \n>"))
L = XLibrary.collatz(Num)
print(f"Se calcularon {len(L)} numeros")
print(f"==>{L} ..._...")

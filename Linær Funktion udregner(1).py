import matplotlib.pyplot as plt # library to do with maths, also note it is being renamed to plt instead of matplotlib
import numpy as np # numpy has to do with data and numbers. also numpy is getting renamed to np so the dev can call its functions without writing the full name, a sort of short hand.

# Spørg brugeren for input
a = float(input("Skriv a (hældningskoefficient): "))
b = float(input("Skriv b (konstanten): "))
x_input = float(input("Skriv hvor mange måneder der er gået: "))

# Udregner y værdien
y_output = a * x_input + b
print("Når x er = ", x_input, "Så er y = ", y_output)

# Tegner en graf for funktionen
x_values = np.linspace(x_input - 15, x_input + 15, 115)

# Laver en række x-værdier til grafen
y_values = a * x_values + b

# Tegner grafen
plt.plot(x_values, y_values, label = "f(x) = "+str(a) + "x +" +str(b))
plt.scatter(x_input, y_output, color="red", label="punkt: ("+str(x_input)+", "+str(y_output)+")")

plt.title("Graf af f(x) = a*x + b")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
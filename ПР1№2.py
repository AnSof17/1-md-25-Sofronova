print("Enter the seat number: ")
 a = int(input())
 if a%2 == 0:
     x = "Upper,"
 else:
     x = "Lower,"
 if a > 36 and a < 55:
     y = "Side seat"
 elif a > 0 and a < 37:
     y = "Compartment seat"
 if a < 1 or a > 54:
     x = "There is't such seat"
     y = ""
 print(x, y)
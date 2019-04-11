import random
import sys
val_secret = random.randint(0,9)
print(val_secret)
answer = None

for i in range(3):
    
    if answer != val_secret:
        answer = int(input("entrer une valeur comprise entre 0 et 9 \n"))
    if answer > val_secret:
        print(" val-secret est inferier a la valeur donner \n")
    elif answer > val_secret:
        print("val-secret est superieur a la valeur donner \n")
    else:
        print("bravo, vous avez gagner")
        sys.exit()
        print("vous avez perdu")

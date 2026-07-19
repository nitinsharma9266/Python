import time
import os

height=15
while True:
    for i in range(height):
        print("\n" *i + "⚽")
        time.sleep(0.06)
        os.system("cls")
        
    for i in range(height,0,-1):
        print("\n" *i + "⚽")
        time.sleep(0.06)
        os.system("cls")
    
    
     
import time
from functools import lru_cache
@lru_cache(maxsize=3)

def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("working something ...")
    (some_work(3))
    print("Done...calling again")
    (some_work(3))
    print("calling again..")
"""
Is program me @lru_cache(maxsize=3)
ka use hua hai jo ek cache banata hai. Jab some_work(n) function 
pehli baar call hota hai to wo time.sleep(n) ke wajah se wait karta 
hai aur result cache me store kar deta hai. Jab same value ke saath function ko 
dobara call karte ho, to Python result ko direct cache se de deta hai bina time waste kiye.
Isliye pehli baar call karne me time lagta hai, lekin dusri baar wahi 
input dene par instantly output milta hai.
"""
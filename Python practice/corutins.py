
def some():
    import time
    time.sleep(5)
    book = "Akshay dhumda is good boy (for some one person special)"

    while True:
       text = (yield)
       if text in book:
           print("your text in book ")
       else:
          print("your text not in book")

serach = some()
next(serach)
serach.send("Akshay")
input("press any key : ")
serach.send("yash")

serach.close() #ye serch ko close karega
"""
Is program me some() ek coroutine hai jo ek book string ke andar text search karta hai.
Jab coroutine start hota hai (next(serach)), to wo yield tak ruk jata hai. Uske baad jab tum serach.
send("Akshay") bhejte ho, tab coroutine resume hota hai aur check karta hai ki "Akshay" book me hai ya nahi.
Agar text mil gaya to "your text in book" print karega, warna "your text not in book".
Ye coroutine hamesha active rehta hai (while True ke wajah se) 
aur har baar naya text receive karke search karta hai bina dobara start kiye.
"""
"""
itrable    :  __iter__() or __getitem__()
itretor    :  __next__()
iteration  : iterator karne ke method ko iteration kahte hai

yeild      :  ye ek genrator hai jo number ko genrate karta hai
"""

# def gen (n):
#     for i in range(n):
#         yield i
#
# g = gen(10)
# print(g)

print("fibonacci series - ")
limit = int(input("Enter number: "))
def gen(limit):
    a,b = 0,1
    while(a<=limit):
        yield a
        a,b = b,a+b

g = gen(limit)
for i in g:
    print(i)


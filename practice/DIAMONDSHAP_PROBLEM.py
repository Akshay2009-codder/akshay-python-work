
"""
ye jo diamond problem hai vo python me to nahi par another languge me jyada aaati hai jisme
jab multiple enheritance me languge ko pata nahi chalega ki konsa pahke access karna hai or konsa baad me
isi confuceon ko diamond shap problem kahete hain

"""

class A:
    def mat(self):
        print("I am a class method in class A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

d.mat()




student = int(input("Enter number of students: "))
apples = int(input("Enter number of apples: "))

if apples % student == 0:
    print(f"All students have {apples // student} apples each")
else:
    extra = apples % student
    need = student - extra

    if extra <= need:
        if 1 <= extra <= 10:
            print(f"{extra} apples wapas le lo.")
        else:
            print("Zyada extra apples hain, adjust karna mushkil hai.")
    else:
        if 1 <= need <= 10:
            print(f"{need} apples aur do taaki sabko equal mile.")
        else:
            print("Zyada apples ki jarurat hai, adjust karna mushkil hai.")

import os

def solder(path, formate):
    os.chdir(path)
    i = 1
    files = os.listdir(path)

    for file in files:
        if os.path.isfile(file):
            new_name = file.capitalize()
            if file != new_name:
                os.rename(file, new_name)
                file = new_name
            if os.path.splitext(file)[1].lower() == formate.lower():
                new_file_name = f"{i}.{formate}"
                os.rename(file, new_file_name)
                i += 1

solder(r"C:\Users\hp\OneDrive\Desktop\testing python code", ".txt")

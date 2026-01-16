def readfile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {filename} not found")

readfile("file1.txt")
readfile("file2.txt")
readfile("file3.txt")

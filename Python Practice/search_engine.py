data = [
    "Python is a high-level programming language.",
    "It was created by Guido van Rossum in 1991.",
    "Python is widely used in web development.",
    "Django and Flask are popular Python web frameworks.",
    "Python supports object-oriented programming.",
    "NumPy is a library for numerical computing in Python.",
    "Pandas is used for data analysis and manipulation.",
    "Matplotlib is used for data visualization in Python.",
    "Seaborn provides high-level interface for visualization.",
    "Scikit-learn is used for machine learning in Python.",
    "TensorFlow is a deep learning framework in Python.",
    "PyTorch is also popular for deep learning research.",
    "BeautifulSoup is used for web scraping in Python.",
    "Requests library is used to send HTTP requests.",
    "Python has a large standard library.",
    "OS module is used for interacting with the operating system.",
    "Sys module provides system-specific functions.",
    "JSON module is used for working with JSON data.",
    "SQLite3 library is used for database management.",
    "Tkinter is used for GUI applications in Python.",
    "PyGame is used for making 2D games in Python.",
    "Logging module helps in application debugging.",
    "Regular Expressions in Python are handled by re module.",
    "Datetime module helps in working with dates and times.",
    "Multiprocessing library is used for parallel processing.",
    "Threading module is used for multithreading in Python.",
    "Python is popular for Artificial Intelligence applications.",
    "Python is widely used in Automation and Scripting.",
    "Python Package Index (PyPI) hosts thousands of libraries.",
    "Python is an interpreted and dynamically typed language.",
    "Python is easy to learn due to its simple syntax.",
    "Python supports multiple programming paradigms.",
    "Machine Learning with Python is widely adopted.",
    "Data Science relies heavily on Python libraries.",
    "Python is cross-platform and runs on Windows, Linux, and Mac.",
]

serch = input("anything about python serch here : ")

found = False
for line in data:
    if serch.upper() in line.upper():
        print(line)
        found = True

if not found:
    print("no result found about", serch)
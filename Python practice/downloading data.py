import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)

if response.status_code == 200:
    data = response.text

    with open("iris_data.txt", "w") as f:
      f.write(data)
    print("database successfuly saved in iris_data.txt")
else:
    print("database failed to saved in iris_data.txt")

fileopen = open("iris_data.txt","r")

data_list = []
for line in fileopen:
    data_list.append(line.strip())
fileopen.close()

fileobj = open("pickling_data","wb")
pickle.dump(data_list,fileobj)
fileobj.close()


filename = "pickling_data"
openingfile = open(filename,"rb")
readingfile = pickle.load(openingfile)
print(readingfile)
openingfile.close()

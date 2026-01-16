user_list = [3,50,4,78,67]
pelindrom_list = []
for user in user_list:
    if user <= 10:
        pelindrom_list.append(user)
    else:
        for i in range (user,user+1000):
            if str(i) == str(i)[::-1]:
                pelindrom_list.append(i)
                break

print(pelindrom_list)
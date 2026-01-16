sample_list = ["Bike","Cycle","Motorcycle"]

for sample in sample_list:
    if sample != "Motorcycle":
        print(sample,"And ", end=" ")
    else:
        print(sample)

# itni line ka code using samplefunction

print("=" * 44)

print(" And ".join(sample_list))
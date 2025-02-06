#Weight loss
monthly_weight_decrease = 1.5
months_quantity = 6
total_loss = 0

weight = float(input("Enter users weight: "))
print("Month\tWeight")
print("==============")
for i in range(1, months_quantity+1):
    print(i, weight, sep = "\t")
    weight -= monthly_weight_decrease
    if i < months_quantity:
        total_loss +=monthly_weight_decrease

print("==============")
print("Total loss:", total_loss)
    
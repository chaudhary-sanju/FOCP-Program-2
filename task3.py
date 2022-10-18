total_std = int(input("How many students? "))
size = int(input("Required group size? "))
group = int(total_std / size)
left_over = total_std % size
print(f"There will be {group} groups with {left_over} student left over")
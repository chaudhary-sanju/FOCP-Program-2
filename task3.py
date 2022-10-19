def group_division():
    total_std = int(input("How many students? "))
    size = int(input("Required group size? "))
    group = int(total_std / size)
    left_over = total_std % size
    return(f"There will be {group} groups with {left_over} student left over")

print(group_division())
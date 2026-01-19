total_books= int(input("Enter number of books purchased this month: "))
total_points=0

if total_books >= 8:
    total_points+= 60 * (total_books//8)
    total_books= total_books % 8
if total_books >= 6:
    total_points+= 30 * (total_books//6)
    total_books= total_books % 6
if total_books >=4:
    total_points+= 15 * (total_books//4)
    total_books= total_books % 4
if total_books >=2:
    total_points+= 5 * (total_books//2)
    total_books= total_books % 2
print(f"Total reward points earned this month: {total_points}")
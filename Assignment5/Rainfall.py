month = {'1':'January',
		'2':'February',
		'3':'March',
		'4':'April',
		'5':'May',
		'6':'June',
		'7':'July',
		'8':'August',
		'9':'September',
		'10':'October',
		'11':'November',
		'12':'December'	}

total_rainfall=0.0
total_months=0
total_years= int(input("Enter number of years: "))
for year in range(total_years):
      for i in month:
        rainfall = float(input(f"Enter rainfall for {month[i]} for year {year+1}: "))
        total_rainfall += rainfall
        total_months += 1

average_rainfall = total_rainfall / total_months
print(f"\nNumber of months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f}")

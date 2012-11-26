days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sundays = 0
week_day = 2
for i,j in [(i,j) for i in range(1901, 2001) for j in range(1, 13)]:		
	if j == 2:		
		if i % 4 == 0 and i % 100 != 0:
			week_day = (week_day + (days[j-1] + 1) % 7) % 7
		elif i % 4 == 0 and i % 100 == 0 and i % 400 == 0:
			week_day = (week_day + (days[j-1] + 1) % 7) % 7
		else:
			week_day = (week_day + days[j-1] % 7) % 7
			
	else:
		week_day = (week_day + days[j-1] % 7) % 7

	if week_day == 6: 
		sundays += 1		

print sundays

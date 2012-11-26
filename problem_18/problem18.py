rows = []
with open('data.txt', 'r') as f:
	rows = [[int(x) for x in line.split()] for line in f]

for i,j in [(i,j) for i in range(len(rows)-2,-1,-1) for j in range(i+1)]:	
	rows[i][j] +=  max([rows[i+1][j],rows[i+1][j+1]])
 

print "%s " % (rows[0][0])

def getConcatenation (concatList):
     
    reportList = ""
    for i in range(0,len(concatList)):
     	if i < len(concatList) - 1:
     		reportList += concatList[i] + ', '
     	elif i == len(concatList) - 1:		
     		reportList += 'and ' + concatList[i] + '.'
    return reportList


def getPicture (concatList):
	for i in range(0,len(concatList)):
		newrow = ''
		for j in range(0,len(concatList[i])):
			newrow += concatList[i][j]
		print(newrow)

vegetables = ['carrot', 'lettuce', 'onion', 'radish']

print(getConcatenation(vegetables))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

getPicture(grid)

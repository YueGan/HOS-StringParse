with open('GameStrings.txt') as inputf:
    lines = inputf.readlines()
    
nameDict = {}

for line in lines:
    if line.startswith('Hero/Name/'):
        
        heroString = 'name:' + line.split('/')[2].split('=')[1].strip('\n')
        nameDict[line.split('/')[2].split('=')[0]] = [heroString]
        

for line in lines:
    
    if line.startswith('Hero/Description/'):
        for element in nameDict:
            if line.split('/')[2].split('=')[0] == element:
                temp = nameDict[element]
                descString = 'description:' + line.split('/')[2].split('=')[1].strip('\n')
                temp.append(descString)
                nameDict[element] = temp
    
    if line.startswith('Hero/Info/'):
        for element in nameDict:
            if line.split('/')[2].split('=')[0] == element:
                temp = nameDict[element]
                descString = 'info:' + line.split('/')[2].split('=')[1].strip('\n')
                temp.append(descString)
                nameDict[element] = temp                
    
    if line.startswith('Hero/Title/'):
        for element in nameDict:
            if line.split('/')[2].split('=')[0] == element:
                temp = nameDict[element]
                descString = 'title:' + line.split('/')[2].split('=')[1].strip('\n')
                temp.append(descString)
                nameDict[element] = temp                
                
print(nameDict)
outputf = open('HeroInfo.xml', 'w')

for element in nameDict:
    if len(nameDict[element]) == 4:
        for line in nameDict[element]:
            temp = line.split(':')
            tempString = '<' + temp[0] + '>' + temp[1] + '</' + temp[0] + '>\n'
            outputf.write(tempString)

outputf.close()
inputf.close()
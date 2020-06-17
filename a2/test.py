def sorting(file):
    """Input a is the file consists of all random words, output is a list of sorted words."""
    f= open (file)
    line = [] #list of all line in file
    for i in f:
        line.append(i)
    words = [] #list of all words in file
    for i in line:
        i=i.strip()
        temp = i.split(" ")
        for j in temp:
            if j.upper() not in words:
                words.append(j.upper())
    words.sort()
    return (words)
def hyphen(li):
    """Take a list of word as input, sorting all the words with illegal punctuation and output would be an acceptable list of words. """
    for i in li:
        for j in range(0,len(i)):
            if i[j].isalpha() != True and j == len(i)-1:
                li.remove(i)
            if j != len(i)-1 and i[j] == '-':
                if i[j+1] == '-':
                    li.remove(i)
    return(li)
def removal(file,li):
    """Take input of a file consists of all words that need to be removed and a list of all sorted words, output is a list of all acceptable words."""
    f=open(file)
    line = [] #list of all lines in file
    for i in f:
        line.append(i)
    words = [] #list of all words that are not needed
    for i in line:
        i=i.strip()
        temp = i.split(" ")
        for j in temp:
            if j.upper() not in words:
                words.append(j.upper())
    for i in li:
        if i in words:
            li.remove(i)
        if i == "":
            li.remove(i)
    for i in li:
        if i in words:
            li.remove(i)
        if i == "":
            li.remove(i)
    for i in li:
        if i in words:
            li.remove(i)
        if i == "":
            li.remove(i)
    for i in li:
        if i in words:
            li.remove(i)
        if i == "":
            li.remove(i)
    li.sort()
    return(li)
def printing(li,file,comparelist):
    """Take a list of all acceptable words and their origin file as input, output is the alphabetically sorted words with its reference. """
    f= open (file)
    line = [] #list of all line in file
    for i in f:
        line.append(i)
    countprint = 0 #count the number of lines that are printed
    countchar=0
    for i in li:
        if len(i) >= countchar:
            countchar = len(i) #finding the longest word to allign
    for i in li:
        for j in range (0,len(line)):
            countline = 0 #number of that word in this specific line
            l = line[j]
            stripl=l.strip()
            w1 = stripl.split(' ')
            w2 =[]
            for k in w1:
                word = k.upper()
                w2.append(word)
            if i in w2:
                while i in w2:
                    countline += 1
                    w2.remove(i)
            if countline > 0:
                countprint += 1
                print(i.ljust(countchar + 2,' '), end ='')
                print(stripl, end =' ')
                if countline == 1:
                    print("({})".format(j+1))
                else:
                    j=str(j+1)+'*'
                    print("({})".format(j))
                print('compare with:')
                print(comparelist[countprint-1])
                if comparelist[countprint - 1] == comparelist[len(comparelist)-1]:
                    print ('full')
def compare(file):
    """Compare the output of this code to the accepted answer, return the list of all lines in the output.txt file"""
    f=open(file)
    line = [] #list of all line in file
    for i in f:
        line.append(i)
    return(line)
def final(commandlist):
    """Take the command list as an input and output would be correspond to the list."""
    if '-e' in commandlist:
        if commandlist[0] == '-e':
            print('I am so mad I get fatter and turn purple')
            return
        else:
            file1 = commandlist[0]
            Step1 = sorting(file1)
            file2 = commandlist[2]
            Step2 = hyphen(Step1)
            Step3 = (removal(file2,Step2))
            file3 = compare(commandlist[3])
            finalstep = printing(Step3,file1,file3)
commandlist2 = ['in02.txt','-e','english.txt','out02.txt']
commandlist3 = ['in03.txt','-e','english.txt','out03.txt']
commandlist4 = ['in04.txt','-e','english.txt','out04.txt']
commandlist5 = ['in05.txt','-e','english.txt','out05.txt']
commandlist6 = ['in06.txt','-e','english.txt','out06.txt']
commandlist7 = ['in07.txt','-e','english.txt','out07.txt']
commandlist8 = ['in08.txt','-e','latin.txt','out08.txt']
commandlist9 = ['in09.txt','-e','latin.txt','out09.txt']
commandlist10 = ['in10.txt','-e','english.txt','out10.txt']
commandlist11 = ['in11.txt','-e','english.txt','out11.txt']
commandlist12 = ['in12.txt','-e','english-2.txt','out12.txt']
commandlist13 = ['in13.txt','-e','english-2.txt','out13.txt']
commandlist14 = ['in14.txt','-e','english-2.txt','out14.txt']
commandlist15 = ['in15.txt','-e','latin.txt','out15.txt']
commandlist16 = ['in16.txt','-e','latin.txt','out16.txt']
commandlist17 = ['in17.txt','-e','latin-2.txt','out17.txt']
commandlist18 = ['in18.txt','-e','latin-2.txt','out18.txt']
commandlist19 = ['in19.txt','-e','deutsch-2.txt','out19.txt']
commandlist20 = ['in20.txt','-e','deutsch-2.txt','out20.txt']
final(commandlist20)

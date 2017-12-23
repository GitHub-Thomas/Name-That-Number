"""
ID:wzch_di3
TASK:namenum
LANG:PYTHON3
"""
dictionary = open("dict.txt","r")
phone = {"2":"ABC","3":"DEF","4":"GHI","5":"JKL",
         "6":"MNO","7":"PRS","8":"TUV","9":"WXY"}
fin = open("namenum.in","r")
fout = open("namenum.out","w")
numbers = fin.read()
number = numbers[0:len(numbers)-1]
names = []
def getname(number,n,result):
    if (n >= len(number)):
        names.append(result)
        return()
    for i in range(0,3):
        result1 = result + phone[number[n]][i]
        getname(number,n+1,result1)
getname(number,0,"")
flag = 0
for name in dictionary.readlines():
    if (len(numbers) != len(name)):
        continue
    name1 = name[0:len(name)-1]
    if name1 in names:
        flag = 1
        fout.write(name1+"\n")
if (flag == 0):
    fout.write("NONE\n")
dictionary.close()
fin.close()
fout.close()

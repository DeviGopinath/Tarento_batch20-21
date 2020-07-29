#- Accept a String input
#- Accept a search String to search in the above input
#- Verify if the search String is present in the input string and the position and number of occurrences


def findall(s,ss):         #funtion for finding position
    a=[]
    l = len(s)
    index = 0
    while index < l:
        i = s.find(ss, index)
        if i == -1:
            return a
        a.append(i+1)
        index = i + 1
    return a               #returns a list of positions
s=input("String: ")
ss=input("String to be searched: ")
count=s.count(ss)
print("Occurrences- ",count)
a=[]
l=len(s)
index = 0
x=findall(s,ss)
print("Position- ",end='')
if x:
	for i in range (len(x)-1):
		print(str(x[i])+',',end='')
	print(x[len(x)-1])s
else:
	print('Not Found')
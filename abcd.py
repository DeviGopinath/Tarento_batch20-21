#Given four strings A, B, C, D, write a program to check if D is an interleaving of A, B 
#and C. D is said to be an interleaving of A, B and C, if it contains all characters of A, B, C and the order of all 
#characters in individual strings can be changed.


import itertools
x=[]
z=dict()
y=['A','B','C'] #list of values for the dictionary
A=x.append(input("A :"))
B=x.append(input("B :"))
C=x.append(input("C :")) #add a b c to list
D=input("D :")
for i,j in zip(itertools.permutations(x,3),itertools.permutations(y,3)):  # permute all possible combinations of A B C with its keys
    v=''.join(j)   #join values as tuples
    k=''.join(i)
    z[k]=v # map short form as key to long as value
 
# print value if it exists
try:
    print("D =",z[D])
except:
    print("No combination possible")    
 
    

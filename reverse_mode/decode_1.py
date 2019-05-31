##Reverse mode                        

##Test - 1
#Input: pglnhenftjdscs pmdchawvngmckde
#Output: lets dance

##Test - 2
#Input: mpndsi5fcdse8r mvljhedsgvcwwdo7frvqk
#Output: nice legwork

##Code_solution

s = input()
ss=""
for i in range(0,len(s)):
    if (i+1)%3==0:
        ss+=s[i]
print(ss)

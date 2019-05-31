
##Reverse mode                        Output

## 12                                 Hello world!
## 48 65 6C 6F 20 77 6F 72 6C 64 21
## code solution
vc = int(input())
s=""
for v in input().split():
    s+=chr(int(v,16))
print(s)

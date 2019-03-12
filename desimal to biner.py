from modulStack import*
n=int(input('masukkan angka: '))
x=n
stack=[]
while (n>0):
    a=int(float(n%2))
    stack.append(a)
    n=(n-a)/2
stack.append(0)
string=""
for j in stack[::-1]:
    string=string+str(j)
print('Biner untuk %d adalah %s'%(x, string))

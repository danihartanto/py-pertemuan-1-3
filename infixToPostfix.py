from modulStack import*
def cek(x):
    s=stack()
    for i in x:
        if i=="(" or i=="[" or i=="{":
            push (s,i)
        elif i==")" or i=="]" or i=="}" :
            if isEmpty(s):
                return "kurang kurung buka atau kelebihan kurung tutup"
            else :
                    pop(s)
    if isEmpty(s):
        return True
    else:
        return "kelebihan kurung buka atau kekurangan kurung tutup"
def intopost(x):
    misal={}
    misal['*']=3
    misal['/']=3
    misal['+']=2
    misal['-']=2
    misal['(']=1
    misal['[']=1
    misal['{']=1
    misal[')']=1
    misal[']']=1
    misal['}']=1
    s=stack()
    postlist=[]
    for i in x:
        if i in '0123456789' or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            postlist.append(i)
        elif i =='(' or i=="[" or i=="{":
            push(s,i)
        elif i==")" or i=="]" or i=="}":
            temp=s.pop()
            while temp!='(' and temp!="[" and temp!="{":
                postlist.append(temp)
                temp=s.pop()
        else:
            while(not isEmpty(s))and(misal[peek(s)]>= misal[i]):
                postlist.append(s.pop())
            push(s,i)
    while not isEmpty(s):
        postlist.append(s.pop())
    return ''.join(postlist)

y=input('masukkan string operasi aritmatika=')
a=cek(y)
print ("cek infix: ",a)
if a==True:
    print ('infix=',y)
b=intopost(y)
print ('postfix=',b)

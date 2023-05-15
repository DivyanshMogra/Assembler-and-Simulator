
import sys
dict=['add','10000','sub','10001','mul','10110','xor','11010','or','11011','and','11100','R1','001','R2','010','R3','011','R0','000','R4','100','R5','101','R6','110']

dict3=['ld','10100','001','st','10110','R1','001','R2','010','R3','011','R0','000','R4','100','R5','101','R6','110']

dict5=['jmp','11111','jlt','01100','jgt','01101','je','01111']
#f = open("cc.txt", "r")
l = []
dict4=['R1','001','R2','010','R3','011','R0','000','R4','100','R5','101','R6','110','mov','10010','ls','110001','rs','11000']
f=open("input.txt")
f1=f.readlines()
for i in f1:
    lk=i.rstrip().split()
    l.append(lk)
dict2=['mov','10011','div','10111','not','11101','cmp','11110','R1','001','R2','010','R3','011','R0','000','R4','100','R5','101','R6','110','FLAGS','111']
f.close()
o=[]
pp=[]
k=[]

uu=0
ee=0
i=0
llen=len(l)
while(i<llen):
    if l[i][0]=="var":
        kq=l[i][1]
        pp.append(kq)
        pp.append(i)
        ee=ee+1
        i+=1
    else:
        i+=1
        break
binary=[]
err=0
output_error=''
i=ee
lllen=len(l)
while(i>=ee and i<lllen):
    if l[i][0]!="var":
        p = l[i][0]
        if p[-1] == ':':
            p=p[:len(p)-1]
            o.append(p)
            o.append(uu)
            l[i].pop(0)
        uu=uu+1
    i+=1
l=list(filter(None,l))
for i in range(ee,len(l)):
    checkvar=l[i][0]
    if checkvar=="hlt":
        pass
    elif checkvar=="var":
        output_error+="Error at line" + str(i + 1) + " variable declared in between "+'\n'
        err=1



    elif checkvar in dict:
        p = str()
        flag = 0
        llenl=len(l[i])
        if llenl==4:
            j=0
            while(j<len(l[i])):
                rw=l[i][j]
                if rw in dict:
                    ind = dict.index(l[i][j])
                    p = p + dict[ind + 1]
                    j+=1
                    if flag == 0:
                        p = p + '00'
                    flag = 1
                else:
                    j+=1
                    output_error+="Error at line" + str(i + 1) + " wrong register value "+'\n'
                    err=1
            binary.append(p)
            p=""
        else:
            output_error+="Error at line"+str(i+1)+"Incomplete command or register missing"+'\n'
            err=1

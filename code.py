
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
    elif checkvar in dict4 and "$" in l[i][2]:
        klen=len(l[i])
        if klen==3:
            p = str()
            j=0
            while(j< klen-1):
                if l[i][j] in dict4:
                    ind = dict4.index(l[i][j])
                    j+=1
                    p = p + dict4[ind + 1]
                else:
                    j+=1
                    output_error+="Error at line" + str(i + 1) + "  wrong register value  "+'\n'
                    err = 1
            y=str(l[i][2])
            tt=y
            tt=tt[1:]
            tt=int(tt)
            if "$" in y and (tt <=255 and tt>=0):
                y=y[1:]
                u = bin(int(y))
                u=u[2:]
                u = str(u)
                t = 8 - len(u)
                q=0
                while(q< t):
                    u = '0' + u
                    q+=1
                p = p + u
                binary.append(p)
                p = ""
            else:
                output_error+="Error at line" + str(i + 1) + " IMM not in range or invalid imm syntax "+'\n'
                err=1
        else:
            output_error+="Error at line" + str(i + 1) + " Incomplete command or register missing "+'\n'
            err=1
    elif checkvar in dict2:
        klen=len(l[i])
        if klen==3:
            p = str()
            flag = 0
            j=0
            while(j<len(l[i])):
                rw=l[i][j]
                if rw in dict2:
                    val1=2
                    #print(rw,dict2)
                    ind = dict2.index(l[i][j])
                    p = p + dict2[ind + 1]
                    j+=1
                    if flag == 0:
                        p = p + '00000'
                    flag = 1
                else:
                    j+=1
                    output_error+="Error at line" + str(i + 1) + " wrong register value "+'\n'
                    err=1
            binary.append(p)
            p=""
        else:
            output_error+="Error at line" + str(i + 1) + " Incomplete command or register missing "+'\n'
            err = 1
        if l[i][2]=='FLAGS' and checkvar!='mov':
            output_error+="Error at line" + str(i + 1) + " Flag command can only be used with mov command "+'\n'
            err = 1
    
    elif checkvar in dict3:
        klen=len(l[i])
        if klen==3:
            if l[i][2] in pp:
                p = str()
                flag = 0
                j=0
                while(j<len(l[i])-1):
                    rw=l[i][j]
                    if rw in dict3:
                        ind = dict3.index(rw)
                        j+=1
                        p = p + dict3[ind + 1]
                    else:
                        j+=1
                        output_error+="Error at line" + str(i + 1) + " wrong register value "+'\n'
                        err=1
                v=pp.index(l[i][2])
                qw=v+1
                v=pp[qw]

                u = bin(i-ee+1)
                u=u[2:]
                u = str(u)
                t = 8 - len(u)
                a=0
                while(a< t):
                    u = '0' + u
                    a+=1
                p = p + u
            else:
                output_error+="Error at line" + str(i + 1) + " variable not declared  "+'\n'
                err=1
                
    elif checkvar in dict5:
        klen=len(l[i])
        if klen==2:
            if l[i][1] not in o:
                output_error+="Error at line" + str(i + 1) + " label not declared "+'\n'
                err=1
            else:
                p=''
                ind = dict5.index(checkvar)
                sq='000'
                p=p+dict5[ind + 1]
                p=p+sq
                ind=o.index(l[i][1])
                qww=ind+1
                u=o[qww]

                u = bin(u)
                u=u[2:]
                t = 8 - len(u)
                a=0
                while(a< t):
                    u = '0' + u
                    a+=1
                p=p+u
                binary.append(p)
                p = ""

        else:
            output_error+="Error at line"+str(i+1)+" Invalid syntax "+'\n'
            err=1
    else:
        output_error+="Error at line" + str(i + 1) + " Incomplete command or register missing "+'\n'
        err = 1
i=0
klen=len(l)-1
while(i<klen):
    if l[i][0]=="hlt":
        
        output_error+="Error at line"+str(i+1)+" hlt cmmnd cannot be used in between"+'\n'
        err=1
    i+=1
if l[len(l)-1][0]!="hlt":
    output_error+="Error at line" + str(len(l)) + " hlt cmmnd was no used in end"+'\n'
    err=1
if err==0:
    f=open('output.txt','w')
    s=''
    for i in binary:
        s+=i+'\n'
    s+="0101000000000000"
    f.write(s)
    f.close()
else:
    f=open('errors.txt','w')
    f.write(output_error)
    f.close()

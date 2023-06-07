import sys
r={}
for i in range(0,7):
    k=bin(i)
    k=k[2:]
    k="{:>03}".format(k)
    # print(k)
    r[k]=0
r["111"]="0000000000000000"
def rec(i, p):


    if i[:5] == '00000':            #add
        k1= r[i[7:10]]
        k2=r[i[10:13]]
        r[i[13:16]] =k1+k2
        k1a=((2 ** 16) - 1)
        k1b=r[i[13:16]]
        if k1b> k1a:
            r["111"] = "0000000000001000"
        else:
            r["111"] = "0000000000000000"
        p += 1

    if i[:5] == '00001':            #Sub
        k1= r[i[7:10]]
        k2=r[i[10:13]]
        r[i[13:16]] =k1 + k2
        k1b=r[i[13:16]]
        if k1b > 0:
            r["111"] = "0000000000000000"
           
        else:
             r["111"] = "0000000000001000"
             r[i[13:16]] = 0
        p += 1
    if i[:5] == '00110':            #Mul
        k1= r[i[7:10]]
        k2=r[i[10:13]]
        r[i[13:16]] =k1 * k2
        if not (r[i[13:16]] > ((2 ** 16) - 1)):
            r["111"] = "0000000000000000"
        else:
            r["111"] = "0000000000001000"
        p+=1

    if i[:5] == '01011':            #or
        k1= r[i[7:10]]
        k2=r[i[10:13]]
        r[i[13:16]]=k1|k2
        p += 1
        r["111"] = "0000000000000000"

    if i[:5] == '01100':            #and
        k1= r[i[7:10]]
        k2=r[i[10:13]]
        r[i[13:16]] = k1&k2
        p += 1
        r["111"] = "0000000000000000"

    if i[:5] == '01000':            #rs
        a = i[5:8]
        k3=r[a]
        k4=int(i[8:16], 2)
        r[a] = k3 >> k4
        p += 1
        r["111"] = "0000000000000000"

    if i[:5] == '00010':            #mov imm
        int(i[8:16], 2)
        r[i[5:8]] = k4
        p += 1
        r["111"] = "0000000000000000"

    if i[:5] == '01001':            #ls
        a = i[5:8]
        k3=r[a]
        k4=int(i[8:16], 2)
        r[a] = k3 << k4
        p += 1
        r["111"] = "0000000000000000"



    if i[:5] == '00011':            #mov reg  
        r[i[13:16]] = r[i[10:13]]
        p += 1
        k4=r[i[13:16]]
        r["111"] = "0000000000000000"


    if i[:5] == '01110':            #cmp
        a = i[10:13]
        b = i[13:16]
        k5=r[a]
        k6=r[b]
        if (k5 == k6):
            r['111'] = "0000000000000001"
        if (k5 > k6):
            r['111'] = "0000000000000010"
        if (k5 < k6):
            r['111'] = "0000000000000100"
        p += 1
    if i[:5] == '00111':            #div
        k7=r[i[10:13]]
        k8= r[i[13:16]]
        r["000"] = k7 /k8

        p += 1
        r["111"] = "0000000000000000"

    if i[:5] == '01101':            #not
        a = i[10:13]
        b = i[13:16]
        k9=~r[b]
        r[a] = k9

        p += 1
        k9=r[a]
        q6=1
        r["111"] = "0000000000000000"


    if i[:5] == '00100':            #ld     
        a = i[5:8]
        k10=int(i[8:16], 2)
        k11=int(l[k10], 2)
        r[a] = k11
        p += 1
        r['111'] = "0000000000000000"
    if i[:5] == '11111':            #je
        k12=r["111"][15]
        if (k12 == "1"):
            p = int(i[8:16], 2)
        else:
            p += 1
        r["111"] = "0000000000000000"
    if i[:5] == '00101':            #st
        a = i[5:8]
        k12=int(i[8:16], 2)
        b = k12
        t=r[a]
        t = bin(int(t)).replace("0b", "")
        t = str(t)
        a = 16 - len(t)
        t = (a * "0") + t
        k13=t
        #print(t)
        l[b] = t
        p += 1
        r['111'] = "0000000000000000"

    if i[:5] == '01111':            #jmp        
        k14=int(i[8:16], 2)
        p = k14
        r["111"] = "0000000000000000"

    if i[:5] == '11100':            #jlt
        k15=r["111"][13]
        if (k15 == "1"):
            p = (int(i[8:16], 2))
        else:
            p += 1
        r["111"] = "0000000000000000"


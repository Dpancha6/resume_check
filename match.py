# Python3 code to select
# data from excel
import xlwings as xw
import numpy as np
import operator

print("Hello World!!")

# Specifying a sheet
ws = xw.Book("Database.xlsx").sheets['JS']
emp = xw.Book("Database.xlsx").sheets['Employee']
# Selecting data from
# a single cell
js = ws.range("B2:J6").value
# js2 = ws.range("B3:J3").value
# js3 = ws.range("B4:J4").value
# js4 = ws.range("B5:J5").value
# js5 = ws.range("B6:J6").value
#v2 = ws.range("F5").value
# print("JS:", js)
# print("JS:", js2)
# print("JS:", js3)
# print("JS:", js4)
# print("JS:", js5)
#print(v1[2])

em = emp.range("B2:H6").value
# em2 = emp.range("B3:H3").value
# em3 = emp.range("B4:H4").value
# em4 = emp.range("B5:H5").value
# em5 = emp.range("B6:H6").value

# print("EMP:", em)
# print("EMP:", em2)
# print("EMP:", em3)
# print("EMP:", em4)
# print("EMP:", em5)



# a=['d','f','t','r']
# b=['d','t','s','v']


# b.reverse()
# a.reverse()

# t= (np.intersect1d(a, b))
# points=0
# for j in t:
#     for i in range (len(a)):
#         if a[i]==j:
#             points += (i+1)*10
#         if b[i] == j:
#             points += (i+1)*10
# print(points)

# temp = []
temp1 = {}
temp2 = {}
for j in js:
    # temp.append(j[0])
    temp1[j[0]] = []
    rev_j = list(reversed(j[1:5]))
    # j[1:5].reverse()
    
    #print('j:',rev_j)
    for e in em:
        # temp2[e[0]] = []
        points = 0
        rev_e = list(reversed(e[1:5]))
        # e[1:5].reverse()
        # print('e:',rev_e)
        t = (np.intersect1d(rev_j, rev_e))
        # print('t:',t)
        for match in t:
            for i in range (len(rev_j)):
                if rev_j[i]==match:
                    points += (i)*10
                if rev_e[i] == match:
                    points += (i)*10
        
        if j[6]==e[6]:
            points+=150

        if j[7]:
            points+=(j[7]*50)

        if j[8]:
            points+=200

        # temp.append([e[0],points])
        temp1[j[0]].append([points, e[0]])
        # print('e00',e[0])

        if e[0] not in temp2:
            temp2[e[0]] = [[points, j[0]]]
        else:
            ttt=temp2[e[0]]
            ttt.append([points, j[0]])
            temp2[e[0]] = ttt


        


for key, value in temp1.items():
    value.sort(reverse=True)
    print(key,':')
    for j in value:
        print(j)
    print('')

for key, value in temp2.items():
    value.sort(reverse=True)
    print(key, ':')
    for j in value:
        print(j)
    print('')


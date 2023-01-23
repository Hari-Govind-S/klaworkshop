import re
with open('C:\\Users\\ktuser\\Downloads\\KLAWorkshop\\Milestone1\\Format_Source.txt') as f:
    lines = f.readlines()


i=0
x=[]
y=[]
for line in lines:
    if(line=="boundary\n"):
        x.append(i)
    elif(line=="endel\n"):
        y.append(i)
    i=i+1
header=lines[0:x[0]]
footer=lines[y[-1]+1:]

polygons=[]
i=0

#code for extracting the text
for poly in x:
    polygons.append(lines[poly:y[i]+1])
    i=i+1
polygonverties=[]


#code for extracting the points
for polygon in polygons:
    x=polygon[3].split(" ")
    i=4
    poly=[]
    while (i<len(x)):
        point=(int(x[i]),int(x[i+1]))
        poly.append(point)
        i = i+3
    polygonverties.append(poly)

#polygon to text
polyout=[]
for i in range(2):
    polyout=polyout+['boundary\n', 'layer 1\n', 'datatype 0\n']
    vert="xy 5 "
    for item in polygonverties[i]:
        x,y=item
        vert = vert + str(x)+ " "+str(y)+"  "
    vert=vert+"\n"
    polyout.append(vert)
    polyout=polyout+['endel\n']
    

output=header+polyout+footer
out = "".join(output)
#print(out)
with open('milestone 1.txt', 'w') as f:
    f.write(out)

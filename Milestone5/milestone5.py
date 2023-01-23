import re
def extract(path):
    with open(path) as f:
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
    
    return header,footer,polygonverties

def polyprinter(verties,printout):
    polyout=[]
    print(len(polyout))
    for i in printout:
        polyout=polyout+['boundary\n', 'layer 1\n', 'datatype 0\n']
        a=len(verties[i])
        vert="xy  "+str(a)+"  "
        for item in verties[i]:
            x,y=item
            vert = vert + str(x)+ " "+str(y)+"  "
        vert=vert+"\n"
        polyout.append(vert)
        polyout=polyout+['endel\n']
    return polyout
    
def vertixprocessor(verties):
    output=[]
    for poly in verties:
        x0,y0=poly[0]
        polygon=[]
        for x,y in poly:
            x=x-x0
            y=y-y0
            polygon.append((x,y))
        output.append(polygon)
    return output

def templateconst(template):
    path=[]
    for i in range(len(template[0])-1):
        x1,y1 = template[0][i]
        x2,y2 = template[0][i+1]
        x = x2 - x1
        y = y2 - y1
        path.append((x,y))
    temp=[]
    for i in range(len(path)):
        x=0
        y=0
        poly=[]
        poly1=[]
        poly2=[]
        poly3=[]
        polyy1=[]
        polyy=[]
        polyy2=[]
        polyy3=[]
        poly.append((x,y))
        poly1.append((y,x))
        poly2.append((-x,y))
        poly3.append((y,-x))
        polyy.append((-x,-y))
        polyy1.append((-y,-x))
        polyy2.append((x,-y))
        polyy3.append((-y,x))
        for j in range(len(path)):
            x0,y0=path[j]
            x = x + x0
            y = y + y0
            poly.append((x,y))
            poly1.append((y,x))
            polyy.append((-x,-y))
            polyy1.append((-y,-x))
            poly2.append((-x,y))
            poly3.append((y,-x))
            polyy2.append((x,-y))
            polyy3.append((-y,x))
        temp.append(poly)
        temp.append(poly1)
        temp.append(poly2)
        temp.append(poly3)
        temp.append(polyy)
        temp.append(polyy1)
        temp.append(polyy2)
        temp.append(polyy3)
        a = path[0]
        path.remove(a)
        path.append(a)
    return temp
#polygon to text
header,footer,verties = extract('C:\\Users\\ktuser\\Downloads\\KLAWorkshop\\Milestone5\\Source.txt')
headertemp,footertemp,template = extract('C:\\Users\\ktuser\\Downloads\\KLAWorkshop\\Milestone5\\POI.txt')
newpoints = vertixprocessor(verties)

temp = templateconst(template)
i = 0
printout=[]

for poly in newpoints:
    if(len(poly)==13):
        for ply in temp: 
            if(poly == ply):
                printout.append(i)
    i = i + 1

polyout = polyprinter(verties,printout)
output=header+polyout+footer
out = "".join(output)
with open('milestone 5.txt', 'w') as f:
    f.write(out)

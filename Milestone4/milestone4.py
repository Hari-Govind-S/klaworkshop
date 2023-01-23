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

        a=len(verties[i])
        vert="xy  "+str(a)+"  "
        for item in verties[i]:
            x,y=item
            vert = vert + str(x)+ " "+str(y)+"  "
        vert=vert+"\n"
        if(polyout.count(vert)==0):
            polyout=polyout+['boundary\n', 'layer 1\n', 'datatype 0\n']
            polyout.append(vert)
            polyout=polyout+['endel\n']
    return polyout
    
def vertixprocessor(verties):
    output=[]
    print(len(verties))
    for poly in verties:
        x0,y0=poly[0]
        polygon=[]
        for x,y in poly:
            x=x-x0
            y=y-y0
            polygon.append((x,y))
        output.append(polygon)
    return output

def templateconst(templa):
    path=[]
    for i in range(len(templa)-1):
        x1,y1 = templa[i]
        x2,y2 = templa[i+1]
        x = x2 - x1
        y = y2 - y1
        path.append((x,y))
    temp=[]
    for i in range(len(path)):
        x=0
        y=0
        poly=[]


        poly.append((x,y))


        for j in range(len(path)):
            x0,y0=path[j]
            x = x + x0
            y = y + y0
            poly.append((x,y))


        temp.append(poly)


        a = path[0]
        path.remove(a)
        path.append(a)
    return temp

def polytorect(template):
    dim=[]
    for temp in  template:
        x0,y0=temp[0]
        x1,y1=temp[1]
        x2,y2=temp[2]
        if(x1-x0!=0):
            l=abs(x1-x0)
            b=abs(y2-y1)
        else:
            l=abs(y1-y0)
            b=abs(x2-x1)
        dim.append((l,b))
    return dim

def contain(x,y,poly):
    j=1
    for i in range(len(poly)-1):
        x0,y0=poly[i]
        x1,y1=poly[i+1]
        k = (x1-x0)*(y-y0) - (y1-y0)*(x-x0)
        if(k<0):
            j=0
    return j

def compare(verties, temp):
    printout=[]
    for vertix in verties:
        for i in range(len(vertix)):
            x0,y0=vertix[0]
            newview=[]
            for x,y in vertix:
                x = x-x0
                y = y-y0
                newview.append((x,y))

            for template in temp:
                j = 1
                for x,y in template:
                    k = contain(x,y,newview)
                    if(k==0):
                        j = 0
                if (j == 1):
                    printout.append(template)
            a=vertix[i]
            vertix.remove(a)
            vertix.append(a)
    return printout

#polygon to text
header,footer,verties = extract('C:\\Users\\ktuser\\Downloads\\KLAWorkshop\\Milestone4\\Source.txt')
headertemp,footertemp,template = extract('C:\\Users\\ktuser\\Downloads\\KLAWorkshop\\Milestone4\\POI.txt')
newpoints = vertixprocessor(verties)
temp = vertixprocessor(template)
print(len(newpoints))

temp=[]
tempa=[]
for templa in template:
   tempa = tempa + templateconst(templa)
for item in tempa:
    if(temp.count(item)==0):
        temp.append(item)
printout=[]
i = 0

i = 0 
for poly in newpoints:
    for ply in temp:     
        if(poly == ply and len(poly)!=13):
            print(poly)
            printout.append(i)
            break
    i = i + 1

printer=[]
for i in printout:
    if(printer.count(i)==0):
        printer.append(i)
#printout=compare(verties[0:1000],temp)
i = 0 
polyout = polyprinter(verties,printer)
output=header+polyout+footer
out = "".join(output)
with open('milestone 4.txt', 'w') as f:
    f.write(out)

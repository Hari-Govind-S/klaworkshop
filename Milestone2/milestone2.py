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
            polycode=x[:4]
            point=(int(x[i]),int(x[i+1]))
            poly.append(point)
            i = i+3
        polygonverties.append(poly)
    
    return header,footer,polygonverties,polycode

def polyprinter(verties,printout,vertn):
    polyout=[]
    for i in printout:
        polyout=polyout+['boundary\n', 'layer 1\n', 'datatype 0\n']
        vert=vertn
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

#polygon to text
header,footer,verties,polycode = extract('C:\\Users\\ktuser\\Downloads\\KLAWorkshop\\Milestone2\\Source.txt')
headertemp,footertemp,template,polycode = extract('C:\\Users\\ktuser\\Downloads\\KLAWorkshop\\Milestone2\\POI.txt')
newpoints = vertixprocessor(verties)
newtemplate = vertixprocessor(template)
i = 0
printout=[]
for poly in newpoints:
    if(poly == newtemplate[0]):
        printout.append(i)
    i = i + 1
   
vert=" ".join(polycode)
print(vert)
polyout = polyprinter(verties,printout,vert)
output=header+polyout+footer
out = "".join(output)
#print(out)
with open('milestone 2.txt', 'w') as f:
    f.write(out)

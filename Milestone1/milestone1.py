import re
with open('C:\\Users\\ktuser\\Downloads\\KLAWorkshop\\Format_Source.txt') as f:
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
footer=lines[y[-1]:]

polygons=[]
i=0
for poly in x:
    polygons.append(lines[poly:y[i]+1])
    i=i+1
output=header+polygons[0]+polygons[1]+footer
out = "".join(output)
print(out)
with open('output.txt', 'w') as f:
    f.write(out)

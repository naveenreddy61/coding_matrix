# -*- coding: utf-8 -*-
"""
Created on Fri May 17 08:41:12 2019

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:24:03 2019
@author: naveenpc
"""
from plotting import plot
import image
import math
S={2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j}
#_plot(S,4)
#print(abs(3+4j))
#print((3+4j).conjugate())
#_plot(set(z+1+2j for z in S)|set(z*(0.5j) for z in S)|set((z*(0.5j))+2-1j for z in S),5)
#_plot([z for z in S],5)
img_data = image.file2image(r"C:\Users\admin\coding_matrix\img01.png")
width = len(img_data[0])
height=len(img_data)
intensity = 100
#_plot([])
pts=list(complex(w,height-h) for (h,row) in list(enumerate(img_data)) for (w,p) in list(enumerate(row)) if p[0]<intensity)
#_plot(pts,200)
#n=80
#w=pow(math.e,complex(0,((2*math.pi)/n)))
#nthpow = list(pow(w,i) for i in range(n))
#_plot(nthpow,2)
#z0=complex(sum([z.real for z in pts])/len(pts),sum([z.imag for z in pts])/len(pts))
#plot(list(z-z0 for z in pts),170)
#_plot(list(z*pow(math.e,complex(0,math.pi/4)) for z in S),5)
#_plot(list(z*pow(math.e,complex(0,math.pi/4)) for z in pts),200)
z1=complex((max([z.real for z in S])+min([z.real for z in S]))/2,(max([z.imag for z in S])+min([z.imag for z in S]))/2)
#plot(list(z-z1 for z in S),3)
z2=complex((max([z.real for z in pts])+min([z.real for z in pts]))/2,(max([z.imag for z in pts])+min([z.imag for z in pts]))/2)
#plot(list(z-z2 for z in pts),170)
plot(list(((z-z2)*pow(math.e,complex(0,math.pi/4)))/2 for z in pts),160)
#print z1
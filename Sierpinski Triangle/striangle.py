import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig=plt.figure()
ax=plt.subplot(111)

level = 8
pt1=[0.0,0.0]
pt2=[1.0,0.0]
pt3=[0.5,0.86]

def draw_striangle(fig,level,a,b,c): #axis canvas, level, a(left),b(right),c(top)
    if (level==1):
        ax.add_patch(Polygon([a,b,c],fill=False,closed=True,color='b'))
    else:
        pt4 = [(a[0]+b[0])/2,(a[1]+b[1])/2] #midpt of base
        pt5 = [(b[0]+c[0])/2,(b[1]+c[1])/2] #midpt of right side
        pt6 = [(a[0]+c[0])/2,(a[1]+c[1])/2] #midpt of left side
        
        draw_striangle(fig,level -1,a,pt4,pt6)
        draw_striangle(fig,level -1,pt4,b,pt5)
        draw_striangle(fig,level -1,pt6,pt5,c)
    
draw_striangle (fig,level,pt1,pt2,pt3)
plt.show()

)
    if (level==1):
        ax.add_patch(Polygon([a,b,c],fill=False,closed=True,color='b'))
    else:
        pt4 = [(a[0]+b[0])/2,(a[1]+b[1])/2] #midpt of base
        pt5 = [(b[0]+c[0])/2,(b[1]+c[1])/2] #midpt of right side
        pt6 = [(a[0]+c[0
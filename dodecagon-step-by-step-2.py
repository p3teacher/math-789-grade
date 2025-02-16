# 探究正十二邊形
# dodecagon-step-by-step-2
# 2024-06-16
import numpy as np #導入
import matplotlib.pyplot as plt
from shapely import affinity
from shapely.geometry import LineString
#
def motif_line(LS, MYcolor, ZORDER, LINEWIDTH) :
    #
    xs, ys = LS.xy
    ax.plot(xs, ys, color=MYcolor, alpha=1.0, linewidth=LINEWIDTH, solid_capstyle='round', zorder=ZORDER)
    return
#
r1 = 10
d0 = r1
d1 = r1*np.cos(np.pi/12)
d2 = r1*np.sin(np.pi/12)
tx = (d1+d2)
ty = (d1-d2)
#
plt.ion()
fig = plt.figure(figsize=(5*0.8,6*0.8))
ax = fig.add_subplot(1, 1, 1)
ax.set_axis_on()
# ax.set_axis_off()
#
plt.xlim(-2*tx, 2*tx)    # 設定X軸的顯示範圍, from xmin to xmax
plt.ylim(-4*ty, 4*ty)    # 設定Y軸的顯示範圍, from ymin to ymax
#
xvalues = [-2*tx,-1*tx,0,1*tx,2*tx]
yvalues = [-4*ty,-3*ty,-2*ty,-1*ty,0,1*ty,2*ty,3*ty,4*ty]
x_ticks = ['-2tx', '-1tx', '0tx', '1tx', '2tx']
y_ticks = ['-4ty', '-3ty', '-2ty', '-1ty', '0ty', '1ty', '2ty', '3ty', '4ty']
plt.xticks(xvalues, x_ticks)
plt.yticks(yvalues, y_ticks)
#
plt.tick_params(labelsize=9)
plt.grid(color='green', linewidth=0.4)
ax.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
#
plt.savefig("./png/fig-0.png",format="png",dpi=150)
#
x = 0 ; y = 0
i_xy = []
# tuple( () )
for i in range(1,14,1) :
    i_xy.append(tuple((x+ r1*np.cos((i*2+1)*np.pi/12), 
                       y+ r1*np.sin((i*2+1)*np.pi/12)
                      )
                     )
               )
#
dodecagon = LineString(i_xy)
xs, ys = dodecagon.xy
plt.plot(xs, ys, color='blue', alpha=1.0, linewidth=0.7)
plt.savefig("./png/fig-1.png",format="png",dpi=150)
#
dodecagon_d = affinity.rotate(dodecagon, 180, (0,-(d1-d2)))
xs, ys = dodecagon_d.xy
plt.plot(xs, ys, alpha=1.0, linewidth=0.7)
plt.savefig("./png/fig-2.png",format="png",dpi=150)
#
"""
triangle_1 = LineString([(0,0), (d1,0), (d1,d2), (0,0)])
triangle_2 = affinity.rotate(triangle_1, -90, (0,0))
#
motif_line(triangle_1, 'magenta', 10, 1.0) 
motif_line(triangle_2, 'darkviolet', 10, 1.2) 
#
plt.savefig("./png/fig-3.png",format="png",dpi=150)
#
"""
for i in (1,2,3,4,5) :
    r_dodecagon = affinity.rotate(dodecagon_d, i*60, (0,0))
    xs, ys = r_dodecagon.xy
    plt.plot(xs, ys, alpha=1.0, linewidth=0.7)
# end for
#
plt.savefig("./png/fig-04.png", format="png", dpi=150)
#
"""
# -------------------------------------------------
'r' --> red
'g' --> green
'b' --> blue
'c' --> cyan
'm' --> magenta
'y' --> yellow
'k' --> black
"""
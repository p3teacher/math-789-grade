# 探究正十二邊形
# dodecagon-step-by-step-1
# 2024-06-16
import numpy as np #導入
import matplotlib.pyplot as plt
from shapely.geometry import LineString
#
r1 = 10
d1 = r1*np.cos(np.pi/12)
d2 = r1*np.sin(np.pi/12)
tx = (d1+d2)
ty = (d1-d2)
#
plt.ion()
fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(1, 1, 1)
ax.set_axis_on()
# ax.set_axis_off()
#
plt.xlim(-2*tx, 2*tx)    # 設定X軸的顯示範圍, from xmin to xmax
plt.ylim(-4*ty, 4*ty)    # 設定Y軸的顯示範圍, from ymin to ymax
#
xvalues = [-2*tx,-1*tx,0,1*tx,2*tx]
yvalues = [-4*ty,-3*ty,-2*ty,-1*ty,0,1*ty,2*ty,3*ty,4*ty]
x_ticks = ['-2tx', '-1tx', '0', '1tx', '2tx']
y_ticks = ['-4ty', '-3ty', '-2ty', '-1ty', '0', '1ty', '2ty', '3ty', '4ty']
plt.xticks(xvalues, x_ticks)
plt.yticks(yvalues, y_ticks)
plt.tick_params(labelsize=10)
plt.grid(color='green', linewidth=0.4)
ax.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig("./png/step-1-1.png",format="png",dpi=150)
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
# end for
#
print(len(i_xy))
print(i_xy)
dodecagon = LineString(i_xy)
xs, ys = dodecagon.xy
plt.plot(xs, ys)
#
plt.savefig("./png/step-1-2.png",format="png",dpi=150)
#
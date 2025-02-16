# All/eP/
# Proofs-of-the-Pythagoras-Theorem
# 2024-02-16
#
"""
Q:
un-sortted /unformated imports error!!!
---------------------------------------
A:
go to pyproject.toml and remove the 
'I' from the select variable list
"""
#
# (a+b)**2    = c**2 + 4*(a*b/2)
# (a+b)*(a+b) = a**2 + 2*a*b + b**2
# we get c**2 = a**2 + b**2
#
import numpy as np
# 載入繪圖模組 pyplot, 重新命名為 plt
import matplotlib.pyplot as plt
from shapely import affinity
from shapely.geometry  import LineString
#
# --------------------------------------
#
def set_graphic_area(width,height) :

    cm2inch = 1/2.54    # inch per cm
    #
    # define graphic area
    #
    left_margin = 1.0   # cm
    right_margin = 1.0  # cm
    #
    figure_width  = width  # cm , from xmin to xmax
    figure_height = height # cm , from ymin to ymax
    #
    top_margin = 1.0    # cm
    bottom_margin = 1.0 # cm
    #
    box_width = left_margin + figure_width + right_margin   # cm
    box_height = top_margin + figure_height + bottom_margin # cm
    #
    top_value    = 1.0 - top_margin / box_height
    bottom_value = bottom_margin / box_height
    left_value   = left_margin / box_width
    right_value  = 1.0 - right_margin / box_width
    #
    return (box_width*cm2inch,box_height*cm2inch,top_value,bottom_value,left_value,right_value,width)
#
# end of def
#
    # Define the arc
# center position is cxy = (cx, cy)
# start_angle, end_angle is in degrees
#
def shapely_Arc(cxy, r, start_angle, end_angle) :
    #
    numsegments = 720
    # The coordinates of the arc
    theta = np.radians(np.linspace(start_angle, end_angle, numsegments))
    x = cxy[0] + r * np.cos(theta)
    y = cxy[1] + r * np.sin(theta)
    Arc = LineString(np.column_stack([x, y]))
    return Arc
    #
# end of def
#
def motif_line(LS, MYcolor, ZORDER, LINEWIDTH) :
    #
    xs, ys = LS.xy
    ax.plot(xs, ys, color=MYcolor, alpha=1.0, linewidth=LINEWIDTH, solid_capstyle='round', zorder=ZORDER)
    return
#
def motif_fill(LS, color, ZORDER, Alpha) :
    #
    xs, ys = LS.xy
    ax.fill(xs, ys, alpha=Alpha, closed=True, edgecolor=None, facecolor=color, fill=True, zorder=ZORDER)
    return
#
def poly_line(LS, MYcolor, ZORDER, LINEWIDTH) :
    #
    xs, ys = LS.exterior.coords.xy
    ax.plot(xs, ys, color=MYcolor, alpha=1.0, linewidth=LINEWIDTH, solid_capstyle='round', zorder=ZORDER)
    return
#
def poly_fill(LS, color, ZORDER, Alpha) :
    #
    xs, ys = LS.exterior.coords.xy
    ax.fill(xs, ys, alpha=Alpha, closed=True, edgecolor=None, facecolor=color, fill=True, zorder=ZORDER)
    return
#
# -------------------------------------------
#
# tup7 is type of Tuple, have 7 indexed value
#
tup7 = set_graphic_area(20, 20) 
#plt.ion()
fig = plt.figure(figsize=(tup7[0], tup7[1])) # 呼叫 pyplot.figure(), 建立一個圖表物件, 並成為目前圖表物件
ax = fig.add_subplot(1,1,1)   # 圖表的繪圖區域被分為1個子圖, 1 row, 1 column, plot to index 1
fig.subplots_adjust(
                top    = tup7[2] ,
                bottom = tup7[3] ,
                left   = tup7[4] ,
                right  = tup7[5] ,
                )
#
plt.xlim(-10,10)
plt.ylim(-10,10)
#
xvalues = range(-10,11,2)
yvalues = range(-10,11,2)
plt.xticks(xvalues)
plt.yticks(yvalues)
plt.tick_params(labelsize=11)
#
plt.grid(color='green', linewidth=1.0)
plt.grid(True)
ax.set_axis_on()    # will turn on  grid line
# ax.set_axis_off() # will turn off grid line
#
# get current axes, set X,Y same ratio & scale  
plt.gca().set_aspect('equal', adjustable='box')
#
plt.savefig("./png/1.png",format="png",dpi=150)
#
h_line = LineString([(-10,0),(10,0)])
v_line = LineString([(0,-10),(0,10)])
#
motif_line(h_line, 'darkviolet', 10,1.0)
motif_line(v_line, 'darkviolet', 10,1.0)
#
plt.savefig("./png/2.png",format="png",dpi=150)
#
left_square = LineString([(0,0),(0,4),
                          (-4,4),(-4,0),
                          (0,0)])
down_square = LineString([(0,0),(0,-2),
                          (2,-2),(2,0),
                          (0,0)])
#
motif_fill(left_square, 'cyan', 10,0.3)
motif_line(left_square, 'navy', 10,1.0)
motif_fill(down_square, 'blue', 10,0.3)
motif_line(down_square, 'navy', 10,1.0)
#
plt.savefig("./png/3.png",format="png",dpi=150)
#
triangle_0 = LineString([(0,0),(2,0),(0,4),(0,0)])
diagonal_0 = LineString([(2,0),(0,4)])
motif_fill(triangle_0, 'magenta', 10,0.3)
motif_line(diagonal_0, 'navy',    10,1.5)
#
plt.savefig("./png/4A.png",format="png",dpi=150)
#
h_line = LineString([(2,3),(4,3)])
v_line = LineString([(3,2),(3,4)])
#
motif_line(h_line, 'blue', 10,1.0)
motif_line(v_line, 'blue', 10,1.0)
#
plt.savefig("./png/4B.png",format="png",dpi=150)
#
triangle_1 = affinity.rotate(triangle_0, -90, (3,3))
triangle_2 = affinity.rotate(triangle_0,-180, (3,3))
triangle_3 = affinity.rotate(triangle_0,-270, (3,3))
#
# diagonal_0 = LineString([(2,0),(0,4)])
diagonal_1 = affinity.rotate(diagonal_0, 90, (0,4))
diagonal_2 = affinity.rotate(diagonal_1, 90, (4,6))
diagonal_3 = affinity.rotate(diagonal_2, 90, (6,2))
#
motif_fill(triangle_1, 'magenta', 10,0.3)
motif_line(diagonal_1, 'navy',    10,1.5)
#
plt.savefig("./png/5.png",format="png",dpi=150)
#
motif_fill(triangle_2, 'magenta', 10,0.3)
motif_line(diagonal_2, 'navy',    10,1.5)
#
plt.savefig("./png/6.png",format="png",dpi=150)
#
motif_fill(triangle_3, 'magenta', 10,0.3)
motif_line(diagonal_3, 'navy',    10,1.5)
#
plt.savefig("./png/7.png",format="png",dpi=150)
#
big_square_1 = LineString([(0,0),(6,0),
                           (6,6),(0,6),
                           (0,0)])
#
motif_line(big_square_1, 'black', 10, 3.0)
#
plt.savefig("./png/8.png",format="png",dpi=150)
#
big_square_2 = LineString([(2,4),(-4,4),
                           (-4,-2),(2,-2),
                           (2,4)])
#
motif_line(big_square_2, 'black', 10, 3.0)
#
plt.savefig("./png/9.png",format="png",dpi=150)
#
print('Done')
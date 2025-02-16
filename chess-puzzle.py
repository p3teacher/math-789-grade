# All/eP/
# chess-puzzle
# 棋盤上的穀粒
# 2024-12-16
#
# 台灣師範大學數學系洪萬生教授 棋盤上的穀粒：數大之奇 
# nani 7up, page 61, explore activity
"""
有一位賢者發明了一個遊戲獻給國王。國王龍心大悅，諭令要以賢者要求的任何賞賜作為回報。這位賢者只想要穀粒！要多少呢？賢者說他要的數量按照棋盤上正方形的數量來算就可以了。
他的公式很簡單：
第一個正方形他要一個穀粒，然後，在接下來的棋盤上的每一個正方形上加倍。換句話說，在第二個正方形上要有兩個(1乘以2)、第三個正方形要有四個(2乘以2)等等，直到全部六十四個正方形都計算出來以決定穀粒的總數。
"""
#
import numpy as np
# 載入繪圖模組 pyplot, 重新命名為 plt
import matplotlib.pyplot as plt
from shapely.geometry  import LineString
#
from replit import clear
from platform import python_version
#
clear()
print('the python version is',python_version())
print(' ')
#
# ---------------------------------------------
#
def set_graphic_area(width,height) :

    cm2inch = 1/2.54    # inch per cm
    #
    # define graphic area
    #
    left_margin = 2.0   # cm
    right_margin = 1.0  # cm
    #
    figure_width  = width  # cm , from xmin to xmax
    figure_height = height # cm , from ymin to ymax
    #
    top_margin = 1.5    # cm
    bottom_margin = 1.5 # cm
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
tup7 = set_graphic_area(10,10)  
# 呼叫 pyplot.figure(), 建立一個圖表物件, 並成為目前圖表物件
# plt.ion()
fig = plt.figure(figsize=(tup7[0], tup7[1]), num='chess-puzzle')
# 圖表的繪圖區域被分為1個子圖, 1 row, 1 column, plot to index 1
ax = fig.add_subplot(1,1,1)  
fig.subplots_adjust(
                top    = tup7[2] ,
                bottom = tup7[3] ,
                left   = tup7[4] ,
                right  = tup7[5] ,
                )
#
plt.xlim(-1,12)
plt.ylim(-1,12)
#
xvalues = range(-1,13,1)
yvalues = range(-100,1201,100)
print(xvalues)
print("-1,0,1,2,3,4,5,6,7,8,9,10,11,12")
print()
#
x_label = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']
plt.xticks(xvalues, x_label)
plt.yticks(yvalues)
plt.tick_params(labelsize=10)
#
plt.grid(color='gray', linewidth=0.4)
plt.grid(True)
ax.set_title('chess-puzzle')
ax.set_xlabel('square id')
ax.set_ylabel('grain numbers')
ax.set_axis_on()    # will turn on  grid line
# ax.set_axis_off() # will turn off grid line
#
plt.savefig("./png/1.png",format="png",dpi=150)
#
x_id = [0,1,2,3,4,5,6,7,8,9,10,11]
xy_list = []
for x in x_id :
    y = np.power(2,x)
    print(y)
    xy_list.append((x,y))
# end for
print('')
print(xy_list)
print('')
#
xy_curve = LineString(xy_list)
motif_line(xy_curve, 'darkgreen', 10, 1.0)
plt.savefig("./png/2A.png",format="png",dpi=150)
#
#
xs, ys = xy_curve.xy
ax.plot(xs, ys, 'ro', alpha=1.0, zorder=20, markersize=4)
#
plt.savefig("./png/2B.png",format="png",dpi=150)
#
x_id = [0,1,2,3,4,5,6,7,8,9,10,11]
# [(0,1), (1,2), (2,4), (3,8), (4,16), (5,32), ...]
for x in x_id :
    y = np.power(2,x)
    print('square',x+1,',y =',y)
    xy_list.append((x,y))
# end for
print('')
#
# x_id = [0,1,2,3,4,5,6,7,8,9,10,11]
for x in x_id :
    y = np.power(2,x)
    if x==0 :
        ax.annotate(str(y), (0,y+20),
        color='navy',
        fontsize=10, 
        zorder=30)
    else :
        ax.annotate(str(y), (x-0.1,y+20),
        color='navy',
        fontsize=10, 
        zorder=30)
    # enfd if
# end for
#
plt.savefig("./png/3.png",format="png",dpi=150)
#
for n in (11,12,13,14,62) :
    num = np.power(2,n)
    print('square '+ str(n+1) + ' have', num, ' grains')
# end for
print('square '+ str(64) + ' have', np.power(2,62), ' grains')
print('             +', np.power(2,62), ' grains')
plt.show()
import cv2
import numpy as np
from  PIL import Image,ImageDraw


np.set_printoptions(threshold=np.nan)

img = cv2.imread('r10.jpg')
image_array = np.array(img)
# print(image_array)

print(image_array[73][98])
col =[]
resistor =[]
code=[]

for row in image_array:
  for pixel in row:
      resistor.append(list(pixel))

# print(resistor)

# boundaries = [
# 	    ([17, 15, 100], [50, 56, 200]),
# 	    ([75, 25, 4], [220, 88, 50]), #85,31
# 	    ([25, 146, 190], [62, 174, 250]),
# 	    ([103, 86, 65], [145, 133, 128])
#         ]
#
# lower_red = np.array(boundaries[0][0],dtype='uint8')
# upper_red = np.array(boundaries[0][1],dtype='uint8')
#
#
# lower_blue = np.array(boundaries[1][0],dtype='uint8')
# upper_blue = np.array(boundaries[1][1],dtype='uint8')
#
#
# lower_yellow = np.array(boundaries[2][0],dtype='uint8')
# upper_yellow = np.array(boundaries[2][1],dtype='uint8')
#
#
#
# lower_grey = np.array(boundaries[3][0],dtype='uint8')
# upper_grey = np.array(boundaries[3][1],dtype='uint8')
#
#
#
# red_mask = cv2.inRange(img,lower_red,upper_red)
# red_res =cv2.bitwise_and(img,img,mask=red_mask)
#
#
# blue_mask = cv2.inRange(img,lower_blue,upper_blue)
# blue_res =cv2.bitwise_and(img,img,mask=blue_mask)
#
#
# yellow_mask = cv2.inRange(img,lower_yellow,upper_yellow)
# yellow_res =cv2.bitwise_and(img,img,mask=yellow_mask)
#
# grey_mask = cv2.inRange(img,lower_grey,upper_grey)
# grey_res =cv2.bitwise_and(img,img,mask=grey_mask)
#
#
# cv2.imshow('res',np.hstack([img,red_res]))
for color in resistor:
     #black
     if 0 <= color[0] < 47 and 0 <= color[1] < 47 and 0<= color[2] <47:
         col.append(resistor.index(color))
         code.append('Black')

     # brown [ 30  63 112] , [ 52  73 101] [ 4  0 94]
     if 0 <= color[0] < 60 and 0 <= color[1] < 86 and 90 <= color[2] <130:
         col.append(resistor.index(color))
         code.append('Brown')


     #Red[ 32  25 230] [ 23  30 193] [  0   0 151] [  0   0 151]
     if 0<= color[0] < 35 and 0 <= color[1] < 36 and 145<= color[2] <=255:
         col.append(resistor.index(color))
         code.append('Red')

    # Orange [  6  91 222]
     if 0 <= color[0] <85 and 70 <= color[1] <140 and 170 <= color[2] <=255:
         col.append(resistor.index(color))
         code.append('Orange')


    #grey
     if 150<color[0]<179 and  178<color[1]<193 and 185<color[2]<200:
          col.append(resistor.index(color))
          code.append('Grey')

    # blue [90 28  2] [82 34  4] [71 32  7] [89 31  1]
     if 64< color[0] <=255 and 20 < color[1] <50 and 0 <=color[2] < 15:
         col.append(resistor.index(color))
         code.append('Blue')


    # Violet [ 93  28 127] [ 58   1 116] [ 72   6 117] [ 67  10 108]
     if 50 < color[0] <= 110 and 0<= color[1] < 40 and 90 <= color[2] <=140:
         col.append(resistor.index(color))
         code.append('Violet')


    # Green[30 73 40][22 68 45] [51 77 29]
     if 15< color[0] <= 60 and 56 <= color[1] <=255 and 16 <= color[2] <= 60:
         col.append(resistor.index(color))
         code.append('Green')

print(col)
print(code)
cv2.waitKey(0)
cv2.destroyAllWindows()


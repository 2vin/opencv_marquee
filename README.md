# Opencv Marquee
To make a vertical marquee slider from images in OpenCV

## Usage:
# python -i image -s slider_speed  -p percent_scroll -o output.avi
image : directory of images (same size)
slider_speed : speed of the marquee [Range (int): 0 - 15]
percent_scroll : percentage of marquee scroller in percent [Range (float): 0 - 1]
output : output image path (.avi)

## Input images

<table>
  <tr>
    <td>Image 1</td>
     <td>Image 2</td>
     <td>Image 3</td>
    <td>Image 4</td>
  </tr>
  <tr>
    <td><img src="https://github.com/2vin/opencv_marquee/blob/master/images/4.png" width=320 height=180></td>
    <td><img src="https://github.com/2vin/opencv_marquee/blob/master/images/3.png" width=320 height=180></td>
    <td><img src="https://github.com/2vin/opencv_marquee/blob/master/images/2.png" width=320 height=180></td>
    <td><img src="https://github.com/2vin/opencv_marquee/blob/master/images/1.png" width=320 height=180></td>
  </tr>
 </table>


![Image](https://github.com/2vin/opencv_marquee/blob/master/images/1.png) ![Image](https://github.com/2vin/opencv_marquee/blob/master/images/2.png) ![Image](https://github.com/2vin/opencv_marquee/blob/master/images/3.png) ![Image](https://github.com/2vin/opencv_marquee/blob/master/images/4.png)

## Output 
![Image](https://github.com/2vin/opencv_marquee/blob/master/result.gif) 

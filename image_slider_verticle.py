## "Usage: python -i image -s slider_speed  -p percent_scroll -o output.avi"

import argparse
import cv2
import time
import os   


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--image-folder',
                        default='',#'input/remove_people/',
                        type=str,
                        help='The directory where images are saved')


    parser.add_argument('-o', '--output-path',
                        type=str,
                        default='./output.avi',
                        help='The path of the output video file')

    parser.add_argument('-s', '--speed',
                        type=int,
                        default=1,
                        help='The slider speed of the output video')

    parser.add_argument('-p', '--percent',
                        type=float,
                        default=.5,
                        help='The scrolling height (in percent) of the output image')


    FLAGS, unparsed = parser.parse_known_args()

    if not FLAGS.image_folder or not FLAGS.output_path or not FLAGS.speed  or not FLAGS.percent :
        print("Usage: python -i image -s slider_speed  -p percent_scroll -o output.avi")
        exit()


    if FLAGS.image_folder:
        im_dir = FLAGS.image_folder
        # speed of slider in Integer
        speed = FLAGS.speed
        # how much to scroll in scroll_percent
        percent = FLAGS.percent
        
        slider = None
        image_shape = None
        # all files in directory
        for file in os.listdir(im_dir):
            # path of image from directory
            im_path = im_dir+"/" + file
            # load image one-by-one
            im = cv2.imread(im_path)
            # load a slider images to scroll
            if slider is None:
                slider = im
                image_shape = im.shape
            else:
                slider = cv2.vconcat([slider, im])

        # Initializing a video writer using OpenCV
        result = cv2.VideoWriter(FLAGS.output_path, cv2.VideoWriter_fourcc(*'MJPG'),int(30), (image_shape[1], int(percent*image_shape[0])))

        print(int(percent*image_shape[0]))
        for i in range(slider.shape[0]-int(percent*image_shape[0])):
            if i % speed == 0:
                # crop the slice of the slider we want to show at this time
                slide = slider[i:i+int(percent*image_shape[0]), 0:slider.shape[1]] 

                # save the image frame in the video
                result.write(slide)

                # show the image to visualize
                cv2.imshow("slider", slide)
                cv2.waitKey(int(30)+1)
            
    # close all windows
    result.release()
    cv2.destroyAllWindows()







# ###
#             slider = im[1740:2000, 0:800] 
#         slider = cv2.vconcat([slider, im])
#         cv2.imshow("im", slider)

#         for i in range(2000):
#             print(i)
#             slide = slider[i:i+260, 0:800] 
#             result.write(slide)

#             cv2.imshow("image", slide)
#             cv2.waitKey(1*speed)


#         cv2.waitKey(0)
#         result.release()
#         cv2.destroyAllWindows()

# ###
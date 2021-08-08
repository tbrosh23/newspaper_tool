# Obtains graylevel of a picture

import matplotlib.pyplot as plt
import PIL.Image as im
import cv2

class get_graylevel:
    def __init__(self, impath):
        self.impath = impath
        self.img = ''
        self.load_image()
        

    def load_image(self):
        self.img = cv2.imread(self.impath)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def show_image(self):
        cv2.imshow('Title',self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pass

    
    # Returns min and max values of pixels
    def min_max_pixels(self):
        maxpixel = 0
        minpixel = 300
        avg = 0
        rows,cols = self.img.shape
        for i in range(rows):
            for j in range(cols):
                if self.img[i,j] < minpixel:
                    minpixel = self.img[i,j]
                if self.img[i,j] > maxpixel:
                    maxpixel = self.img[i,j]
                avg += self.img[i,j]
        print('max: ', maxpixel)
        print('min: ', minpixel)
        print('avg: ', float(avg)/(rows*cols))
        pass

def main():
    test = get_graylevel('./images/a01-000u-00.png')
    test.show_image()
    test.min_max_pixels()


if __name__=="__main__":
    main()
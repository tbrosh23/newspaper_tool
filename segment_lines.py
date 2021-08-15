import matplotlib.pyplot as plt
import cv2
import numpy as np

class segment_lines():
    def __init__(self, article_path):
        self.article_path = article_path
        self.img = ''
        self.load_image()
        self.get_average_pixel_value()
        pass

    def load_image(self):
        self.img = cv2.imread(self.article_path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def show_image(self, img):
        cv2.imshow('Title',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pass

    def draw_line(self, start, end, thickness):
        cv2.line(self.img, start, end, thickness)
        #self.show_image()

    def get_average_pixel_value(self):
        rows,cols = self.img.shape
        total_pix = rows*cols
        self.pix_average = 0
        for i in range(rows):
            for j in range(cols):
                self.pix_average += self.img[i,j]

        self.pix_average = self.pix_average / total_pix
        print("Pixel average: %d\n", sum)

    def scan_image(self):
        self.paper_lines = []
        rows,cols = self.img.shape
        print(rows, cols)
        # Sum the total pixel values of each row.
        # If the sum exceeds a certain threshold, than we can 
        # say that it is mostly white (a space between lines).
        # Then, add a line here and move on to the next one.
        # Take threshold as the average pixel value of the entire image
        threshold = self.pix_average
        row_sum = 0
        in_white = 0
        in_text = 0
        for i in range(rows):
            row_sum = 0
            for j in range(cols):
                row_sum+=self.img[i,j]
            row_sum = row_sum / cols
            if(row_sum > threshold):
                self.draw_line((0, i), (cols, i), 10)
                in_white = 1

                #If in_text == True, we just got out of text ( in to whitespace)
                if(in_text):
                    end_row = i
                    temp_img = np.zeros((end_row-start_row, cols), np.uint8)
                    temp_img[:,:] = self.img[start_row:end_row,:]
                    self.show_image(temp_img)
                in_text = 0
                pass
            else:
                in_text = 1
                # If in_white == True, we just got out of a whitespace
                if(in_white):
                    start_row = i
                in_white = 0
                

                


def main():
    article_path = './newspaper_tool/images/article.png'
    test = segment_lines(article_path)
    test.show_image(test.img)
    test.scan_image()
    test.show_image(test.img)
    test.draw_line((0, 200), (423, 200), 10)

if __name__ == "__main__":
    main()
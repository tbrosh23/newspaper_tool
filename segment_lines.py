import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

class segment_lines():
    def __init__(self, article_path):
        self.article_path = article_path
        if not os.path.exists('./newspaper_tool/training'):
            os.mkdir('./newspaper_tool/training')
        if not os.path.exists('./newspaper_tool/training/img'):
            os.mkdir('./newspaper_tool/training/img')
        self.img = ''
        self.load_image()
        self.pix_average = self.get_average_pixel_value(self.img)
        self.line_img = []
        self.word_img = []
        self.word_line_img = []
        
        pass

    def load_image(self):
        self.img = cv2.imread(self.article_path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def show_image(self, img):
        cv2.imshow('Title',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def draw_line(self, img, start, end, thickness):
        cv2.line(img, start, end, thickness)
        #self.show_image()

    def get_average_pixel_value(self, img):
        rows,cols = img.shape
        total_pix = rows*cols
        pix_average = 0
        for i in range(rows):
            for j in range(cols):
                pix_average += img[i,j]

        pix_average = pix_average / total_pix
        #print("Pixel average: %d\n", sum)
        return pix_average

    def scan_image(self):
        SAVING = True
        SHOWING = False
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
        num_image = 0
        for i in range(rows):
            row_sum = 0
            for j in range(cols):
                row_sum+=self.img[i,j]
            row_sum = row_sum / cols
            if(row_sum > threshold):
                #self.draw_line(self.img, (0, i), (cols, i), 10)
                in_white = 1

                #If in_text == True, we just got out of text ( in to whitespace)
                if(in_text):
                    end_row = i
                    # Assume that lines less than 6 lines are false positives
                    if (end_row - start_row) < 6:
                        pass
                    else:
                        temp_img = np.zeros((end_row-start_row+4, cols), np.uint8)
                        # Give 2 pixels on either side as a buffer
                        temp_img[:,:] = self.img[start_row-2:end_row+2,:]
                        self.line_img.append(temp_img)
                        if SHOWING:
                            self.show_image(temp_img)
                        if SAVING:
                            if num_image > 9:
                                img_index = str(num_image)
                            else:
                                img_index = '0'+str(num_image)
                            name = 'newspaper_tool/training/img/a01-000u-'+img_index+'.png'
                            cv2.imwrite(name, temp_img)
                            num_image += 1
                in_text = 0
                pass
            else:
                in_text = 1
                # If in_white == True, we just got out of a whitespace
                if(in_white):
                    start_row = i
                in_white = 0

    # We may need to split lines into words for training
    def get_split_words(self):
        SAVING=0
        SHOWING=0

        to_split = self.line_img[0]

        self.show_image(to_split)
        rows, cols = to_split.shape
        #self.draw_line(to_split, (10, 0), (10, rows), 10)
        #self.draw_line(to_split, (17, 0), (17, rows), 10)
        #self.show_image(to_split)
        pix_average = self.get_average_pixel_value(to_split)
        threshold = pix_average
        # This shape is 14 by 423

        # Iterate through all the columns, finding spaces (sections where the local average pixel value
        # falls lower than the global average pixel value)
        in_text = 0

        # Assume start in white
        in_white = 1
        block_width = 7
        line_num = 0
        for splitting in self.line_img:
            self.word_line_img.append([])
            rows, cols = splitting.shape
            pix_average = self.get_average_pixel_value(to_split)
            threshold = pix_average
            for j in range(cols-block_width):
                
                # Since we are seeing the space between letters, need to scan using a block instead of a single
                # column of the image. This will make blocks seem to have a higher pixel value, so we may need to
                # increase the threshold
                col_sum = 0
                for k in range(j, j+block_width):
                    for i in range(rows):
                        col_sum+=splitting[i,k]
                col_sum = col_sum / (rows*block_width)
                # If true, we have reached a space
                if(col_sum > threshold*1.1):
                    in_white = 1

                    if(in_text):
                        end_col = j
                        pass
                        # Assume that lines less than 6 lines are false positives
                        if (end_col - start_col) < 6:
                            pass
                        else:
                            temp_img = np.zeros((rows, end_col-start_col+4), np.uint8)
                            # Give 2 pixels on either side as a buffer
                            temp_img[:,:] = splitting[:,start_col-2:end_col+2]
                            self.word_img.append(temp_img)
                            self.word_line_img[line_num].append(temp_img)
                            if SHOWING:
                                self.show_image(temp_img)
                            """
                            if SAVING:
                                if num_image > 9:
                                    img_index = str(num_image)
                                else:
                                    img_index = '0'+str(num_image)
                                name = 'newspaper_tool/training/img/a01-000u-'+img_index+'.png'
                                cv2.imwrite(name, temp_img)
                                num_image += 1
                            """
                    in_text = 0

                    pass
                else:
                    in_text = 1
                    # If in_white == True, we just got out of a whitespace
                    if(in_white):
                        start_col = j
                    in_white = 0

            line_num+=1
            pass

    def show_all_words_per_line(self):
        for i in range(len(self.word_line_img)):
            print('Line %d\n' % i)
            for j in range(len(self.word_line_img[i])):
                self.show_image(self.word_line_img[i][j])
                

                


def main():
    article_path = './newspaper_tool/images/article.png'
    test = segment_lines(article_path)
    test.show_image(test.img)
    test.scan_image()
    #test.show_image(test.img)
    #test.draw_line(test.img,(0, 200), (423, 200), 10)
    test.get_split_words()
    test.show_all_words_per_line()
if __name__ == "__main__":
    main()
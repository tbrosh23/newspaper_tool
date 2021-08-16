import cv2
import os
import re

# Give path to the data folder and text folder and assemble key textfile
class assemble_key:
    def __init__(self, textpath, imgdir):
        self.textpath = textpath
        self.imgdir = imgdir
        self.bounds = []
        self.average = []
        self.segmented = []
        self.num_components = []
        self.imgnames = []
        if not os.path.exists('./newspaper_tool/training'):
            os.mkdir('./newspaper/training')
        if not os.path.exists('./newspaper_tool/training/gt'):
            os.mkdir('./newspaper_tool/training/gt')
        pass
    
    def parsetext(self):
        self.textcontents = []
        with open(self.textpath,'r') as fp:
            line = 'asdf'
            ind = 0
            line = fp.readline()
            while line != '':
                words = line.split(' ')
                self.textcontents.append('')
                for i in words:
                    self.textcontents[ind] += i+'|'
                
                # Strip last | character and the '\n'
                self.textcontents[ind] = self.textcontents[ind].rstrip(self.textcontents[ind][-1])
                self.textcontents[ind] = self.textcontents[ind].rstrip(self.textcontents[ind][-1])
                ind = ind+1
                line = fp.readline()

        #self.textcontents.pop(len(self.textcontents)-1)
        print(self.textcontents)
        pass

    def get_components(self):
        # Check how many different ASCII codes exist

        for line in self.textcontents:
            phrase = line
            archive = []
            exists = False
            for i in phrase:
                exists = False
                for j in archive:
                    if i == j:
                        exists = True
                
                if not exists:
                    archive.append(i)
            
            self.num_components.append(len(archive)-1)

        pass
    
    def load_image(self, imgpath):
        self.img = cv2.imread(imgpath)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    # For now just take the entire image as bounds
    def get_bounds(self):
        rows, cols = self.img.shape
        #print('Rows, cols: ', rows, cols)
        #print(rows/2, cols/2)
        # For now, go (x_min, x_max, y_min, y_max)
        self.bounds.append((0, 0, cols, rows))
        pass

    def get_graylevel(self):
        # For now, compute the average pixel value
        avg = 0
        rows,cols = self.img.shape
        for i in range(rows):
            for j in range(cols):
                avg += self.img[i,j]
        avg = int(avg / (rows*cols))
        self.average.append(avg)

    def get_segmentation(self):
        # For now, just say ok for all
        self.segmented.append('ok')

    def iterate_through_images(self):
        # Go through all images and get bounds, graylevel, segmentation, and name
        images = os.listdir(self.imgdir)
        for i in images:
            self.load_image(self.imgdir+i)
            self.get_bounds()
            self.get_graylevel()
            self.get_segmentation()
            self.imgnames.append(i[:len(i)-4])
        pass

    def sort_listdir(self):
        imgnums = []
        for i in self.imgnames:
            #print(i)
            imgnums.append(int(re.search(r'\d+', i).group()))

        # Bubble sort to re-order self.imgnames to be 0,1,2,3,4...
        for i in range(len(self.imgnames)):
            for j in range(i,len(self.imgnames)):
                if imgnums[i] > imgnums[j]:
                    # Sort imgnums, as well as imgnames
                    temp = imgnums[j]
                    imgnums[j] = imgnums[i]
                    imgnums[i] = temp

                    temp = self.imgnames[j]
                    self.imgnames[j] = self.imgnames[i]
                    self.imgnames[i] = temp


        pass

    def create_key(self):
        # Combine metadata and data to create entire key
        #TODO: sort os.listdir'd files by increasing line number
        # so data is properly attributed
        with open('./newspaper_tool/training/gt/words.txt','w') as fp:
            image_ind = 0
            while(image_ind < len(self.textcontents)):
                bounds = []
                for i in range(4):
                    bounds+=str(self.bounds[image_ind][i])+' '
                bounds = ''.join(bounds)
                to_write = self.imgnames[image_ind]+' '+self.segmented[image_ind] +' ' \
                    +str(self.average[image_ind])+' '+str(self.num_components[image_ind]) \
                    +' '+bounds+self.textcontents[image_ind]+'\n'
                fp.write(to_write)
                image_ind += 1


def main():
    test = assemble_key('./newspaper_tool/text/lines.txt','./newspaper_tool/training/img/')
    test.parsetext()
    test.get_components()
    test.iterate_through_images()
    test.sort_listdir()
    test.create_key()

if __name__ == "__main__":
    main()
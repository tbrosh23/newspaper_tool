import cv2
import os

# Give path to the data folder and text folder and assemble key textfile
class assemble_key:
    def __init__(self, textpath, imgpath):
        self.textpath = textpath
        self.imgpath = imgpath
        self.bounds = []
        self.average = []
        self.segmented = []
        self.num_components = []
        if not os.path.exists('./newspaper_tool/training'):
            os.mkdir('./newspaper/training')
        if not os.path.exists('./newspaper_tool/training/key'):
            os.mkdir('./newspaper_tool/training/key')
        self.load_image()
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

        self.textcontents.pop(len(self.textcontents)-1)
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
    
    def load_image(self):
        self.img = cv2.imread(self.imgpath)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    # For now just take the entire image as bounds
    def get_bounds(self):
        rows, cols = self.img.shape
        print('Rows, cols: ', rows, cols)
        print(rows/2, cols/2)
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
        self.average.append(avg)

    def get_segmentation(self):
        # For now, just say ok for all
        self.segmented.append('ok')


def main():
    test = assemble_key('./newspaper_tool/text/lines.txt','./data/lines/a01/a01-000u/a01-000u-02.png')
    test.parsetext()
    test.get_bounds()
    test.get_components()

if __name__ == "__main__":
    main()
import cv2

# Give path to the data folder and text folder and assemble key textfile
class assemble_key:
    def __init__(self, textpath, imgpath):
        self.textpath = textpath
        self.imgpath = imgpath
        self.load_image()
        pass
    
    def parsetext(self):
        self.textcontents = []
        with open(self.textpath,'r') as fp:
            line = 'asdf'
            ind = 0
            while line != '':
                line = fp.readline()
                words = line.split(' ')
                self.textcontents.append('')
                for i in words:
                    self.textcontents[ind] += i+'|'
                self.textcontents[ind] = self.textcontents[ind].rstrip(self.textcontents[ind][-1])
                ind = ind+1

        self.textcontents.pop(len(self.textcontents)-1)
        print(self.textcontents)
        pass
    
    def load_image(self):
        self.img = cv2.imread(self.imgpath)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    # For now just take the entire image as bounds
    def getbounds(self):
        rows, cols = self.img.shape
        print('Rows, cols: ', rows, cols)
        print(rows/2, cols/2)
        pass


def main():
    test = assemble_key('./text/lines.txt','../data/lines/a01/a01-000u/a01-000u-02.png')
    test.parsetext()

if __name__ == "__main__":
    main()
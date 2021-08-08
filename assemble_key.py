
class assemble_key:
    def __init__(self, textpath):
        self.textpath = textpath
        pass
    
    def parsetext(self):
        with open(self.textpath,'r') as fp:
            line = fp.readline()
            words = line.split(' ')
            newline = ''
            for i in words:
                newline += i+'|'
            newline = newline.rstrip(newline[-1])
            print(newline)
        pass


def main():
    test = assemble_key('./text/lines.txt')
    test.parsetext()

if __name__ == "__main__":
    main()
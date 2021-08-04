from pdf2image import convert_from_path
import matplotlib.pyplot as plt

images = images= convert_from_path('https://chroniclingamerica.loc.gov/data/batches/au_brown_ver01/data/sn86072192/00340583310/1897080101/0236.pdf',
    poppler_path=r"E:/Release-21.03.0/poppler-21.03.0/Library/bin")

images[0].save('page 2.jpg','JPEG')
plt.imshow(images[0])
plt.show()

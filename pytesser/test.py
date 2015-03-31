from pytesser import *
#im = Image.open('fnord.tif')
im = Image.open('phototest.tif')
#im = Image.open('eurotext.tif')
#im = Image.open('fonts_test.png')
text = image_to_string(im)
print text


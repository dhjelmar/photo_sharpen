import pymupdf 
import re

def pdf2png(pdf_file, dpi=600, zoom=72):
    # https://stackoverflow.com/questions/69643954/converting-pdf-to-png-with-python-without-pdf2image
    # https://github.com/pymupdf/PyMuPDF
    # dpi = 600  # choose desired dpi here
    # zoom = dpi / 72  # zoom factor, standard: 72 dpi

    # extract filename from pdf_file
    pattern = '[\w-]+?(?=\.)'
    fn = re.search(pattern, pdf_file).group()

    magnify = pymupdf.Matrix(zoom, zoom)  # magnifies in x, resp. y direction
    doc = pymupdf.open(pdf_file)  # open document
    for page in doc:
        image_name = fn + '_' + str(page.number) + '.png'
        print('saving file: ', image_name)
        pix = page.get_pixmap(matrix=magnify)  # render page to an image
        #pix.save(f"'{image_name}'")
        pix.save(f"{image_name}")
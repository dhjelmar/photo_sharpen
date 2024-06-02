#!/c/Users/dlhje/anaconda3/envs/py39/python
# remember to also make the script executable: chmod 755 budget.py
# execute script with: ./budget.py

## to execute file, need to:
##   1. Open Project using one of the following
##      a. Open VSCode
##         Select File / Open Folder / F:\Documents\01_Dave\Programs\GitHub_home\budget
##      b. Double click project folder in File Explorer
##         (double clicking budget.py in File Explorer does not open Project correctly)
##   3. Select "Run Below" in the cell below these instructions

# %%[markdown]   # Jupyter-like notebook in text file using ipython extension and ipykernel package
# # Budget Vs. Actual Spending

#%% 
## import packages
import pandas as pd
import pymupdf # imports the pymupdf library
import numpy as np
import matplotlib.pyplot as plt

## import my functions
from modules.pdf2png import pdf2png
from modules.show_image import show_image


############################################################
#%%
# Convert multi-page PDF to JPG files
redo = False
if (redo):
    pdf_file = "F:\\Documents\\01_Dave\\Engineering\\hot_patch\\WAPD-TM-1419_Table1.pdf"
    pdf2png(pdf_file)
    pdf_file = "F:\\Documents\\01_Dave\\Engineering\\hot_patch\\WAPD-TM-1419_Table2.pdf"
    pdf2png(pdf_file)
    df_file = "F:\\Documents\\01_Dave\\Engineering\\hot_patch\\WAPD-TM-1419_TableA.pdf"
    pdf2png(pdf_file)


#%%
# Sharpen (unblur) images
# https://www.geeksforgeeks.org/python-sharpen-and-blur-filtering-using-pgmagick/


'''
############################################################
#%%
# Convert PDF to text
# https://github.com/pymupdf/PyMuPDF
#doc = pymupdf.open(pdf_file) # open a document
#for page in doc: # iterate the document pages
#  text = page.get_text() # get plain text encoded as UTF-8
#print(text)

# %%
# Show first page
# https://github.com/pymupdf/PyMuPDF
doc = pymupdf.open(pdf_file) # open a document
page = doc[0]  # read first page to demo the layout
show_image(page,"First Page Content")

#%%
# Extract and join multiple tables
dataframes = []  # list of DataFrames per table fragment
for page in doc:  # iterate over the pages
    tabs = page.find_tables()  # locate tables on page
    if len(tabs.tables) == []:  # no tables found?
        break  # stop
    tab = tabs[0]  # assume fragment to be 1st table
    dataframes.append(tab.to_pandas())  # append this DataFrame
df = pd.concat(dataframes)  # make concatenated DataFrame
df  # show it

# %%
'''
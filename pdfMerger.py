# run pip install PyPDF2
# put the files you want to merge in the same directory as this script
# or alternatively run this scripts in the directory that contains the files you want to merge
import PyPDF2
import sys
import os

merger = PyPDF2
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
#         print(file)
        merger.append(file)
    merger.write("combinedBSUniDocs.pdf")
        
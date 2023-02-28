import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endsWith(".pdf"):
        merger.append(file)
        merger.write("combinedDocs.pdf")
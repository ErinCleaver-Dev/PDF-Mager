#https://pypi.org/project/PyPDF2/
#https://pypdf2.readthedocs.io/en/stable/

import PyPDF2 
import pathlib 
import sys 


pdf_list = []

try:
    pdf_list = sys.argv[1:]
except:
    print("Failed to provide pdfs")

def pdf_merger(pdf_list: list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        path = pathlib.Path(__file__).parent / f"documents/{pdf}"
        merger.append(path)
    merger.write('super.pdf')

pdf_merger(pdf_list)
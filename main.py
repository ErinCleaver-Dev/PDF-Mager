#https://pypi.org/project/PyPDF2/
#https://pypdf2.readthedocs.io/en/stable/


import sys 
from pdf_functions import pdf_merger, pdf_watermarker

pdf_list = []

try:
    pdf_list = sys.argv[1:]
except:
    print("Failed to provide pdfs")

pdf_merger(pdf_list, 'documents')

pdf_watermarker('wtr.pdf', 'super.pdf', 'documents')




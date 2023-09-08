#https://pypi.org/project/PyPDF2/
#https://pypdf2.readthedocs.io/en/stable/

import PyPDF2 
import pathlib 

filepath = pathlib.Path(__file__).parent / "documents\\twopage.pdf"

with open(filepath, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # to get the number of pages use len(reder.pages)
    print(len(reader.pages))





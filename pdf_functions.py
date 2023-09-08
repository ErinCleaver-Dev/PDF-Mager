import PyPDF2 
import pathlib 

def pdf_merger(pdf_list: list, foldername):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        path = pathlib.Path(__file__).parent / f"{foldername}/{pdf}"
        merger.append(path)
    merger.write('super.pdf')
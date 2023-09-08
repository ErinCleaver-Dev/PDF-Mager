import PyPDF2 
import pathlib 
import os

def pdf_merger(pdf_list: list, foldername='.'):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        path = pathlib.Path(__file__).parent / f"{foldername}/{pdf}"
        merger.append(path)
    merger.write('super.pdf')

def pdf_watermarker(image, name, folder1=".", folder2="."):
    path_watermark = pathlib.Path(__file__).parent / f"{folder1}/{image}"
    path_file = pathlib.Path(__file__).parent / f"{folder2}/{name}"
    if(os.path.exists(path_file) and os.path.exists(path_watermark)): 
        file = PyPDF2.PdfReader(path_file)
        writer = PyPDF2.PdfWriter()
        watermark = PyPDF2.PdfReader(path_watermark)

        try: 
            for page in file.pages:
                page.merge_page(watermark.pages[0])
                writer.add_page(page)
            with open('watered_marked.pdf', 'wb') as file:
                writer.write(file)
            
        except TypeError as error: 
            print(f'failed to create pdf: {error}')
    


#https://pypi.org/project/PyPDF2/
#https://pypdf2.readthedocs.io/en/stable/

import PyPDF2 
import pathlib 


# filepath = pathlib.Path(__file__).parent / "documents\twopage.pdf"

# with open(filepath, 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     # to get the number of pages use len(reder.pages)
#     print(len(reader.pages))

filepath = pathlib.Path(__file__).parent / "documents\onepage.pdf"

with open(filepath, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # to get the number of pages use len(reder.pages)
    # print(len(reader.pages))
    # to get page the first page type in pages[0] since it is a list of objects
    print(reader.pages[0])

    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    # the newest verison 3.0 has changed it to rotate
    with open('documents/route.pdf', 'wb') as new_file:
        writer.write(new_file)


                        






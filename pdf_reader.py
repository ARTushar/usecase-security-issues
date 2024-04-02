from pypdf import PdfReader
import PyPDF2 as ppdf2
import PyPDF4 as ppdf4
import fitz

pdf_path = 'resources/bss-ch01.pdf'
# pdf_path = 'state_of_the_union.pdf'

def load_pdf(file_path):
    # Logic to read pdf
    reader = PdfReader(file_path)

    # Loop over each page and store it in a variable
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text

def load_pdf_2(file_path):
    # Logic to read pdf
    reader = ppdf2.PdfReader(file_path)

    # Loop over each page and store it in a variable
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text
    
def load_pdf_4(file_path):
    # Logic to read pdf

    pdf = ppdf4.PdfFileReader(file_path)
    first_page = pdf.getPage(0)
    print(first_page.extract_text())
    text = ''
    for i in range(pdf.getNumPages()):
        text += pdf.getPage(i).extract_text()
    return text

def load_pdf_fitz(file_path):
    doc = fitz.open(file_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

    
text = load_pdf_fitz(file_path=pdf_path)

with open('temp.txt', 'w') as file:
    file.write(text)
    
# print(text)
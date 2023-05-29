import textract
import PyPDF2
import os

def extract_text_from_pdf(file):
    '''Opens and reads in a PDF file from path'''
    
    fileReader = PyPDF2.PdfReader(open(file,'rb'))
    page_count = len(fileReader.pages)
    text = [fileReader.pages[i].extract_text() for i in range(page_count)]
    
    return str(text).replace("\\n", "")

def extract_text_from_word(filepath):
    '''Opens en reads in a .doc or .docx file from path'''
    
    txt = textract.process(filepath).decode('utf-8')
    
    return txt.replace('\n', ' ').replace('\t', ' ')


def file_extraction(location):
    filename, file_extension = os.path.splitext(location)
    if file_extension ==".pdf":
        return extract_text_from_pdf(location)
    elif file_extension ==".docx" or file_extension==".doc":
        return extract_text_from_word(location)
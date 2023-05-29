import os
import PyPDF2
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import PyPDF2, pdfplumber
import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import read_files as rd

def output(file_location, job_description):
    file_location=file_location+"/"
    job = rd.file_extraction(job_description)
    # print(job)
    Script_Req = job
    Script_Req=''.join(Script_Req)
    Req_Clear=Script_Req.replace("\n","")

    os.chdir(file_location)
    pdfs = []
    for file in glob.glob("*.pdf"):
        pdfs.append(file)
    for file in glob.glob("*.docx"):
        pdfs.append(file)
    for file in glob.glob("*.doc"):
        pdfs.append(file)
    # print(pdfs)

    match_p =[]
    # print(pdfs)
    for i in pdfs:
        resume = rd.file_extraction(i)
        Match_Test=[resume,Req_Clear]
        cv=CountVectorizer()
        count_matrix=cv.fit_transform(Match_Test)
        MatchPercentage=cosine_similarity(count_matrix)[0][1]*100
        match_p.append(round(MatchPercentage,2))
        # print(match_p)
    return match_p
        





    # #calculate the simimlarity
    # def Similarity(file_location, job_description):
    #     CV_File = open(file_location,'rb')
    #     Script = PyPDF2.PdfReader(CV_File)
    #     pages = len(Script.pages)

    #     Script = []
    #     with pdfplumber.open(CV_File) as pdf:
    #         for i in range (0,pages):
    #             page=pdf.pages[i]
    #             text=page.extract_text()
    #             Script.append(text)

    #     Script=''.join(Script)
    #     CV_Clear=Script.replace("\n","")
    #     CV_Clear


    #     Script_Req = job_description
    #     Script_Req=''.join(Script_Req)
    #     Req_Clear=Script_Req.replace("\n","")
    #     Req_Clear

    #     Match_Test=[CV_Clear,Req_Clear]

       
    #     cv=CountVectorizer()
    #     count_matrix=cv.fit_transform(Match_Test)

    #     MatchPercentage=cosine_similarity(count_matrix)[0][1]*100
    #     return round(MatchPercentage,2)
    

    # def readfiles():
    #     os.chdir(file_location)
    #     pdfs = []
    #     for file in glob.glob("*.pdf"):
    #         pdfs.append(file)
    #     return pdfs

    # #for appending matching % into list match_p
    # pdfs = readfiles()
    # match_p =[]

    # for i in range(len(pdfs)):
    #     asf= file_location+str(pdfs[i])
    #     match_p.append(Similarity(asf, job_description))
    #     print(match_p)

    # return match_p


# os.chdir(folder_location)
# pdfs = []
# for file in glob.glob("*.pdf"):
#     pdfs.append(file)
# for file in glob.glob("*.docx"):
#     pdfs.append(file)
# for file in glob.glob("*.doc"):
#     pdfs.append(file)
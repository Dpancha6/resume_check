import PyPDF2
import docx2txt
import fitz
import re
from PyPDF2 import PdfReader
import os

# folder path
dir_path = r'Resume\\'

# list to store files
res = []





def classifier(pdf_file):
    with open(pdf_file, "rb") as f:
        pdf = fitz.open(f)
        res = []
        for page in pdf:
            image_area = 0.0
            text_area = 0.0
            for b in page.get_text("blocks"):
                if '<image:' in b[4]:
                    r = fitz.Rect(b[:4])
                    image_area = image_area + abs(r)
                else:
                    r = fitz.Rect(b[:4])
                    text_area = text_area + abs(r)
            if image_area == 0.0 and text_area != 0.0:
                res.append(1)
            if text_area == 0.0 and image_area != 0.0:
                res.append(0)
        return res



# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    # if os.path.isfile(os.path.join(dir_path, path)):

    try:
        if path[-3:] == 'pdf':
            file_path = (f"Resume\\{path}")
            classifier_result = classifier(file_path)
            if 0 in classifier_result:
                print("PDF is image-based!... Please Provide in another Formate")
            else:

                # creating a pdf file object
                # pdfFileObj = open(f"Resume\\{filename}", 'rb')

                # # creating a pdf reader object
                # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                # # creating a page object
                # pageObj = pdfReader.getPage(0)
                Reject = 1
                skills = ['css' 'javascript',
                          'python', 'aws']
                reader = PdfReader(f"Resume\\{path}")
                number_of_pages = len(reader.pages)
                for i in range(number_of_pages):
                    page = reader.pages[i]
                    text = page.extract_text()

        # page = reader.pages[0]
        # text = page.extract_text()
                    
                # extracting text from page
                    for skill in skills:
                        if (re.search(fr'\b{skill.lower()}\b', text.lower())):
                            print(skill, 'in this resume')
                            Reject = 0
                            skills.remove(skill)
                    
                if Reject:
                    print(f"Rejected {path} !!!   No skills in the resume")
                # closing the pdf file object
        else:
        
            pageObj = docx2txt.process(f"Resume\\{path}")
            Reject = 1
            for skill in skills:
                if (re.search(fr'\b{skill.lower()}\b', pageObj.lower())):
                    print(skill, 'in this resume')
                    Reject = 0
            

            if Reject:
                print(f"Rejected {path} !!!   No skills in the resume")
        print('')
    except:
        print('DOcument is not valid')



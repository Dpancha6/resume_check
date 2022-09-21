import PyPDF2

skills = ['Github', 'java', 'python', 'aws']

filename = input("Enter File name \n")

pdfFileObj = open(f"Resume\\{filename}", 'rb')

    # creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
for skill in skills:
    if skill.lower() in pageObj.extractText().lower():
        print(skill, 'in this resume')  
else:
    print("Rejected!!! No skills in the resume")

# closing the pdf file object
pdfFileObj.close()

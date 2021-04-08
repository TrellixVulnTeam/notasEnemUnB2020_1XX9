# %%
import PyPDF2

nomecursoPDF = open('PDFs/nomecurso.PDF', 'rb')
nomecurso = PyPDF2.PdfFileReader(nomecursoPDF)


def rawtext(pdf):
    txt = ''
    for page in range(pdf.numPages-2):
        txt += pdf.getPage(page).extractText()
    return txt.strip()


def text():  # working
    data = rawtext(nomecurso)
    start = data.find(".")
    return data[start+400:-559].strip()  # return just the required data


def splittext():
    data = text()
    res = data.split("\n")  # try splilines() method
    return res


def extractIDandCourse():
    rawnames = splittext()
    rawdata = rawnames[:]
    numandcourse = []
    for i in rawdata:
        if i.isnumeric() or "/" in i:
            numandcourse += i
    return numandcourse  # not working


def idEcourses():  # E == and in portuguese
    data = extractIDandCourse()
    idnumbers = []
    courses = []
    di = {}
    for i in data:
        if i.isnumeric():
            idnumbers += i
        else:
            courses += i
    for r in range(len(courses)):
        di[idnumbers[r]] = courses[r]
    return di  # not working beacuse of extractIDandcourse


rawdata = extractIDandCourse()
dictres = idEcourses().items

print(rawdata[:5], "\n\n", dictres)

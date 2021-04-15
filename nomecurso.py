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
    res = data.splitlines()
    return res


def extractIDandCourse():
    splittedtext = splittext()
    numandcourse = []
    for i in splittedtext:
        if "Sociais-Antropologia" in i:
            numandcourse.append(i)
        if "(" in i or i.isnumeric():
            numandcourse.append(i)
    return numandcourse  # some issues


def idEcourses(debug=False):
    data = extractIDandCourse()
    idnumbers = []
    courses = []
    for i in data:
        if i.isnumeric():
            idnumbers.append(i)
        else:
            courses.append(i)

    coursey = justfornow(courses)
    ids = justID(idnumbers)

    if debug:
        return len(coursey), len(ids)

    di = {"Id": ids, "Course": coursey}
    return di  # It needs len(c) == len(n)


def justID(lista):
    for i in lista:
        if len(i) != 8:
            lista.remove(i)
    return lista


def justfornow(lista):
    xl = ["XYZ" for i in range(46)]
    lista += xl
    return lista

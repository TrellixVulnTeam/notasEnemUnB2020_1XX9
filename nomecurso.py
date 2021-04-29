# %%
import PyPDF2
import json
import re

nomecursoPDF = open('PDFs/nomecurso.PDF', 'rb')
nomecurso = PyPDF2.PdfFileReader(nomecursoPDF)


def rawtext(pdf):
    txt = ''
    for page in range(pdf.numPages-2):
        txt += pdf.getPage(page).extractText()
    return txt.strip()


def text():
    data = rawtext(nomecurso)
    start = data.find(".")
    # return just the required data
    return data[start+400:-559].strip().replace('\n', '')


def candidates(debug=False):
    x = text()
    columns = ['IDs', 'Courses']
    candidates = {}

    idp = re.compile(r'(\d){8}')
    cpc = r'\d\s[A-ZÍíÃãÓóÇÔôÕõÊêÉéÂâÁáÉÚú\s()a-z]+\s/+'
    coursep = re.compile(cpc)
    patterns = [idp, coursep]

    for i in range(len(columns)):
        matches = patterns[i].finditer(x)
        lista = []
        for match in matches:
            value = match.group()
            if i == 0:
                lista.append(value[:])
            elif i == 1:
                lista.append(value[2:])
        if debug:
            print(len(lista), end=', ',)
        candidates[columns[i]] = lista
    return candidates


def splittext():
    data = text()
    res = data.splitlines()
    return res[2:]


def extractIDandCourse():
    splittedtext = splittext()
    numandcourse = []
    for i in range(len(splittedtext)):
        if splittedtext[i].isnumeric() and len(splittedtext[i]) == 8:
            numandcourse.append(splittedtext[i])
        elif numandcourse[-1].isnumeric() and not splittedtext[i].isspace():
            numandcourse.append(splittedtext[i].strip())

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

    if debug:
        return len(courses), len(idnumbers)

    di = {"Id": idnumbers, "Course": courses}
    return di  # It needs len(c) == len(n)


# %%
m = idEcourses()
j = json.dumps(m)

with open('jsons/nomecurso.json', 'w') as f:
    f.write(j)
    f.close()

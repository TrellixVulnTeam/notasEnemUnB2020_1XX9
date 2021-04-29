# %%
import PyPDF2
import json
import re

nomenotaPDF = open("PDFs/nomenota.PDF", "rb")
nomenota = PyPDF2.PdfFileReader(nomenotaPDF)


def rawtext(pdf):
    txt = ''
    for page in range(40, pdf.numPages):
        txt += pdf.getPage(page).extractText()
    return txt.strip()


def text():
    data = rawtext(nomenota).replace('\n', '')
    start = data.find("DIURNO")
    end = data.find("4 das")
    return data[start:end].strip()


def candidates(debug=False):
    x = text()
    columns = ['IDs', 'Grades']
    candidates = {}

    idp = re.compile(r'\d{8},')
    gradep = re.compile(r'\s\d\d\d\.\d\d')
    patterns = [idp, gradep]

    for i in range(len(columns)):
        matches = patterns[i].finditer(x)
        lista = []
        for match in matches:
            value = match.group()
            if i == 0:
                lista.append(value[:8])
            elif i == 1:
                lista.append(value[:])
        if debug:
            print(len(lista), end=', ')
        candidates[columns[i]] = lista
    return candidates


# %%
m = candidates()
j = json.dumps(m)

with open('jsons/nomenota.json', 'w') as f:
    f.write(j)
    f.close()

import PyPDF2
# a ideia é pegar os nomes e os cursos e relacionar-los. Após isso, agrupar por curso, nota e nome.

# get names and courses
nomecursoPDF = open('PDFs/nomecurso.PDF', 'rb')
nomecurso = PyPDF2.PdfFileReader(nomecursoPDF)

# get names and grades
nomenotaPDF = open("PDFs/nomenota.PDF", "rb")
nomenota = PyPDF2.PdfFileReader(nomenotaPDF)


def rawtext():
    nomenotatxt = ''
    for page in range(nomenota.numPages):
        nomenotatxt += nomenota.getPage(page).extractText()
    return nomenotatxt


def text():
    data = rawtext()
    start = data.find("DIURNO")
    end = data.find("4 das")
    return data[start:end].strip()


def candidates():
    data = text()
    candidates = data.split("/").strip()
    return candidates


def teststep1():
    assert text().startswith("ADMINISTRAÇÃO") and text().endswith("-.") == True

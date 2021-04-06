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
    return nomenotatxt.strip()


def text():
    data = rawtext()
    start = data.find("DIURNO")
    end = data.find("4 das")
    return data[start:end].strip()


def rawcandidates():
    data = text()
    candidates0 = data.split("/")
    candidates = candidates0[:-5]
    lastcandl = candidates0[-5].split('.')
    lastcand = lastcandl[0]+lastcandl[1]
    candidates.append(lastcand)
    return candidates


def candidates():
    data = rawcandidates()
    lista = []
    for candidate in data:
        if not candidate[0].isdecimal():
            try:
                candidatel = candidate.split(")")
                realcandidate = candidatel[-1].strip()
                lista.append(realcandidate)
            except:
                candidatel = candidate.split("*")
                realcandidate = candidatel[-1].strip()
                lista.append(realcandidate)
        else:
            lista.append(candidate.strip())
    return lista


def teste():
    res = candidates()
    print(
        f"first element: {res[0]}\nsecond-to-last: {res[-2]}\nlast element: {res[-1]}",)

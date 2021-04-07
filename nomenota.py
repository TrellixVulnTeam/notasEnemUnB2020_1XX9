import PyPDF2
nomenotaPDF = open("PDFs/nomenota.PDF", "rb")
nomenota = PyPDF2.PdfFileReader(nomenotaPDF)


def rawtext(pdf):
    txt = ''
    for page in range(pdf.numPages):
        txt += pdf.getPage(page).extractText()
    return txt.strip()


def text():
    data = rawtext(nomenota)
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
    data = candidates()
    print(f"first element: {data[0]}\nlast element: {data[-1]}")

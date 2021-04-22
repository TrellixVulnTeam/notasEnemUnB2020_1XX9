# %%
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
    data = text().replace(' \n-\n,', '').replace('\n-', '').replace('\n', '')
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
            except Exception:
                # except Exception lets me use control+c to stop the code
                candidatel = candidate.split("*")
                realcandidate = candidatel[-1].strip()
                lista.append(realcandidate)
        else:
            lista.append(candidate.strip())
    return lista


def todic(debug=False):
    pessoas = candidates()
    IDs = []
    grades = []
    for candidate in pessoas:
        wds = candidate.split(',')
        IDs.append(fixID(wds[0].strip()))
        for wd in wds:
            pl = wd.strip()
            if len(pl) >= 6 and wds[0] != wd and wd != wds[1] and wd != "(BACHARELADO":
                grades.append(fixgrade(pl))
    dic = {'IDs': IDs, 'Grades': grades}

    if debug:
        return len(IDs), len(grades)

    return dic


def fixgrade(grade):
    if len(grade) > 6:
        x = grade.split()
        for i in x:
            if len(i) == 6:
                return i
    elif len(grade) == 6:
        return grade
    else:
        return None


def fixID(ID):
    if len(ID) > 8:
        x = ID.split()
        return x[-1].strip()
    else:
        return ID

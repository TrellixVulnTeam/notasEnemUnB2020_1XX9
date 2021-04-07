import PyPDF2


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
    return data[start+400:-559].strip()  # return just the interested data


def teste():
    data = text()
    print(data)
    print(
        f"***First 200 string elements: {data[:200]}\n***Last 200 string elements: {data[-200:]}")


teste()

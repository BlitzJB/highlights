from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def convert_pdf_to_html(pdf_bytes):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    device = HTMLConverter(rsrcmgr, retstr, laparams=LAParams(), showpageno=False) 
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(pdf_bytes):
        interpreter.process_page(page)
    return retstr.getvalue()

# open('dump.html', 'w').write(convert_pdf_to_html(open('merged.pdf', 'rb')))
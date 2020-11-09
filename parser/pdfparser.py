import io

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from utilities.misc import bugprint


# Parse the PDF file and store results in the dictionary
# Dictionary: {page_number: page_text}
class PDFParser:
    pages = dict()

    def __init__(self):
        pass

    def read_pages(self, filename):
        fp = open(filename, 'rb')
        resource_manager = PDFResourceManager()
        return_str = io.StringIO()
        device = TextConverter(resource_manager, return_str, codec='utf-8', laparams=LAParams())
        interpreter = PDFPageInterpreter(resource_manager, device)
        for page_number, page in enumerate(PDFPage.get_pages(fp)):
            interpreter.process_page(page)
            data = return_str.getvalue()
            self.pages[page_number] = data
            data = ''
            return_str.truncate(0)
            return_str.seek(0)

    def get_pages(self):
        return self.pages

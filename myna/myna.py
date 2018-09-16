import six

import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTLine, LTTextBoxHorizontal
from pdfminer.converter import PDFPageAggregator

# Uses pdfminer.six fork of pdfminer (https://euske.github.io/pdfminer/index.html)


# Open a PDF document.
# fp = open('./myna/Configuration-Profile-Reference.pdf', 'rb')
# parser = PDFParser(fp)
# document = PDFDocument(parser, None)
#
# # Get the outlines of the document.
# outlines = document.get_outlines()
# for (level,title,dest,a,se) in outlines:
#     print (level, title)
#
#
# from pdfminer.layout import LAParams
# from pdfminer.converter import PDFPageAggregator

# Open a PDF file.
fp = open('./myna/Configuration-Profile-Reference.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser, None)
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed


# # Get the outlines of the document.
# outlines = document.get_outlines()
# for (level,title,dest,a,se) in outlines:
#     print (level, title, dest, a, se)
#
# sys.exit(0)

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
device = PDFDevice(rsrcmgr)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)


# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    lines = []  # Lines by y0
    within_lines = {}

    # First Pass: Lines
    for obj in layout:
        # print(obj)
        if isinstance(obj, LTLine):
            lines.append(obj.y0)
            #if obj.linewidth > 0.7:  # Thicker line above Key, Type, Value
            #    print(obj.linewidth)

    # Second Pass: TextBoxes nearest lines
    for obj in layout:
        if isinstance(obj, LTTextBoxHorizontal):
            for yl in lines:
                if abs(obj.y0 - yl) < 30:
                    within_lines[obj.y0] = obj.get_text()

    print(within_lines)

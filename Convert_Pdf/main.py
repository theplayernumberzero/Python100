from pdf2docx import Converter

pdf_file = "./Pdf_files/ornek_pdf.pdf"
converted_file = "./Docx_files/converted.docx"

cv = Converter(pdf_file=pdf_file)
cv.convert(converted_file)
cv.close()
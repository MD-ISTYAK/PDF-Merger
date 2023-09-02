import PyPDF2

pdfiles=["my1.pdf", "my1.pdf"]
merger=PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile=open(filename,'rb')
    pdfReader= PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')
#Tomado de https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/

# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('articulo.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
texto = (pageObj.extractText())

print(texto)

# crear documento de texto
f = open('doc-nuevo.txt','a')
f.write(texto)
      
# closing the pdf file object
pdfFileObj.close()


# cerrando archivo de texto
f.close()

      

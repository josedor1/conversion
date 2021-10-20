from typing import TextIO
import shutil
import PyPDF2

pdfFileobj = open('Resolución 000114 de 14-10-2021.pdf', 'rb')  # Abra el archivo en formato binario de solo lectura
pdfReader = PyPDF2.PdfFileReader(pdfFileobj)  # Obtener objeto de contenido
print('El documento tiene', pdfReader.numPages, ' Páginas')  # Imprimir páginas PDF

documento = pdfReader.getPage(0)  # Obtener página comienza desde 0, es decir, 0 significa la primera página en PDF


f: TextIO = open('borrador.txt', 'a')  # abrimos el archivo donde se guarda el texto hallado
f.write(documento.extractText())  # almacena la cadena de texto extraida del PDF en un archivo txt
pdfFileobj.close()
f.close()

p = open('borrador.txt', 'r').read().find('RESOLUCIÓN') # abrimos el archivo para lectura de informacion

if p > 0: # Preguntamos si se encontró la información
    print('el documento es una resolución')
    f = open("borrador.txt", "w")# Se abre el archivo de texo en modo de lectura para que se borre la informacion
    f.close()
    m = shutil.move("Resolución 000114 de 14-10-2021.pdf", "Resolucion/Resolución 000114 de 14-10-2021.pdf") # movemos el documento a la carpeta definitiva según tipo
import urllib.request
from bs4 import BeautifulSoup

direccion = input("Enter - ")

codigo = urllib.request.urlopen(direccion)
bea = BeautifulSoup(codigo)

etiqueta = bea('a')

# Abre el archivo "datos.txt" en modo escritura
with open("datos.txt", "w") as archivo:
    archivo.write("Enlaces pagina principal\n")
    for x in etiqueta:
        archivo.write("Direccion enlace principal: " + str(x.get('href')) + "\n")

    archivo.write("\nEnlaces en las paginas secundarias:\n\n")

    for x in etiqueta:
        nueva_url = x.get('href', None)
        archivo.write('Accediendo a los enlaces dentro de la pagina: ' + str(nueva_url) + "\n")
        try:
            if nueva_url[0:10] == 'http':
                codigo2 = urllib.request.urlopen(nueva_url)
            else:
                codigo2 = urllib.request.urlopen(direccion + nueva_url)
            bea2 = BeautifulSoup(codigo2)
            nueva_etiqueta = bea2('a')

            if len(nueva_etiqueta) > 0:
                archivo.write(str(nueva_etiqueta) + 'enlaces:\n')
                for y in nueva_etiqueta:
                    archivo.write("Direccion enlace secundario: " + str(y.get('href')) + "\n")

            else:
                archivo.write("No hay mas enlaces\n")
        except:
            archivo.write("No hay mas enlaces\n")

print("Los datos se han guardado en 'datos.txt'")

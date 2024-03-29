import xml.etree.ElementTree as ET


class Lectura:
    
    def __init__(self) -> None:
        pass

    #CREATE MATRIZ
    def create(filas,columnas,mat):
        for i in range(filas):
            mat.append([0]*columnas)
        
        return mat


    #RECORRIDO DE LA MATRIZ
    def datos(ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        name = ''
        rows = ''
        column = ''
        x = ''
        y = ''
        content = ''
        
        for elem in root:
            matrix = []
            name = elem.attrib['name']
            rows = elem.attrib['n']
            column = elem.attrib['m']
            
            
            Lectura.create(int(rows),int(column),matrix)
            for subelem in elem:
                x = subelem.attrib['x']
                y = subelem.attrib['y']
                content = subelem.text
                
                matrix[int(x)-1][int(y)-1] = int(content)

            diccionario = {'Nombre':name,'filas':rows,'columnas':column,'matriz':matrix}

            datos.append(diccionario) 

        print('\n******************************* Lectura Exitosa *******************************')

        return datos
        


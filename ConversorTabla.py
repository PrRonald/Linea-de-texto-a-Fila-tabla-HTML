def conversor_Texto_Tabla_HTML (linea):
    Corte_str = linea.find(":")

    comando = "<td> " + linea[0:Corte_str] + " </td>"
    funcion = "<td> " + linea[Corte_str + 1:len(linea)]  + " </td>"
    fila = """    <tr>
        {}
        {}
    </tr> """.format(comando, funcion)
     
    print(fila)



if __name__ == "__main__":
    texto_a_fila = input("Introducir texto a convertir a fila de columna HTML: ")
    conversor_Texto_Tabla_HTML(texto_a_fila)
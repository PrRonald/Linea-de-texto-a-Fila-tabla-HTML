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
    while True:
        texto_a_fila = input("""Introducir texto a convertir a fila de columna HTML. 
                                    si desea salir introdusca 1: """)
        if texto_a_fila != "1":
            conversor_Texto_Tabla_HTML(texto_a_fila)
        elif texto_a_fila == "1":
            break
 
 #dar alerta de un numero distinto de 1
 
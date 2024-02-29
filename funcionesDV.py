def flipper(obj:str)->str:
    """toma un string y el objeto del primer indice lo deja en el último, así sucesivamente
    ej : flipper("juan")="nauj"
    """
    if type(obj)!=str:
        raise ValueError(f"'{obj}' no es de tipo {str}")
    
    flipped=""
    for letter in obj:
        flipped=letter+flipped

    return flipped

def ponderador(texto:str,ponderadora:list[int])->int:
    """Recibe un string casteable a int, para luego multiplicar cada numero por una lista ponderadora
    """
    suma=0
    i=0
    j=0
    while i < len(texto):
        digito=int(texto[i])
        if j>=len(ponderadora):
            j=0
        suma+=(digito*ponderadora[j])
        i+=1
        j+=1
    return suma


def DigitoVerificador(RUT:int)->str:
    """ Calcula el digito verificador de un numero dado
    """
    if type(RUT)!=int:
        raise ValueError(f"'{RUT}' no es de tipo {int}")
    
    strRut=str(RUT)
    flipped=flipper(strRut)
    res=ponderador(flipped,[2,3,4,5,6,7])
    res=11-res%11
    if res==11:
        res=0
    elif res==10:
        res='k'
    return str(res)


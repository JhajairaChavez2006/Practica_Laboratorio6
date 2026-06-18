def validar_correo(correo):
    """
    Valida si una cadena tiene formato de correo electrónico.
    Parámetros:
        correo (str): Correo a validar.
    Retorna:
        bool: True si es válido, False si no lo es.
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, correo))
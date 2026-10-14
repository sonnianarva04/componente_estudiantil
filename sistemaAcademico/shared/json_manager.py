import json
import os


class GestorJSON:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer(self):
        # Si el archivo no existe o está vacío (0 bytes), devuelve []
        if not os.path.exists(self.archivo) or os.path.getsize(self.archivo) == 0:
            return []

        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            # Si el JSON está mal formateado o corrupto, evita que el programa colapse
            return []

    def guardar(self, datos):
        carpeta = os.path.dirname(self.archivo)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        with open(self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
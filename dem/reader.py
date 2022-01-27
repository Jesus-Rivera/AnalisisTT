import fitz
import re

class Reader:

    pages = 0
    u_pages = 0

    _sheets = []
    
    def __init__(self,direction):
        self._file = fitz.open(direction)
        self.pages = self._file.pageCount
        for i in range(0,self.pages):
            sheet = self._get_sheetData(self._file,i)
            aux = self._clean(sheet)
            if self._approve_text(aux):
                self._sheets.append(aux)
        self._file.close()
        self.u_pages = len(self._sheets)

    def _get_sheetData(self,file,sheet):
        page = file.load_page(sheet)
        text = page.get_text("text")
        return text

    def _clean(self,text):
        # Eliminar separadores
        new_text = re.sub(r"__+", ' ', text)
        new_text = re.sub(r"--+", ' ', new_text)
        
        #Eliminar encabezados, pies de pagina y numero
        i = 0
        jump = 0
        
        while ord(new_text[i]) < 49 or ord(new_text[i]) > 57:
            if new_text[i] == "\n":
                jump += 1
                if jump >= 2:
                    #new_text = "\n" + new_text[:]
                    i = 0
                    break
            i += 1

        new_text = new_text[i:]
        new_text = new_text[new_text.index("\n") + 1:]

        #Eliminar informacion de contacto, fechas y horas
        new_text = re.sub(r"[0-9]+:[0-9]+:[0-9]+ ?", ' ', new_text)
        new_text = re.sub(r"[0-9]+/[0-9]+/[0-9]+ ?", ' ', new_text)
        new_text = re.sub(r"[0-9]*-[0-9-]*-?", ' ', new_text)
        new_text = re.sub(r"[a-zA-Z0-9_]+[a-zA-Z0-9_.]*@[a-zA-Z]+.[a-zA-Z]+[.a-zA-Z]*", ' ', new_text)
        new_text = re.sub(r"https?://[A-Za-z0-9./]+", ' ', new_text)
        new_text = re.sub(r"www.[A-Za-z0-9./]+", ' ', new_text)

        
        #Eliminar posibles indices
        new_text = re.sub(r"[a-zA-Z0-9.,;: áéíóúÁÉÍÓÚ \n ñÑ¿?¡!]+[.]{4,} ?[0-9]{1,3}", ' ', new_text)
        
        #Eliminar simbolos innecesarios
        #new_text = re.sub(r'[^0-9a-zA-Z.¡!¿?_(),\náéíóú \-"]', ' ', new_text)

        #Eliminar espacios y saltos de linea de mas
        #new_text = re.sub(r"\n+", ' ', new_text)
        new_text = re.sub(r"\t+", ' ', new_text)
        new_text = re.sub(r" +", ' ', new_text)
        return new_text

    def _approve_text(self,text):
        new_text = re.sub(r"\n+", ' ', text)
        new_text = re.sub(r" +", ' ', new_text)
        if len(new_text) > 200:
            return True
        else:
            return False
    
    def get_data_page(self,page):
        return self._sheets[page]

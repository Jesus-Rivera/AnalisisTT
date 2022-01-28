import re

class Tokenizer:

    parags = []
    sentences = []
    _text = ''

    def load_text(self,text):
        self._text = text
        self._make_sections()
        return self.parags

    def _make_sections (self):
        aux = self._text
        bandera = True

        while(bandera == True):
            exp = re.search(r'[\.|…]\n\D',aux)
            if exp is None:
                print(len(aux))
                if len(aux) > 25:
                    self.parags.append(aux)
                bandera = False
            else:
                begin = exp.start()
                new_section = aux[:begin + 1]
                self.parags.append(new_section)
                aux = aux[begin + 2:]

        
#start()
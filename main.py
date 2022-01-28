
from dem.reader import Reader
from dem.tokenizer import Tokenizer

book = '../data/books/poemas.pdf'
read = Reader(book)


page = int(input('Pagina a segmentar: '))

toks = Tokenizer()

aux = toks.load_text(read.get_data_page(page))

for i in aux:
    print(i)
    print('-------------------------------')

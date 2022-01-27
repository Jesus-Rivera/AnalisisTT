
from dem.reader import Reader

book = 'data/books/poemas.pdf'
read = Reader(book)


print('Paginas en el libro: '+ str(read.pages))
print('Paginas utililizadas: '+ str(read.u_pages))

print(read.get_data_page(int(input('Pagina: '))))
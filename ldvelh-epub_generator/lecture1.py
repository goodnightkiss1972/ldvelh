from ebooklib import epub

book = epub.read_epub('../_external_ressources/epub1/perroquet.epub')

print(book.get_metadata('DC', 'creator'))
print(book.get_metadata('DC', 'publisher'))
print(book.get_metadata('DC', 'date'))

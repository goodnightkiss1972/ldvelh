from ebooklib import epub, ITEM_DOCUMENT

book = epub.read_epub('../_external_ressources/epub1/perroquet.epub')

for bookitems in book.get_items_of_type(ITEM_DOCUMENT):
    print(bookitems.file_name)


from BookDao import bookDao

book1 = {
    'ISBN': 1234567,
    'price': 12,
    'author': 'jk',
    'title': 'some fantasy book'

}
book2 = {
    'ISBN': 2321345,
    'price': 333,
    'author': 'mary',
    'title': 'had a little lamb'

}

#returnValue = bookDao.create(book2)
#returnValue = bookDao.getAll()
##print(returnValue)
#returnValue = bookDao.findById(book2['ISBN'])
#print("find By Id")
#print(returnValue)
returnValue = bookDao.update(book2)
#print(returnValue)
#returnValue = bookDao.findById(book2['ISBN'])
print(returnValue)
#returnValue = bookDao.delete(book2['ISBN'])
#print(returnValue)
#returnValue = bookDao.getAll()
print(returnValue)

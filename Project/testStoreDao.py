from storeDao import StoreDao

product1 = {
    'productName': "Crisps",
    'productType': 'Food',
    'productPrice': '4.95'

}
product2 = {
    'productName': "somethingNice",
    'productType': ' not durable',
    'productPrice': '22'

}
returnValue = StoreDao.insert(StoreDao,product1)
#print(returnValueC)
#returnValue = StoreDao.create(StoreDao,product1)
#returnValue = StoreDao.getAll(StoreDao)
#returnValue = StoreDao.convertToDict(StoreDao)
#print(returnValue)

#returnValue = StoreDao.findById(StoreDao,'somethingNice')
#print("find By Id")
#print(returnValue)

#returnValue = StoreDao.update(StoreDao, product2)
#print(returnValue)
#returnValue = bookDao.findById(book2['ISBN'])
#print(returnValue)
#StoreDao.delete(StoreDao, product1['productName'])
##returnValue = StoreDao.getAll(StoreDao)
#print(returnValue)
print(returnValue)

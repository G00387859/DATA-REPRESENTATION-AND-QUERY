from storeDao import StoreDao

product1 = {
    'productName': "Cheese",
    'productType': 'Food',
    'productPrice': '4.95'

}
product2 = {
    'productType': "meat",
    'productName': 'lamb',
    'productPrice': '12.99'

}
returnValue = StoreDao.insert(StoreDao,product2)
#print(returnValueC)
#returnValue = StoreDao.create(StoreDao,product1)
#returnValue = StoreDao.getAll(StoreDao)
#returnValue = StoreDao.convertToDict(StoreDao)
#print(returnValue)

#returnValue = StoreDao.findById(StoreDao,"potatoes")
#print("find By Id")
#print(returnValue)

#returnValue = StoreDao.update(StoreDao, product2)
#print(returnValue)
#returnValue = bookDao.findById(book2['ISBN'])
#print(returnValue)
#returnValue = StoreDao.delete(StoreDao, product1['productName'])
##returnValue = StoreDao.getAll(StoreDao)
print(returnValue)
#x = returnValue.get('id')
#returnValue["id"] = 2018
#print(returnValue)

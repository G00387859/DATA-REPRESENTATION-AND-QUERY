def convertToDict(self, result):

for result in results:
            colnames = ['productName','productType','productPrice']
            book = {}
            if result:
               
                for i , colName in enumerate(colnames):
                    value = result[i]
                    book[colName] = value
                #print(book)
            returnArray.append(book)
        return book
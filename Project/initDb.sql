/*productType == Durable :television, refrigerator, clothes, machines,
                 Consumer :salt, pepper, soap, etc,
                 Industrial Products : wheat, cotton, livestock, vegetables, fruits, - crude oil, fish, timber, metal.
                 ref: https://www.businessmanagementideas.com/products/types-of-product/20612. 
                 How reliable this? I dont know. 
                  */
use datarepresentation;
CREATE TABLE store (
    -> id int NOT NULL auto_increment,
    -> productType VARCHAR(100),
    -> productName varchar(100),
    -> productPrice int(4),
    -> PRIMARY KEY(id)
    -> );
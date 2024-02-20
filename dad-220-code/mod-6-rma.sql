mysql -u root -p

create table Customers  ( CustomerID INT PRIMARY KEY, FirstName VARCHAR(25), LastName VARCHAR(25), Street VARCHAR(50), City VARCHAR(50), State VARCHAR(25), ZipCode VARCHAR(10), Telephone VARCHAR(15) );

create table Orders  ( OrderID INT PRIMARY KEY, CustomerID INT, SKU VARCHAR(20), Description VARCHAR(50), FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) );

create table RMA  ( RMAID INT PRIMARY KEY, OrderID INT, Step VARCHAR(50), Status VARCHAR(15), Reason VARCHAR(15), FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) );

LOAD DATA INFILE '/home/codio/workspace/customers.csv' INTO TABLE Customers FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/codio/workspace/orders.csv' INTO TABLE Orders FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/codio/workspace/rma.csv' INTO TABLE RMA FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

# I used a combination of SELECT, COUNT, AS, FROM, JOIN, ON, WHERE, & AND. They are all keywords, clauses and operators. I needed to reference two tables.

SELECT COUNT(Orders.orderID) as FraminghamMAOrders FROM Orders JOIN Customers ON Customers.customerID = Orders.CustomerID WHERE Customers.city = 'Framingham' AND Customers.state = 'Massachusetts';

SELECT COUNT(Customers.customerID) as CustomersFromMA FROM Customers WHERE Customers.state = 'Massachusetts';

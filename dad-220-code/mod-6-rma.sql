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


INSERT INTO Customers (CustomerID, FirstName, LastName, Street, City, State, ZipCode, Telephone) VALUES 
(100004, 'Luke', 'Skywalker', '15 Maiden Lane', 'New York', 'NY', '10222', '212-555-1234'), 
(100005, 'Winston', 'Smith', '123 Sycamore Street', 'Greensboro', 'NC', '27401', '919-555-6623'), 
(100006, 'MaryAnne', 'Jenkins', '1 Coconut Way', 'Jupiter', 'FL', '33458', '321-555-8907'), 
(100007, 'Janet', 'Williams', '55 Redondo Beach Blvd', 'Torrence', 'CA', '90501', '310-555-5678');

select * from Customers where Customers.CustomerID IN (100004, 100005, 100006, 100007);

INSERT INTO Orders (OrderID, CustomerID, SKU, Description) VALUES 
(1204305, 100004, 'ADV-24-10C', 'Advanced Switch 10GigE Copper 24 port'), 
(1204306, 100005, 'ADV-48-10F', 'Advanced Switch 10 GigE Copper/Fiber 44 port co...'), 
(1204307, 100006, 'ENT-24-10F', 'Enterprise Switch 10GigE SFP+ 24 Port'), 
(1204308, 100007, 'ENT-48-10F', 'Enterprise Switch 10GigE SFP+ 48 port');

select * from Orders where Orders.CustomerID IN (100004, 100005, 100006, 100007);



select count(CustomerID) as WsRICs FROM Customers where City = 'Woonsocket' AND State = 'Rhode Island';



select Status, Step from RMA where OrderID = 5175;
update RMA set Status = 'Complete', Step = 'Credit Customer Account' where OrderID = 5175;
select Status, Step from RMA where OrderID = 5175;	



select * from RMA where Reason = 'Rejected';
delete from RMA where Reason = 'Rejected';





show tables;
describe Customers;
describe Orders;

select CONSTRAINT_NAME from INFORMATION_SCHEMA.KEY_COLUMN_USAGE where TABLE_NAME = 'Orders' and CONSTRAINT_SCHEMA = 'QuantigrationUpdates' and REFERENCED_TABLE_NAME is not null;
alter table Orders drop foreign key Orders_ibfk_1;

alter table Customers change CustomerID CollaboratorID int;

rename table Customers to Collaborators;
describe Collaborators;

alter table Orders change CustomerID CollaboratorID int;
describe Orders;

select TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
from INFORMATION_SCHEMA.KEY_COLUMN_USAGE
where REFERENCED_TABLE_SCHEMA = 'QuantigrationUpdates' and REFERENCED_TABLE_NAME = 'Collaborators';

alter table Orders add constraint CollaboratorID foreign key (CollaboratorID) references Collaborators(CollaboratorID);
describe Orders;
select TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
from INFORMATION_SCHEMA.KEY_COLUMN_USAGE
where REFERENCED_TABLE_SCHEMA = 'QuantigrationUpdates' and REFERENCED_TABLE_NAME = 'Collaborators';





select * into outfile '/home/codio/workspace/orders-2024-feb-20-update.csv' fields terminated by ',' lines terminated by '\n' from Orders;
exit;
ls
sudo chmod 777 orders-2024-feb-20-update.csv


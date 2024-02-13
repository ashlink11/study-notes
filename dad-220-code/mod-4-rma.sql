`pwd` 

LOAD DATA INFILE '/home/codio/workspace/customers.csv' INTO TABLE Customers FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 

 

D.	LOAD DATA INFILE '/home/codio/workspace/orders.csv' INTO TABLE Orders FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 

 

E.	LOAD DATA INFILE '/home/codio/workspace/rma.csv' INTO TABLE RMA FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 

i.	SELECT COUNT(Orders.orderID) as NumFraminghamOrders FROM Orders JOIN Customers ON Customers.customerID = Orders.CustomerID WHERE Customers.city = 'Framingham' AND Customers.state = 'Massachusetts';


i.	SELECT COUNT(Customers.customerID) as NumMACustomers FROM Customers WHERE Customers.state = 'Massachusetts';

ii.	INSERT INTO Customers (CustomerID, FirstName, LastName, Street, City, State, ZipCode, Telephone) VALUES (100004, 'Luke', 'Skywalker', '17 Maiden Lane', 'New York', 'NY', '10222', '212-555-1234'), (100005, 'Winston', 'Smith', '128 Sycamore Street', 'Greensboro', 'NC', '27401', '919-555-6623'), (100006, 'MaryAnne', 'Jenkins', '2 Coconut Way', 'Jupiter', 'FL', '33458', '321-555-8907'), (100007, 'Janet', 'Williams', '58 Redondo Beach Blvd', 'Torrence', 'CA', '90501', '310-555-5678');
iii.	select * from Customers where Customers.CustomerID IN (100004, 100005, 100006, 100007);

v.	INSERT INTO Orders (OrderID, CustomerID, SKU, Description) VALUES (1204305, 100004, 'ADV-24-10C', 'Advanced Switch 10GigE Copper 24 port'), (1204306, 100005, 'ADV-48-10G', 'Advanced Switch 10GigE Copper/Fiber 44 port coppe'), (1204307, 100006, 'ENT-24-10F', 'Enterprise Switch 10GigE SFP+ 24 Port'), (1204308, 100007, 'ENT-48-10F', 'Enterprise Switch 10GigE SFP+ 48 Port');
vi.	select * from Orders where Orders.CustomerID IN (100004, 100005, 100006, 100007);

 

 

i.	select count(CustomerID) as WoonsocketRICustomers FROM Customers where City = 'Woonsocket' AND State = 'Rhode Island';
ii.	select count(CustomerID) as WoonsocketRICustomers FROM Customers where City = 'Woonsocket';

 


1.	select Status, Step from RMA where OrderID = 5175;	

 

1.	update RMA set Status = 'Complete', Step = 'Credit Customer Account' where OrderID = 5175;
2.	select Status, Step from RMA where OrderID = 5175;	


1.	select * from RMA where Reason = 'Rejected';
2.	delete from RMA where Reason = 'Rejected';

i.	select * into outfile '/home/codio/workspace/updated-orders.csv' fields terminated by ',' lines terminated by '\n' from Orders;
ii.	chmod 777 updated-orders.csv
iii.	cat updated-orders.csv

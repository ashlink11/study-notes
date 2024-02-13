
•	Just running `mysqlsampledatabase.sql` in either the mysql terminal or in the Ubuntu terminal leads to errors and doesn’t create the new database with its tables and records.
•	First I exited mysql to the Ubuntu terminal with `exit;`. I didn’t know my username and password. So, I viewed all the system usernames with `cut -d: -f1 /etc/passwd` and assumed I was the root user since I think I’d noticed it while using Codio. Then I changed the password with `sudo passwd root`. Then I went into mysql with `mysql -u root -p` and did `create database classicmodels;`, then `exit;`, then `mysql -u root -p classicmodels < mysqlsampledatabase.sql`. Then my classicmodels db was populated in mysql and I could `use classicmodels;` and `show tables;`. (I might’ve been able to use the `source` command which I saw in mysql `help`.

a.	select firstName, lastName, jobTitle, offices.city from employees inner join offices on employees.officeCode = offices.officeCode where state = 'CA';

c.	select firstName, lastName, jobTitle, offices.city from employees inner join offices on employees.officeCode = offices.officeCode where state = 'NY';

a.	select * from orders where orderNumber IN (10330, 10338, 10194);

a.	describe payments;
b.	select * from payments where customerNumber = 103;

c.	delete from payments where customerNumber = 103;
d.	select * from payments;

a.	select * from customers inner join employees on customers.salesRepEmployeeNumber = employees. employeeNumber where employees.employeeNumber = 1504;


a.	select employeeNumber, firstName, lastName, customers.customerNumber, customers.customerName, customers.contactLastName, customers.contactFirstName, customers.phone, customers.addressLine1, customers.addressLine2, customers.city, customers.state, customers.postalCode, customers.country, customers.creditLimit from employees inner join customers on employees.employeeNumber = customers.salesRepEmployeeNumber inner join offices on employees.officeCode = offices.officeCode where offices.state = 'NY';


a.	insert into customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit) VALUES (101, 'LLC', 'A', 'B', '2223334444', 'River Rd', NULL, 'M', 'NY', '55555', 'USA', 1188, 10000.00);
b.	select * from customers;

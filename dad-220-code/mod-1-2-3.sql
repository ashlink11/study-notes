select * from collaborator limit 5;

insert into Customers (CustomerID, FirstName, LastName, Street, City, State, ZipCode, Telephone) VALUES (01, ‘amy’, ‘anthony’, ‘1 apple way’, ‘albaquerque’, ‘arizona’, ‘00001’, ‘1111111111’),  (02, 'bill', 'jones', '2 basket way', 'boston', 'ma', '00002', '2222222222');

alter table description rename details;

create view Collaborator as select CustomerID as CollaboratorID, FirstName AS FirstName, LastName as LastName, Street as Street, City as City, State as State, ZipCode as ZipCode, Telephone as Telephone from Customers;

describe Collaborator;

select * from Collaborator limit 5;

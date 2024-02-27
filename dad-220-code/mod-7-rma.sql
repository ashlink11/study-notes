select Customers.State as State, count(RMA.RMAID) as Returns_Per_State 
from 
	(select distinct State, CustomerID from Customers) Customers 
left join 
	Orders on Customers.CustomerID = Orders.CustomerID 
left join 
	RMA on Orders.OrderID = RMA.OrderID 
group by 
	Customers.State
order by
	Returns_Per_State desc;




select 
	Orders.SKU,
	count(RMA.RMAID) as Num_of_Returns,
	round(count(RMA.RMAID) * 100.0 / (select count(*) from RMA), 2) as Percentage_of_Total_Returns
from
	Orders
left join
	RMA on Orders.OrderID = RMA.OrderID
group by
	Orders.SKU;




select Customers.State as State, count(RMA.RMAID) as Returns_Per_State 
from 
	(select distinct State, CustomerID from Customers) Customers 
left join 
	Orders on Customers.CustomerID = Orders.CustomerID 
left join 
	RMA on Orders.OrderID = RMA.OrderID 
group by 
	Customers.State
order by
	Returns_Per_State desc
into outfile '/home/codio/workspace/rma-returns-per-state.csv' 
fields terminated by ',' 
lines terminated by '\n' ;




select 
	Orders.SKU,
	count(RMA.RMAID) as Num_of_Returns,
	round(count(RMA.RMAID) * 100.0 / (select count(*) from RMA), 2) as Percentage_of_Total_Returns
from
	Orders
left join
	RMA on Orders.OrderID = RMA.OrderID
group by
	Orders.SKU
into outfile '/home/codio/workspace/rma-percent-of-total-returns.csv' 
fields terminated by ',' 
lines terminated by '\n';

ls
sudo chmod 777 rma-returns-per-state.csv
sudo chmod 777 rma-percent-of-total-returns.csv









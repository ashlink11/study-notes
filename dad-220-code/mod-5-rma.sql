select Customers.State, count(distinct Customers.CustomerID) AS customerCount, count(Orders.OrderID) as orderCount from Customers left join Orders on Customers.CustomerID = Orders.CustomerID group by Customers.State; 

 

select SKU, count(*) as skuCount from Orders group by SKU order by skuCount desc;

 
select * from Orders;

 

select SKU, count(*) as skuCount from Orders group by SKU order by skuCount desc;

 

select Orders.SKU, count(*) as skuCount from Orders join (select * from Customers where State in ('North
 Carolina', 'Georgia', 'Virginia', 'South Carolina')) Customers on Orders.CustomerID = Customers.CustomerID gro
up by Orders.SKU order by skuCount desc;
 

select Orders.SKU, count(*) as numReturnedOrders from RMA join Orders
on RMA.OrderID = Orders.OrderID group by Orders.SKU order by numReturnedOrders desc;


 

select count(*) as RMAcount from RMA;
select count(*) as Ordercount from Orders;



select Orders.SKU, count(*) as numReturnedOrdersNW  from (select * from Customers where State in ('Oregon', 'Idaho', 'Montana', 'Washington')) as Customers join Orders on Customers.CustomerID = Orders.CustomerID join RMA on
Orders.OrderID = RMA.OrderID  group by Orders.SKU  order by numReturnedOrdersNW desc;

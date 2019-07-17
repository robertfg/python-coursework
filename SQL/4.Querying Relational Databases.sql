/*  **********  QUERYING RELATIONAL DATABASES **********  */

/*  ***** Joining Table Data with SQL  ***** */

/*  JOIN Queries */

-- Code Challenge
select md.ModelName, c.VIN, c.StickerPrice FROM MODEL md
INNER JOIN Car c ON c.ModelID = md.ModelID

select mk.MakeName, md.ModelName, c.VIN, c.StickerPrice FROM MODEL md
INNER JOIN Car c ON c.ModelID = md.ModelID
INNER JOIN Make mk ON mk.MakeID = md.MakeID

select firstname, lastname, saleamount from sale sa
inner join salesrep sr on sr.salesrepid = sa.salesrepid

select modelname, vin from model md
left outer join car on car.modelid = md.modelid

select sa.saledate, sa.saleamount, sr.firstname, sr.lastname from sale sa
left outer join salesrep sr on sr.salesrepid = sa.salesrepid


/*  ***** SET Operations  ***** */

/*  SET Operations  */

-- Code Challenge
select name from fruit union select name from vegetable

select name from fruit where substr(name, 1, 1) between 'A' and 'K'
union
select name from vegetable where substr(name, 1, 1) between 'A' and 'K'

-- include duplicates
select name from fruit
union all
select name from vegetable order by name

-- both fruit and vegetable
select name from fruit
intersect
select name from vegetable order by name

-- fruits not considered vegetables
select name from fruit
except
select name from vegetable order by name

-- vegetables not considered fruits
select name from vegetable
except
select name from fruit order by name

/*  ***** Subqueries  ***** */

-- Code Challenge
select modelname from model
where modelid in (select modelid from car where stickerprice > 30000)

select * from sale
where carid in (select carid from car where stickerprice > 30000)

select * from sale where customerid in (select customerid from customer where gender = 'F')

-- select all columns from sale table for female customers
select * from sale
inner join
(select customerid from customer where gender = 'F') as cust
on cust.customerid = sale.customerid



/*  **********  SQL BASICS **********  */

/*  ***** Getting Data from a Database  ***** */

/*  First SQL Statement */

-- Code Challenge
SELECT * FROM products;
SELECT * FROM users;
SELECT * FROM customer_addresses;
SELECT * FROM phone_book;
SELECT * FROM results;


/*  Retrieving Columns of Information */

-- Code Challenge
select first_name, last_name from users;
select name from products;
select street, city, state, zip from customer_addresses;
select phone from phone_book;
select first_name, last_name from phone_book;


/*  Categorizing Output with AS */

-- Code Challenge
select name as "Product Name", description as "Product Description" from products;
select username as "Username", first_name as "First Name", last_name as "Last Name" from users;
select first_name as "First Name", last_name as "Last Name", phone as "Phone Number" from phone_book;
select home_team as "Home Team", home_score as "Home Score", away_team as "Away Team", away_score as "Away Score", played_on as "Date Played" from results;


/*  ***** Finding the Data You Want ***** */

/*  Searching Tables with Where */

-- Code Challenge
select first_name, last_name from users where username = "wig_lady";
select * from products where price != 9.99;
select username from users where last_name="Chalkley";


/*  Filtering by Comparing Values */

-- Code Challenge
select * from results where home_score > 12;
select * from results where away_score < 10;
select * from products where price <= 10.99;


/*  Filtering by More than One Condition  */

-- Code Challenge
select * from results where away_team = "Hessle" and away_score > 18;
select * from users where last_name = "Hinkley" or last_name = "Pettit";


/*  Filtering by Dates  */

-- Code Challenge
select * from results where away_team = "Hessle" and played_on >= "2015-10-01";


/*  Searching Within a Set of Values  */

-- Code Challenge
select * from products where price in (7.99, 9.99, 11.99);
select * from users where username in ("2spooky4me", "beard_man");


/*  Searching Within a Range of Values  */

-- Code Challenge
select * from products where price between 10.99 and 12.99;  
select * from results where played_on between "2015-09-01" and "2015-09-30";


/*  Finding Data that Matches a Pattern */

-- Code Challenge
select * from products where name like '%t-shirt%';
select * from users where first_name like 'L%';


/*  Filtering Out or Finding Missing Information  */

-- Code Challenge
select * from phone_book where phone is null;
select last_name from phone_book where last_name is not null;






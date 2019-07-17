/*  **********  REPORTING WITH SQL **********  */

/*  ***** Ordering, Limiting, and Paging Results  ***** */

/*  Ordering Results  */

-- Code Challenge
select * from phone_book order by last_name, first_name;
select * from books order by first_published desc;
select * from books order by genre, title;

/*  Limiting the Number of Results  */

-- Code Challenge
select * from books where genre="Fantasy" order by first_published limit 5;
select * from books where genre="Science Fiction" order by first_published limit 1;

/*  Paging Through Results  */

-- Code Challenge
select * from books order by title limit 10 offset 10;
select * from phone_book order by last_name, first_name limit 20 offset 40;


/*  ***** Working with Text ***** */

/*  Adding Text Columns Together  */

-- Code Challenge
select first_name || ' ' || last_name || ' <' || email || '>' as to_field from patrons
select street || ', ' || city || ', ' || state || ' ' || zip || '. ' || country as address from addresses

/*  Finding the Length of Text  */

-- Code Challenge
select title, max(length(title)) as longest_length from books

/*  Changing the Case of Text Columns  */

-- Code Challenge
select lower(title) as lowercase_title, upper(author) as uppercase_author from books
select first_name || ' ' || upper(last_name) as full_name, library_id from patrons

/*  Creating Excerpts from Text  */

-- Code Challenge
select substr(first_name, 1, 1) as initial, last_name from customers

/*  Replacing Portions of Text  */

-- Code Challenge
select replace(email, '@', '<at>') as obfuscated_email from customers


/*  ***** Aggregate and Numeric Functions  ***** */

/*  Counting Results  */

-- Code Challenge
select count(*) as scifi_book_count from books where genre='Science Fiction'
select count(*) as jk_book_count from books where author='J.K. Rowling'

/*  Counting Groups of Rows  */

-- Code Challenge
select genre, count(*) as genre_count from books group by genre
select count(distinct genre) as total_genres from books

/*  Getting the Grand Total  */

-- Code Challenge
select sum(rating) as starman_total_ratings from reviews where movie_id = 6

/*  Calculating Averages  */

-- Code Challenge
select avg(rating) as average_rating from reviews where movie_id=6

/*  Getting Minimum and Maximum Values  */

-- Code Challenge
select min(rating) as star_min, max(rating) as star_max from reviews where movie_id=6

/*  Performing Math on Numeric Types  */

-- Code Challenge
select name, round(price/1.4, 2) as price_gbp from products

/*  Creating Up-to-the-Minute Reports */

-- Code Challenge
select count(*) as shipped_today from orders where status = 'shipped' and ordered_on = DATE("now")

/*  Calculating Dates */

-- Code Challenge
select count(*) as ordered_yesterday_and_shipped from orders where status = 'shipped' and ordered_on = date("now", "-1 day")

/*  Formatting Dates for Reporting  */

-- Code Challenge
select title, strftime("%m/%Y", date_released) as month_year_released from movies



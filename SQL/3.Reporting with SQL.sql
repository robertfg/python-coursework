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




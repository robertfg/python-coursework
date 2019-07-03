/*  **********  MODIFYING DATA WITH SQL **********  */

/*  ***** Adding Data to a Database  ***** */

/*  Adding Multiple Rows to a Table */

-- Code Challenge
insert into products values(null, "Watch", "Rolex", "10000")
insert into users values(null, "robertfg", "abcde", "Robert", "Glover");
insert into phone_book values(null, "Lana", "Glover", "555-555-5555");


/*  ***** Updating Data in a Database  ***** */

/*  Updating All Rows in a Table  */

-- Code Challenge
update products set price = 0.99;
update phone_book set first_name="Mystery", last_name="Person";

-- Quiz
UPDATE games SET platform = "Cross-Plaform" WHERE id IN (1,4);
UPDATE cars SET model = "Ford" WHERE id = 1; 




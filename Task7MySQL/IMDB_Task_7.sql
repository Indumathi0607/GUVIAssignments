drop table artist_role;
drop table artist;
drop table user_info;
drop table genre;
drop table review;
drop table media;
drop table movie;
drop view tamil_movies;
drop procedure find_movie_by_lang;


#Creating a movie table to store movie details
CREATE TABLE movie (
    movie_id INT PRIMARY KEY,
    movie_name VARCHAR(40) NOT NULL,
    movie_duration_in_minutes INT,
    movie_release_date DATE,
    movie_language TEXT
);

#Inserting values into the movie table
INSERT INTO movie(movie_id, movie_name, movie_duration_in_minutes, movie_release_date, movie_language) 
VALUES(1, "PS1", 170, "2022-09-30", "Tamil"),
(2, "Vikram", 174, "2022-06-03", "Tamil"),
(3, "Avatar2", 192, "2022-12-16", "English"),
(4, "Bahubali", 158, "2015-07-10", "Telugu"),
(5, "KGF1", 155, "2018-12-21", "Kannada");

CREATE TABLE media (
    media_id INT PRIMARY KEY,
    media_name VARCHAR(40),
    media_type VARCHAR(10) NOT NULL,
    movie_id INT,
    FOREIGN KEY(movie_id) REFERENCES movie(movie_id)    
);

#Insert values into media table
INSERT INTO media (media_id, media_name, media_type, movie_id)
VALUES(111, "Video", "mp4", 1),
(112, "Audio", "mp3", 2),
(113, "Image", ".jpg", 3),
(114, "Video", ".mov", 4),
(115, "WebMedia", ".m3u8", 5);

#Table to store genre information
CREATE TABLE genre(
genre_id VARCHAR(10) PRIMARY KEY,
movie_id INT NOT NULL,
genre_type VARCHAR(50),
FOREIGN KEY(movie_id) REFERENCES movie(movie_id)
);

#Add values to Genre table
INSERT INTO genre 
VALUES("G001", "1", "Action"),
("G002", 2, "Drama"),
("G003", 3, "Comedy"),
("G004", 4, "Thriller"),
("G005", 5, "Horror");

#Create table for review
CREATE TABLE review(
review_id VARCHAR(10) PRIMARY KEY,
movie_id INT,
review_comment VARCHAR(1000),
FOREIGN KEY(movie_id) REFERENCES movie(movie_id)
);

INSERT INTO review
VALUES("R001", 1, "Epic storytelling"),
("R002", 1, "Awesome"),
("R003", 2, "Visually stunning"),
("R004", 2, "Clever twist"),
("R005", 3, "Superb cinematography"),
("R006", 5, "Deeply impactful"),
("R007", 5, "Well written");


#Create table to store user info of review comments. Uses 2 primary keys
CREATE TABLE user_info(
user_id VARCHAR(10) ,
user_name VARCHAR(30) NOT NULL,
review_id VARCHAR(10),
movie_id INT,
FOREIGN KEY (review_id) REFERENCES review(review_id),
FOREIGN KEY (movie_id) REFERENCES movie(movie_id),
PRIMARY KEY(user_id, user_name)
);

# Adding values to user_info table, same user with multiple comments
INSERT INTO user_info
VALUES("U001", "User1", "R001", 1),
("U002", "User2", "R002", 1),
("U003", "User3", "R003", 2),
("U004", "User4", "R004", 2),
("U005", "User1", "R005", 3),
("U006", "User2", "R006", 5),
("U007", "User5", "R007", 5);

#Creating table to store artist details
CREATE TABLE artist(
artist_id VARCHAR(10),
artist_name VARCHAR(30),
artist_skill VARCHAR(100) PRIMARY KEY,
artist_age INT
);

INSERT INTO artist
VALUES("A001", "Artist1", "Acting", 30),
("A001", "Artist1", "Music director", 30),
("A002", "Artist2", "Editing", 35),
("A003", "Artist3", "Voice skill", 25),
("A003", "Artist3", "Photography", 25),
("A003", "Artist3", "Directing", 25);


#Creating table to store artist skill and their movies
CREATE TABLE artist_role(
id int PRIMARY KEY,
artist_role VARCHAR(50),
artist_skill VARCHAR(100),
movie_id INT,
FOREIGN KEY (artist_skill) REFERENCES artist(artist_skill),
FOREIGN KEY (movie_id) REFERENCES movie(movie_id)
);

INSERT INTO artist_role
VALUES(1001, "Lead actor", "Acting", 1 ),
(1002, "Film editor", "Editing", 2 ),
(1003, "Director", "Directing", 3 ),
(1004, "Music director", "Music director", 1 ),
(1005, "Lighting Technician", "Photography", 3 ),
(1006, "Dubbing Artist", "Voice skill", 1 );

#Using inner join to join 3 tables movie, media and genre
SELECT mov.movie_name, mov.movie_release_date, mov.movie_language, med.media_type, med.media_name, gen.genre_type
FROM movie mov
INNER JOIN media med ON mov.movie_id=med.movie_id
INNER JOIN genre gen ON mov.movie_id=gen.movie_id;

#Use Left JOIN to find the review comments of the movies
SELECT mov.movie_name, rev.review_comment
FROM movie mov
LEFT JOIN review rev ON mov.movie_id=rev.movie_id;

#Use RIGHT JOIN to movie without any review comment from user
SELECT ui.user_name,  mov.movie_name
FROM user_info ui
RIGHT JOIN movie mov ON ui.movie_id=mov.movie_id;

SELECT mov.movie_name, rev.review_comment
FROM movie mov
JOIN review rev ON mov.movie_id=rev.movie_id;

#Use Update query to update data in movie table
UPDATE movie 
SET movie_language = "Tamil" 
WHERE movie_id = 5;
SELECT * FROM movie;

#Add new column and update values
ALTER TABLE movie 
ADD movie_budget VARCHAR(50);

UPDATE movie
SET movie_budget = "250 Crores"
WHERE movie_id = 1;
SELECT * FROM movie;

#Delete the budget column
ALTER TABLE movie
DROP COLUMN movie_budget;
SELECT * FROM movie;

#Insert and delete rows in Movie table
INSERT INTO movie
VALUES(6, "Jailer", 150, "2023-10-09", "Kannada"),
(7, "NEEK", 145, "2024-12-20", "Tamil");
SELECT * FROM movie;

DELETE FROM movie
WHERE movie_id = 6;
SELECT * FROM movie;

# Use DISTINCT 
SELECT DISTINCT movie_language from movie;

#Use GROUP BY and HAVING
SELECT movie_language, COUNT(*) AS total
FROM movie
GROUP BY movie_language
HAVING movie_language = "Tamil";

#Use ORDER BY
SELECT * FROM movie
WHERE movie_language = "Tamil"
ORDER BY movie_duration_in_minutes DESC;

#Subquery
SELECT movie_name, movie_language, movie_duration_in_minutes
FROM movie
WHERE movie_duration_in_minutes > (
SELECT AVG(movie_duration_in_minutes) FROM movie
);

#View
CREATE VIEW tamil_movies AS
SELECT movie_id, movie_name, movie_duration_in_minutes, movie_release_date
FROM movie
WHERE movie_language = "Tamil";

Select * FROM tamil_movies;
# DROP VIEW tamil_movies;

#Stored Procedure
DELIMITER //
CREATE PROCEDURE find_movie_by_language(IN lang VARCHAR(30))
BEGIN
	SELECT * FROM movie 
    WHERE movie_language = lang;
END //

DELIMITER ;

CALL find_movie_by_language("Tamil");


#Transactions
ALTER TABLE movie
ADD movie_ticket_price INT;

START TRANSACTION ;
UPDATE movie SET movie_ticket_price = 200 WHERE movie_id = 5;
UPDATE movie SET movie_ticket_price = 100 WHERE movie_id = 1;
UPDATE movie SET movie_ticket_price = 250 WHERE movie_id = 3;
UPDATE movie SET movie_ticket_price = 150 WHERE movie_id = 2;
COMMIT ;
# ROLLBACK ; if the above transaction not working properly

SELECT * FROM movie;





























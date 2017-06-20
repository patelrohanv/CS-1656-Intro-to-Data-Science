import sqlite3 as lite
import csv
import argparse
import collections
import glob
import os
import pandas
import re
import string
import sys

con = lite.connect('cs1656.sqlite')

with con:
	cur = con.cursor() 

	########################################################################		
	### CREATE TABLES ######################################################
	########################################################################		
	# DO NOT MODIFY - START 
	cur.execute('DROP TABLE IF EXISTS Actors')
	cur.execute("CREATE TABLE Actors(aid INT, fname TEXT, lname TEXT, gender CHAR(6), PRIMARY KEY(aid))")

	cur.execute('DROP TABLE IF EXISTS Movies')
	cur.execute("CREATE TABLE Movies(mid INT, title TEXT, year INT, rank REAL, PRIMARY KEY(mid))")

	cur.execute('DROP TABLE IF EXISTS Directors')
	cur.execute("CREATE TABLE Directors(did INT, fname TEXT, lname TEXT, PRIMARY KEY(did))")

	cur.execute('DROP TABLE IF EXISTS Cast')
	cur.execute("CREATE TABLE Cast(aid INT, mid INT, role TEXT)")

	cur.execute('DROP TABLE IF EXISTS Movie_Director')
	cur.execute("CREATE TABLE Movie_Director(did INT, mid INT)")
	# DO NOT MODIFY - END

	########################################################################		
	### READ DATA FROM FILES ###############################################
	########################################################################	
	# actors.csv, movies.csv, directors.csv, cast.csv, movie_director.csv
	# UPDATE THIS
	with open('all_actors.csv', 'r') as fileActors:
		dr = csv.reader(fileActors)
		for row in dr:
			insert = list(row)
			cur.execute("INSERT INTO Actors VALUES (?, ?, ?, ?);", insert)	
	con.commit()

	with open('all_movies.csv', 'r') as fileMovies:
		dr = csv.reader(fileMovies)
		for row in dr:
			insert = list(row)
			cur.execute("INSERT INTO Movies VALUES (?, ?, ?, ?);", insert)
	con.commit()	

	with open('all_directors.csv', 'r') as fileDirectors:
		dr = csv.reader(fileDirectors)
		for row in dr:
			insert = list(row)
			cur.execute("INSERT INTO Directors VALUES (?, ?, ?);", insert)
	con.commit()

	with open('all_cast.csv', 'r') as fileCast:
		dr = csv.reader(fileCast)
		for row in dr:
			insert = list(row)
			cur.execute("INSERT INTO Cast VALUES (?, ?, ?);", insert)
	con.commit()

	with open('all_movie_dir.csv', 'r') as fileMovieDir:
		dr = csv.reader(fileMovieDir)
		for row in dr:
			insert = list(row)
			cur.execute("INSERT INTO Movie_Director VALUES (?, ?);", insert)
	con.commit()

	########################################################################		
	### INSERT DATA INTO DATABASE ##########################################
	# ACTORS
	# aid, fname, lname, sex

	# MOVIES
	# mid, title, year, rank
	
	# CAST
	# aid, mid, role

	# DIRECTORS
	# did, fname, lname
	
	# MOVIE DIRECTORS
	# did, mid
	########################################################################		
	# UPDATE THIS
	# cur.execute("INSERT INTO Actors VALUES(1001, 'Harrison', 'Ford', 'Male')") 
	# cur.execute("INSERT INTO Actors VALUES(1002, 'Daisy', 'Ridley', 'Female')") 
	# cur.execute("INSERT INTO Actors VALUES(1003, 'Mark', 'Hamil', 'Male')") 
	# cur.execute("INSERT INTO Actors VALUES(1004, 'Carrie', 'Fisher', 'Female')") 
	# cur.execute("INSERT INTO Actors VALUES(1005, 'Billy Dee', 'Williams', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1006, 'Felicty', 'Jones', 'Female')")   
	# cur.execute("INSERT INTO Actors VALUES(1007, 'Karen', 'Allen', 'Female')")   
	# cur.execute("INSERT INTO Actors VALUES(1008, 'Sean', 'Connery', 'Male')")   
	# cur.execute("INSERT INTO Actors VALUES(1009, 'Peter', 'Cushing', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1010, 'Adam', 'Driver', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1011, 'John', 'Boyega', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1012, 'Oscar', 'Isaac', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1013, 'Zachary', 'Quinto', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1014, 'Chris', 'Pine', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1015, 'Arnold', 'Schwartzenegger', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1016, 'Michael', 'Biehn', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1017, 'Lindsey', 'Lohan', 'Female')")
	# cur.execute("INSERT INTO Actors VALUES(1018, 'Rachel', 'McAdams', 'Female')")
	# cur.execute("INSERT INTO Actors VALUES(1019, 'Tina', 'Fey', 'Female')")
	# cur.execute("INSERT INTO Actors VALUES(1020, 'Amy', 'Poehler', 'Female')")
	# cur.execute("INSERT INTO Actors VALUES(1021, 'Lizzy', 'Caplan', 'Female')")
	# cur.execute("INSERT INTO Actors VALUES(1022, 'Amanada', 'Seyfried', 'Female')")
	# cur.execute("INSERT INTO Actors VALUES(1023, 'Tim', 'Meadows', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1024, 'Hrithik', 'Roshan', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1025, 'Clint', 'Eastwood', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1026, 'Kevin', 'Bacon', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1027, 'Ryan', 'Reynolds', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1028, 'Jeff', 'Bridges', 'Male')")
	# cur.execute("INSERT INTO Actors VALUES(1029, 'Julius', 'LeFlore', 'Male')")

	# cur.execute("INSERT INTO Movies VALUES(101, 'Star Wars VII: The Force Awakens', 2015, 8.2)") 
	# cur.execute("INSERT INTO Movies VALUES(102, 'Rogue One: A Star Wars Story', 2016, 8.0)")
	# cur.execute("INSERT INTO Movies VALUES(103, 'Star Wars IV: A New Hope', 1977, 8.7)") 
	# cur.execute("INSERT INTO Movies VALUES(104, 'Star Wars V: The Empire Strikes Back', 1980, 8.8)") 
	# cur.execute("INSERT INTO Movies VALUES(105, 'Star Wars VI: Return of the Jedi', 1983, 8.4)") 
	# cur.execute("INSERT INTO Movies VALUES(106, 'Raiders of the Lost Ark', 1981, 8.5)")
	# cur.execute("INSERT INTO Movies VALUES(107, 'Indiana Jones and the Last Crusade', 1989, 8.3)")
	# cur.execute("INSERT INTO Movies VALUES(108, 'Jurassic Park', 1993, 8.1)")
	# cur.execute("INSERT INTO Movies VALUES(109, 'Star Trek Beyond', 2016, 7.1)")
	# cur.execute("INSERT INTO Movies VALUES(110, 'Star Trek Into Darkness', 2013, 7.8)")
	# cur.execute("INSERT INTO Movies VALUES(111, 'The Terminator', 1984, 8.0)")
	# cur.execute("INSERT INTO Movies VALUES(112, 'Vigil in the Night', 1940, 6.8)")
	# cur.execute("INSERT INTO Movies VALUES(113, 'Zootopia', 2016, 8.1)")
	# cur.execute("INSERT INTO Movies VALUES(114, 'Deadopool', 2016, 8.0)")
	# cur.execute("INSERT INTO Movies VALUES(115, 'Arrival', 2016, 8.0)")
	# cur.execute("INSERT INTO Movies VALUES(116, 'Hacksaw Ridge', 2016, 8.1)")
	# cur.execute("INSERT INTO Movies VALUES(117, 'Mean Girls', 2004, 7.0)")
	# cur.execute("INSERT INTO Movies VALUES(118, 'Apocalypse Now', 1979, 8.5)")
	# cur.execute("INSERT INTO Movies VALUES(119, 'Blade Runner', 1982, 8.2)")
	# cur.execute("INSERT INTO Movies VALUES(120, 'Patriot Games', 1992, 6.9)")
	# cur.execute("INSERT INTO Movies VALUES(121, 'Cowboys & Aliens', 2011, 6.0)")
	# cur.execute("INSERT INTO Movies VALUES(122, 'Kaho Naa... Pyar Hai', 2000, 6.9)")
	# cur.execute("INSERT INTO Movies VALUES(123, 'Sully', 2016, 7.5)")
	# cur.execute("INSERT INTO Movies VALUES(124, 'Invictus', 2009, 7.4)")
	# cur.execute("INSERT INTO Movies VALUES(125, 'Mystic River', 2003, 8.0)")
	# cur.execute("INSERT INTO Movies VALUES(126, 'American Sniper', 2014, 7.3)")
	# cur.execute("INSERT INTO Movies VALUES(127, 'The Good, the Bad and the Ugly', 1966, 8.9)")
	# cur.execute("INSERT INTO Movies VALUES(128, 'Heartbreak Ridge', 1986, 6.8)")
	# cur.execute("INSERT INTO Movies VALUES(129, 'Wizards', 1977, 6.5)")
	# cur.execute("INSERT INTO Movies VALUES(130, 'Deadpool', 2016, 8.0)")
	# cur.execute("INSERT INTO Movies VALUES(131, 'The Big Lebowski', 1998, 8.2)")
	# cur.execute("INSERT INTO Movies VALUES(132, 'RIPD', 2013, 5.6)")
	# cur.execute("INSERT INTO Movies VALUES(133, 'In The Cut', 2003, 5.3)")

	# cur.execute("INSERT INTO Cast VALUES(1001, 101, 'Han Solo')")  
	# cur.execute("INSERT INTO Cast VALUES(1002, 101, 'Rey')") 
	# cur.execute("INSERT INTO Cast VALUES(1010, 101, 'Kylo Ren')") 
	# cur.execute("INSERT INTO Cast VALUES(1011, 101, 'Finn')") 
	# cur.execute("INSERT INTO Cast VALUES(1012, 101, 'Poe Dameron')") 
	# cur.execute("INSERT INTO Cast VALUES(1004, 101, 'Leia Organa')")
	# cur.execute("INSERT INTO Cast VALUES(1006, 102, 'Jyn Esso')")  
	# cur.execute("INSERT INTO Cast VALUES(1004, 105, 'Leia Organa')")
	# cur.execute("INSERT INTO Cast VALUES(1003, 101, 'Luke Skywalker')")  
	# cur.execute("INSERT INTO Cast VALUES(1001, 103, 'Han Solo')")  
	# cur.execute("INSERT INTO Cast VALUES(1003, 103, 'Luke Skywalker')")  
	# cur.execute("INSERT INTO Cast VALUES(1004, 103, 'Leia Organa')")
	# cur.execute("INSERT INTO Cast VALUES(1009, 103, 'Grand Moff Tarkin')")  
	# cur.execute("INSERT INTO Cast VALUES(1001, 104, 'Han Solo')")  
	# cur.execute("INSERT INTO Cast VALUES(1003, 104, 'Luke Skywalker')")  
	# cur.execute("INSERT INTO Cast VALUES(1004, 104, 'Leia Organa')")
	# cur.execute("INSERT INTO Cast VALUES(1005, 104, 'Lando Calrissian')")
	# cur.execute("INSERT INTO Cast VALUES(1001, 105, 'Han Solo')")  
	# cur.execute("INSERT INTO Cast VALUES(1003, 105, 'Luke Skywalker')")  
	# cur.execute("INSERT INTO Cast VALUES(1004, 105, 'Leia Organa')")
	# cur.execute("INSERT INTO Cast VALUES(1005, 105, 'Lando Calrissian')")
	# cur.execute("INSERT INTO Cast VALUES(1001, 106, 'Indiana Jones')")
	# cur.execute("INSERT INTO Cast VALUES(1007, 106, 'Marion Ravenwood')")  
	# cur.execute("INSERT INTO Cast VALUES(1001, 107, 'Indiana Jones')")  
	# cur.execute("INSERT INTO Cast VALUES(1013, 109, 'Commander Spock')")  
	# cur.execute("INSERT INTO Cast VALUES(1014, 109, 'Captain James T. Kirk')")
	# cur.execute("INSERT INTO Cast VALUES(1013, 110, 'Commander Spock')")  
	# cur.execute("INSERT INTO Cast VALUES(1014, 110, 'Captain James T. Kirk')")    
	# cur.execute("INSERT INTO Cast VALUES(1015, 111, 'Terminator')")  
	# cur.execute("INSERT INTO Cast VALUES(1016, 111, 'Kyle Reese')")  
	# cur.execute("INSERT INTO Cast VALUES(1009, 112, 'Joe Shand')")
	# cur.execute("INSERT INTO Cast VALUES(1017, 117, 'Cady Heron')")
	# cur.execute("INSERT INTO Cast VALUES(1018, 117, 'Regina George')")
	# cur.execute("INSERT INTO Cast VALUES(1019, 117, 'Ms. Norbury')")
	# cur.execute("INSERT INTO Cast VALUES(1020, 117, 'Mrs. George')")
	# cur.execute("INSERT INTO Cast VALUES(1021, 117, 'Janis Ian')")
	# cur.execute("INSERT INTO Cast VALUES(1022, 117, 'Karen Smith')")
	# cur.execute("INSERT INTO Cast VALUES(1023, 117, 'Mr. Duvall')")
	# cur.execute("INSERT INTO Cast VALUES(1001, 118, 'Colonel Lucas')")
	# cur.execute("INSERT INTO Cast VALUES(1001, 119, 'Rick Deck')")
	# cur.execute("INSERT INTO Cast VALUES(1001, 120, 'Jack Ryan')")
	# cur.execute("INSERT INTO Cast VALUES(1001, 121, 'Woodrow Dolarhyde')")  
	# cur.execute("INSERT INTO Cast VALUES(1024, 122, 'Rohit Mehra')")
	# cur.execute("INSERT INTO Cast VALUES(1024, 122, 'Raj Chopra')")
	# cur.execute("INSERT INTO Cast VALUES(1025, 127, 'Blondie')")
	# cur.execute("INSERT INTO Cast VALUES(1025, 128, 'Highway')")
	# cur.execute("INSERT INTO Cast VALUES(1003, 129, 'Sean')")
	# cur.execute("INSERT INTO Cast VALUES(1026, 132, 'Hayes')")
	# cur.execute("INSERT INTO Cast VALUES(1027, 132, 'Nick')")
	# cur.execute("INSERT INTO Cast VALUES(1028, 132, 'Roy')")
	# cur.execute("INSERT INTO Cast VALUES(1026, 133, 'John Graham')")
	# cur.execute("INSERT INTO Cast VALUES(1029, 133, 'Cursin Motorist')")
	# cur.execute("INSERT INTO Cast VALUES(1029, 105, 'Stormtrooper')")
	# cur.execute("INSERT INTO Cast VALUES(1027, 130, 'Wade Wilson/Deadpool')")
	# cur.execute("INSERT INTO Cast VALUES(1028, 131, 'The Dude')")

	# cur.execute("INSERT INTO Directors VALUES(5000, 'J.J.', 'Abrams')")  
	# cur.execute("INSERT INTO Directors VALUES(6000, 'Steven', 'Spielberg')")  
	# cur.execute("INSERT INTO Directors VALUES(7000, 'George', 'Lucas')")  
	# cur.execute("INSERT INTO Directors VALUES(8000, 'Irvin', 'Kershner')")  
	# cur.execute("INSERT INTO Directors VALUES(9000, 'Richard', 'Marquand')")
	# cur.execute("INSERT INTO Directors VALUES(10000, 'Francis Ford', 'Coppola')")  
	# cur.execute("INSERT INTO Directors VALUES(11000, 'Ridley', 'Scott')")  
	# cur.execute("INSERT INTO Directors VALUES(12000, 'Phillip', 'Noyce')")  
	# cur.execute("INSERT INTO Directors VALUES(13000, 'Jon', 'Favreau')")    
	# cur.execute("INSERT INTO Directors VALUES(14000, 'Rakesh', 'Roshan')")
	# cur.execute("INSERT INTO Directors VALUES(15000, 'Clint', 'Eastwood')")
	# cur.execute("INSERT INTO Directors VALUES(16000, 'Sergio', 'Leone')")

	# cur.execute("INSERT INTO Movie_Director VALUES(5000, 101)")  
	# cur.execute("INSERT INTO Movie_Director VALUES(6000, 106)")  
	# cur.execute("INSERT INTO Movie_Director VALUES(6000, 107)")  
	# cur.execute("INSERT INTO Movie_Director VALUES(7000, 103)")  
	# cur.execute("INSERT INTO Movie_Director VALUES(8000, 104)")  
	# cur.execute("INSERT INTO Movie_Director VALUES(9000, 105)") 
	# cur.execute("INSERT INTO Movie_Director VALUES(5000, 109)") 
	# cur.execute("INSERT INTO Movie_Director VALUES(5000, 110)")
	# cur.execute("INSERT INTO Movie_Director VALUES(10000, 118)")  
	# cur.execute("INSERT INTO Movie_Director VALUES(11000, 119)")  
	# cur.execute("INSERT INTO Movie_Director VALUES(12000, 120)")  
	# cur.execute("INSERT INTO Movie_Director VALUES(13000, 121)")   
	# cur.execute("INSERT INTO Movie_Director VALUES(14000, 122)")
	# cur.execute("INSERT INTO Movie_Director VALUES(15000, 123)")
	# cur.execute("INSERT INTO Movie_Director VALUES(15000, 124)")
	# cur.execute("INSERT INTO Movie_Director VALUES(15000, 125)")
	# cur.execute("INSERT INTO Movie_Director VALUES(15000, 126)")
	# cur.execute("INSERT INTO Movie_Director VALUES(16000, 127)")
	# cur.execute("INSERT INTO Movie_Director VALUES(15000, 128)")
	con.commit()	

	########################################################################		
	### QUERY SECTION ######################################################
	########################################################################		
	queries = {}

	# DO NOT MODIFY - START 	
	# DEBUG: all_movies ########################
	queries['all_movies'] = '''
SELECT * FROM Movies
'''	
	# DEBUG: all_actors ########################
	queries['all_actors'] = '''
SELECT * FROM Actors
'''	
	# DEBUG: all_cast ########################
	queries['all_cast'] = '''
SELECT * FROM Cast
'''	
	# DEBUG: all_directors ########################
	queries['all_directors'] = '''
SELECT * FROM Directors
'''	
	# DEBUG: all_movie_dir ########################
	queries['all_movie_dir'] = '''
SELECT * FROM Movie_Director
'''	
	# DO NOT MODIFY - END

	########################################################################		
	### INSERT YOUR QUERIES HERE ###########################################
	########################################################################		

	# Q1 
	# List all the actors (first and last name) who acted in at least one film in the 1st half of the 20th century (1901-1950) 
	# and in at least one film in the 2nd half of the 20th century (1951 - 2000).	
	queries['query01'] = '''
		SELECT fname, lname
		FROM Actors NATURAL JOIN Cast
			NATURAL JOIN Movies
		WHERE year >= 1901 AND year <= 1950

		INTERSECT

		SELECT fname, lname
		FROM Actors NATURAL JOIN Cast
			NATURAL JOIN Movies
		WHERE year >= 1951 AND year <= 2000;
	'''
	# Q2 
	# List all the movies (title, year) that were released in the same year as the movie entitled "Rogue One: A Star Wars Story"
	# , but had a better rank (Note: the higher the value in the rank attribute, the better the rank of the movie).	
	queries['query02'] = '''
		SELECT title, year
		FROM Movies
		WHERE year = (SELECT year FROM Movies WHERE title = "Rogue One: A Star Wars Story") AND rank > (SELECT rank FROM Movies WHERE title = "Rogue One: A Star Wars Story");
	'''

	# Q3 	
	# List all the actors (first and last name) who played in the movie entitled "Star Wars VII: The Force Awakens".
	#(SELECT mid FROM Movies WHERE title = "Star Wars VII: The Force Awakens")
	queries['query03'] = '''
		SELECT fname, lname
		FROM Actors NATURAL JOIN Cast
		WHERE mid = (SELECT mid FROM Movies WHERE title = "Star Wars VII: The Force Awakens");
	'''

	# Q4 		
	# Find the actor(s) (first and last name) who only acted in films released before 1985.
	queries['query04'] = '''
		SELECT DISTINCT fname, lname
		FROM Actors NATURAL JOIN Cast
			NATURAL JOIN Movies
		WHERE year < 1985
		
		EXCEPT 

		SELECT DISTINCT fname, lname
		FROM Actors NATURAL JOIN Cast
			NATURAL JOIN Movies
		WHERE year >= 1985;
	'''
	# Q5 		
	# List all the directors in descending order of the number of films they directed (first name, last name, number of films directed)
	queries['query05'] = '''
		SELECT fname, lname, COUNT(did)
		FROM Directors NATURAL JOIN Movie_Director
		GROUP BY did
		ORDER BY COUNT(did) DESC
	'''

	# Q6 		
	# Find the movie(s) with the largest cast (title, number of cast members). Note: show all movies in case of a tie.
	queries['query06'] = '''
		SELECT title, COUNT(DISTINCT aid)
		FROM Movies NATURAL JOIN Cast
		GROUP BY mid
		HAVING COUNT(DISTINCT aid) = (SELECT COUNT(DISTINCT aid) FROM Cast GROUP BY mid ORDER BY COUNT(DISTINCT aid) DESC LIMIT 1);
	'''
	# Q7 		
	# Find the movie(s) whose cast has more actresses than actors (i.e., gender=female vs gender=male). 
	# Show the title, the number of actresses, and the number of actors in the results.
	cur.execute('DROP VIEW IF EXISTS Female;')
	cur.execute('''
		CREATE VIEW Female(title, girl) AS
		SELECT title, count(*) AS girl
		FROM Movies AS m
			INNER JOIN Cast AS c
			ON m.mid = c.mid
			INNER JOIN Actors AS a
			ON c.aid = a.aid
		WHERE gender = "Female"
		GROUP BY m.title;
		''')
	cur.execute('DROP VIEW IF EXISTS Male;')
	cur.execute('''
		CREATE VIEW Male(title, boy) AS
		SELECT title, count(*) AS boy
		FROM Movies AS m
			INNER JOIN Cast AS c
			ON m.mid = c.mid
			INNER JOIN Actors AS a
			ON c.aid = a.aid
		WHERE gender = "Male"
		GROUP BY m.title;
		''')

	# queries['query07-girl'] = '''SELECT title, girl FROM Female;'''
	# queries['query07-boy'] = '''SELECT title, boy FROM Male;'''

	queries['query07'] = '''
		SELECT f.title, girl, boy
		FROM Female AS f 
			LEFT JOIN Male AS m USING(title)
		WHERE IFNULL(girl, 0) > IFNULL(boy, 0)
    '''
	# Q8 		
	# Find all the actors who have worked with at least 7 different directors (i.e., acted in at least 7 different movies with distinct directors). 
	# Show the actor's first, last name, and the number of directors he/she has worked with.
	queries['query08']='''
			SELECT  fname, lname, COUNT(DISTINCT did)
			FROM Actors NATURAL JOIN Cast
				NATURAL JOIN Movies
				NATURAL JOIN Movie_Director
			GROUP BY fname
			HAVING COUNT(DISTINCT did) >= 7;
		'''
	# Q9 		
	# For every actor, count the movies that he/she appeared in his/her debut year (i.e., year of their first movie). 
	# Show the actor's first and last name, plus the count. Sort by decreasing order of the count.
	queries['query09']='''
			SELECT a.fname, a.lname, COUNT(DISTINCT mid)
			FROM Actors AS a NATURAL JOIN Cast AS c
				NATURAL JOIN Movies AS m
				WHERE m.year = (SELECT MIN(subm.year) 
					FROM Movies AS subm
						NATURAL JOIN Cast AS subc
					WHERE a.aid = subc.aid)
			GROUP BY a.aid
			ORDER BY COUNT(DISTINCT mid) DESC;
		'''
	# Q10 		
	# Find instances of nepotism between actors and directors, i.e., an actor in a movie and the director have the same last name. 
	# Show the last name and the title of the movie, sorted alphabetically by last name.
	queries['query10'] = '''
		SELECT lname, title
			FROM Actors NATURAL JOIN CAST
				NATURAL JOIN Movies
		
		INTERSECT

		SELECT lname, title
			FROM Directors NATURAL JOIN Movie_Director
				NATURAL JOIN Movies
		
		ORDER BY lname;
	'''
	# Q11 		
	# The Bacon number of an actor is the length of the shortest path between the actor and Kevin Bacon in the "co-acting" graph. 
	# That is, Kevin Bacon has Bacon number 0; all actors who acted in the same movie as him have Bacon number 1; 
	# all actors who acted in the same film as some actor with Bacon number 1 have Bacon number 2, etc. 
	# List all actors whose Bacon number is 2 (first name, last name).
	queries['query11']='''
	SELECT a.fname, a.lname FROM Actors AS a WHERE a.aid IN (
		SELECT c1.aid FROM Cast AS c1 WHERE c1.mid IN (
			SELECT DISTINCT c2.mid FROM Cast AS c2 WHERE c2.aid IN (
				SELECT a3.aid FROM Actors AS a3 WHERE a3.aid IN (
					SELECT c4.aid FROM Cast AS c4 WHERE c4.mid IN (
						SELECT c5.mid FROM Cast AS c5 WHERE c5.aid IN (
							SELECT a6.aid FROM Actors AS a6 WHERE a6.fname='Kevin' AND a6.lname='Bacon'
						)
					)
					AND c4.aid != (
						SELECT a7.aid FROM Actors AS a7 WHERE a7.fname='Kevin' AND a7.lname='Bacon'
					)
				)
			GROUP BY aid
			)
		)
		AND c1.aid NOT IN (
			SELECT a7.aid FROM Actors AS a7 WHERE a7.aid IN (
				SELECT c8.aid FROM Cast AS c8 WHERE c8.mid IN (
					SELECT c9.mid FROM Cast AS c9 WHERE c9.aid IN (
						SELECT a10.aid FROM Actors AS a10 WHERE a10.fname='Kevin' AND a10.lname='Bacon'
					)
				)
			)
			GROUP BY aid
		)
	)
	'''
	# Q12 		
	# Assume that the popularity of an actor is reflected by the average rank of all the movies he/she has acted in. 
	# Find the top 20 most popular actors (in descreasing order of popularity) 
	# -- list the actor's first/last name, the total number of movies he/she has acted, and his/her popularity score. 
	# For simplicity, feel free to ignore ties at the number 20 spot
	queries['query12'] = '''
		SELECT fname, lname, COUNT(aid), AVG(rank)
		FROM Actors NATURAL JOIN Cast
			NATURAL JOIN Movies
			GROUP BY aid
			ORDER BY AVG (rank) DESC
			LIMIT 20;
	'''

	########################################################################		
	### SAVE RESULTS TO FILES ##############################################
	########################################################################		
	# DO NOT MODIFY - START 	
	for (qkey, qstring) in sorted(queries.items()):
		try:
			cur.execute(qstring)
			all_rows = cur.fetchall()
			
			print ("=========== ",qkey," QUERY ======================")
			print (qstring)
			print ("=========== ",qkey," RESULTS ====================")
			for row in all_rows:
				print (row)
			print (" ")

			with open(qkey+'.csv', 'w') as f:
				writer = csv.writer(f)
				writer.writerows(all_rows)
				f.close()
		
		except lite.Error as e:
			print ("An error occurred:", e.args[0])
	# DO NOT MODIFY - END
	

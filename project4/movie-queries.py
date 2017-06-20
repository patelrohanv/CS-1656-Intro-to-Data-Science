from neo4j.v1 import GraphDatabase, basic_auth

#driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "cs1656"), encrypted=False)
driver = GraphDatabase.driver("bolt://localhost", encrypted=False)
session = driver.session()

out = open('output.txt', 'w')
# [Q1] List all the actors who played in the movie entitled "Star Wars VII: The Force Awakens".
# OUTPUT: actor_name

out.write("### Q1 ###")
out.write("\n")
result = session.run("""
    MATCH (m:Movie {title: 'Star Wars VII: The Force Awakens'})<-[:ACTS_IN]-(a:Actor)
    RETURN a.name
    ;""")
for record in result:
    #print (record)
    out.write(str(record['a.name']))
    out.write("\n")

#out.write("\n")
out.write("### Q2 ###")
out.write("\n")
# [Q2] List all the directors in descending order of the number of films they directed.
# OUTPUT: director_name, number_of_films_directed
result = session.run("""
    MATCH (d:Director)-[:DIRECTED]->(m:Movie)
    WITH d, COUNT(DISTINCT m) AS movies
    RETURN d.name, movies
    ORDER BY movies DESC
    ;""")
for record in result:
    #print (record)
    out.write(str(record['d.name']) + ", " + str(record['movies']))
    out.write("\n")

# out.write("\n")
out.write("### Q3 ###")
out.write("\n")
# [Q3] Find the movie with the largest cast.
# OUTPUT: movie_title, number_of_cast_members
result = session.run("""
    MATCH (m:Movie)<-[:ACTS_IN]-(a:Actor)
    WITH m, COUNT(DISTINCT a) AS cast
    RETURN m.title, cast
    ORDER BY cast DESC
    LIMIT 1
    ;""")
for record in result:
    #print (record)
    out.write(str(record['m.title']) + ", " + str(record['cast']))
    out.write("\n")

# out.write("\n")
out.write("### Q4 ###")
out.write("\n")
# [Q4] Find all the actors who have worked with at least 3 different directors (i.e., acted in at least 3 different movies with distinct directors).
# OUTPUT: actor_name, number_of_directors_he/she_has_worked_with
result = session.run("""
    MATCH (a:Actor)-[:ACTS_IN]->(m:Movie)<-[:DIRECTED]-(d:Director)
    WITH a, COUNT(DISTINCT d) AS dCount
    WHERE dCount > 2
    RETURN a.name, dCount
    ORDER BY dCount DESC
    ;""")
for record in result:
    #print (record)
    out.write(str(record['a.name']) + ", " + str(record['dCount']))
    out.write("\n")

# out.write("\n")
out.write("### Q5 ###")
out.write("\n")
# [Q5] The Bacon number of an actor is the length of the shortest path between the actor and Kevin Bacon in the "co-acting" graph. 
# That is, Kevin Bacon has Bacon number 0; 
# all actors who acted in the same movie as him have Bacon number 1; 
# all actors who acted in the same film as some actor with Bacon number 1 have Bacon number 2, etc. 
# List all actors whose Bacon number is 2 (first name, last name). 
# You can familiarize yourself with the concept, by visiting The Oracle of Bacon.
# OUTPUT: actor_name

# for record in result:
#     #print (record)
#     out.write(str(record['a.name']))
#     out.write("\n")

result = session.run("""
    MATCH (kev:Actor {name:'Kevin Bacon'})-[:ACTS_IN]->(m)<-[:ACTS_IN]-(coActors),
    (coActors)-[:ACTS_IN]->(m2)<-[:ACTS_IN]-(cocoActors)
    WHERE NOT (kev)-[:ACTS_IN]->(m2) AND cocoActors.name <> kev.name AND NOT (cocoActors)-[:ACTS_IN]->(m)
    RETURN DISTINCT cocoActors.name
    ORDER BY cocoActors.name ASC
    ;""")
for record in result:
    #print (record)
    out.write(str(record['cocoActors.name']))
    out.write("\n")

# out.write("\n")
out.write("### Q6 ###")
out.write("\n")
# [Q6] Extend the previous query to show all actors with a Bacon number of 1 to 4.
# OUTPUT: actor_name
result = session.run("""
    MATCH shortestPath((kev:Actor{name: "Kevin Bacon"})-[:ACTS_IN*1..8]-(a:Actor))
    WHERE a <> kev
    RETURN DISTINCT a.name
    ORDER BY a.name ASC
    ;""")
for record in result:
    #print (record)
    out.write(str(record['a.name']))
    out.write("\n")

# out.write("\n")
out.write("### Q7 ###")
out.write("\n")
# [Q7] Find those actors who are not connected to Kevin Bacon in the co-acting graph (i.e., their Bacon number would be infinity).
# OUTPUT: actor_name
result = session.run("""
    MATCH p = shortestPath((bacon: Actor{name: 'Kevin Bacon'})-[:ACTS_IN*0..24]-(a: Actor))
    WITH p, a
    WHERE length(p) > 12 AND bacon <> a
    RETURN a.name
    ;""")
for record in result:
    #print (record)
    out.write(str(record['a.name']))
    out.write("\n")

# out.write("\n")
out.write("### Q8 ###")
out.write("\n")
# [Q8] Should the Kevin Bacon game be renamed? 
# Is there a different actor with a higher number of first-level connections in the co-acting graph?
# Compute the number of co-actors for each actor and return the top 50 highest (sorted in descending order).
# OUTPUT: actor_name, number_of_co_actors
result = session.run("""
    MATCH ((a:Actor)-[:ACTS_IN*2]-(b:Actor))
    RETURN a.name, COUNT(DISTINCT b) AS bacon
    ORDER BY bacon DESC
    LIMIT 50
    ;""")
for record in result:
    #print (record)
    out.write(str(record['a.name']) + ", " + str(record['bacon']))
    out.write("\n")
    
out.close()
session.close()
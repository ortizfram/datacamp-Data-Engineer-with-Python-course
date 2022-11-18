"""
Join all the tables together
In this last exercise, your task is to find the university city of the professor with the most affiliations in the sector "Media & communication".

For this,

you need to join all the tables,
group by some column,
and then use selection criteria to get only the rows in the correct sector.
Let's do this in three steps!

Instructions 3/3

- Join all tables in the database (starting with affiliations, professors, organizations, and universities) and look at the result.
- Now group the result by organization sector, professor, and university city.
  Count the resulting number of rows.
- Only retain rows with "Media & communication" as organization sector, and sort the table by count, in descending order.

"""
#1
#-- Join all tables
SELECT *
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id;

#2
#-- Group the table by organization sector, professor ID and university city
SELECT COUNT(*), organizations.organization_sector, 
professors.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
GROUP BY organizations.organization_sector, 
professors.id, universities.university_city;

#3
#-- Filter the table and sort it
SELECT COUNT(*), organizations.organization_sector, 
professors.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
WHERE organizations.organization_sector = 'Media & communication'
GROUP BY organizations.organization_sector, 
professors.id, universities.university_city
ORDER BY count DESC;

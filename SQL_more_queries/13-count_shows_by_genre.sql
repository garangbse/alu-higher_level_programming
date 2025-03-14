-- Lists all genres and displays number of shows linked to each
SELECT g.name AS genre,
    COUNT(s.show_id) AS number_of_shows
FROM tv_genres g
INNER JOIN tv_show_genres s
ON g.id = s.genre_id
GROUP BY g.name
HAVING COUNT(s.show_id) > 0
ORDER BY COUNT(s.show_id) DESC;

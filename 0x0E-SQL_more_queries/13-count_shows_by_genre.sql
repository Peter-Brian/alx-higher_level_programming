-- The database name will be passed as an argument of the mysql command
-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;

-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Results must be sorted in ascending order by the show title and genre name
SELECT sh.title, gr.name FROM tv_shows AS sh LEFT JOIN tv_show_genres AS shgr
ON sh.id=shgr.show_id LEFT JOIN tv_genres AS gr
ON shgr.genre_id=gr.id ORDER BY sh.title, gr.name ASC;

-- lists all shows contained in the database
-- lists all shows contained in the database
   SELECT tv_shows.title, tv_show_genres.genre_id
     FROM tv_shows
LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
 ORDER BY title, genre_id;

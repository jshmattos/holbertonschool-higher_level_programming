-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- create database if it does not exists
-- list all shows that has a genre linked
  CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
  SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    JOIN tv_show_genres
      ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id;

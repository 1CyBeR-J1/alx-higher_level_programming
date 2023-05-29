-- lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows INNER JOIN tv_show_rating
ON tv_shows.id = tv_show_rating.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;

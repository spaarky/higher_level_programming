-- lists the `score` and number of occurances with each score with 'number'

SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC

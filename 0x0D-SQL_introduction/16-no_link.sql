-- The result should display:
-- the score
-- the number of records for this score with the label number
-- The list should be sorted by the number of records (descending)
-- The database name will be passed as an argument to the mysql command
SELECT score, name FROM `second_table` WHERE name IS NOT NULL  ORDER BY score DESC;

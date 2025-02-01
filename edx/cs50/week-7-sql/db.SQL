-- Queries

CREATE TABLE friends (
    id INT AUTOINCREMENT PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO friends (name) VALUES ('Silvio');
INSERT INTO friends (name) VALUES ('Israel');
INSERT INTO friends (name) VALUES ('Jefferson');
INSERT INTO friends (name) VALUES ('Nicolas');

COUNT()
MIN()
MAX()
AVG()
SUM()

JOIN author ON todos.author_id = users.id
JOIN author ON notes.author_id = users.id
JOIN author ON posts.author_id = users.id

SELECT AVG(energy)
FROM songs
WHERE artist_id IN (SELECT id FROM artists WHERE name = 'Drake');

SELECT name FROM songs WHERE name LIKE '%feat.%';


GROUP BY
ORDER BY ASC DESC


WHERE
LIKE
IS
NOT

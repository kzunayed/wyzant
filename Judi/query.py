import sqlite3

conn = sqlite3.connect('C:/Users/Anabil/Downloads/Formula1.sqlite')

cursor = conn.cursor()

query = """
WITH RacePositionChanges AS (
SELECT
races.raceId,
races.name,
races.year,
SUM(ABS(results.grid - results.position)) AS total_position_change
FROM
results
JOIN races ON results.raceId = races.raceId
WHERE
results.position BETWEEN 1 AND 10
GROUP BY
races.raceId,
races.name,
races.year
HAVING
COUNT(results.position) = 10
)
SELECT
rpc.raceId,
rpc.name,
rpc.year,
rs.position,
rs.grid,
d.forename,
d.surname,
c.name AS constructor_name
FROM
RacePositionChanges rpc
JOIN results rs ON rs.raceId = rpc.raceId
JOIN drivers d ON rs.driverId = d.driverId
JOIN constructors c ON rs.constructorId = c.constructorId
WHERE
total_position_change = (
SELECT MAX(total_position_change)
FROM RacePositionChanges
)
and rs.position <= 10
ORDER BY
total_position_change DESC;
"""

cursor.execute(query)

results = cursor.fetchall()
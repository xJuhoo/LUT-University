SELECT * FROM Player
INNER JOIN Ranking
ON Player.playerid = Ranking.FK_playerid
WHERE Ranking.rank <= 10;
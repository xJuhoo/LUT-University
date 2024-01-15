INSERT INTO Matches (FK_playerOne, FK_playerTwo, resultSets, matchdate, winnerID)
VALUES (
    (SELECT FK_playerid FROM Ranking WHERE rank = 1),
    (SELECT FK_playerid FROM Ranking WHERE rank = (SELECT MAX(rank) FROM Ranking)),
    '0-0',
    'unplayed',
    0
);
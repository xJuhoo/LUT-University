CREATE VIEW View_1 AS
SELECT band, band_member, member_instrument
FROM musicrecords
WHERE band IS NOT NULL
AND band_member IS NOT NULL
AND member_instrument IS NOT NULL
ORDER BY band, band_member;

CREATE VIEW View_2 AS
SELECT band, album, releaseYear
FROM musicrecords
WHERE band IS NOT NULL
AND album IS NOT NULL
AND releaseYear IS NOT NULL
GROUP BY album
ORDER BY band, releaseYear;

CREATE VIEW View_3 AS
SELECT band, album, track, track_duration
FROM musicrecords
WHERE band IS NOT NULL
AND album IS NOT NULL
AND track IS NOT NULL
AND track_duration IS NOT NULL
ORDER BY band, album, track_duration;
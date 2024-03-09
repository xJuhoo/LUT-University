SELECT
    n AS name,
    d AS purchase_date
FROM
    purchases
WHERE
    EXTRACT(DOW FROM d) = 5
    AND EXTRACT(DAY FROM d) >= 22
ORDER BY
    d;

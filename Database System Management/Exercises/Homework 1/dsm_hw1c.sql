SELECT
    n AS name,
    d AS purchase_date
FROM
    purchases
WHERE
    EXTRACT(MONTH FROM d) IN (2, 3) -- Feb and March
    AND EXTRACT(YEAR FROM d) % 4 = 0 -- Leap year check
ORDER BY
    name,
    purchase_date;

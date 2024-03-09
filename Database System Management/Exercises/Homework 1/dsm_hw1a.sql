SELECT 
	p1.n AS name,
    p1.i AS item_1,
    p1.d AS purchase_date_1,
    p2.i AS item_2,
    p2.d AS purchase_date_2
FROM
	purchases p1
JOIN
	purchases p2 ON p1.n = p2.n -- Same customer
    AND p1.d + interval '1 month' = p2.d -- One month difference
ORDER BY
	name;

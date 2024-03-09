CREATE FUNCTION hw5_get_shipping_info(varchar, timestamp, money)
RETURNS TABLE (
    orderid int,
    shipname varchar,
    shipaddress varchar,
    shipcity varchar,
    shipcountry varchar
)
AS $$
BEGIN
    RETURN QUERY
    SELECT o.orderid, o.shipname, o.shipaddress, o.shipcity, o.shipcountry
    FROM Orders o
    WHERE o.shipname = $1
    AND o.orderdate <= $2
    AND o.freight::numeric::int BETWEEN ($3::numeric::int - 10) AND ($3::numeric::int + 10);
END;
$$ LANGUAGE plpgsql;

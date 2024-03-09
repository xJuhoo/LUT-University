CREATE FUNCTION hw5_get_shipping_info(target varchar)
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
    WHERE o.shipname = target;
END;
$$ LANGUAGE plpgsql;

CREATE ROLE trainee WITH LOGIN VALID UNTIL '2023-05-30';
GRANT ALL(orderdate, shippeddate) ON Orders TO trainee;

-- Creating the roles
CREATE ROLE db_user;
CREATE ROLE db_manager;
CREATE ROLE db_owner;

GRANT ALL ON Orders TO db_owner;
GRANT SELECT ON Orders TO db_user;
GRANT INSERT ON Orders TO db_manager;

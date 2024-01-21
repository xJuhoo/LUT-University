CREATE TRIGGER hashtag_not_allowed
BEFORE INSERT ON Hashtag
BEGIN 
    SELECT CASE
        WHEN NEW.Content LIKE "%mayonnaise%" THEN
            RAISE (ABORT, "Mayonnaise detected!")
   END;
END;
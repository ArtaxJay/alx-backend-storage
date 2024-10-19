-- script will create trigger that resets the attr
-- (valid_email) when the email has been changed.

DELIMITER $$ ;
CREATE TRIGGER validate BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;$$
delimiter;
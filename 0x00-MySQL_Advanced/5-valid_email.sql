-- Creates a trigger that resets the attribute valid_email only when email has
-- been changed

-- Change delimiter
DELIMITER $$

-- Create trigger
CREATE TRIGGER reset_email BEFORE UPDATE on users
FOR EACH ROW
BEGIN
	IF !(NEW.email <=> OLD.email) THEN
		SET NEW.valid_email = 0;
	END IF;
END$$

-- Reset delimiter
DELIMITER ;

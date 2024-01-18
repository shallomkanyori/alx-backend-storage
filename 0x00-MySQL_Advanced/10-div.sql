-- Creates a function SafeDiv that safely divides two integers and returns the
-- result

-- Change delimiter
DELIMITER $$

-- Create function
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END$$

-- Reset delimiter
DELIMITER ;

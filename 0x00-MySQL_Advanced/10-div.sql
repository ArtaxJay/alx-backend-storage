-- This will create a func: SafeDiv that
-- divides & returns d first by d second number (SUCCESS)
-- or returns 0 (FAILED) if the second number is equal to 0.

DELIMITER $$;
CREATE FUNCTION SafeDiv(
	a INT,
	b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	DECLARE result FLOAT;
	IF b = 0 THEN
		RETURN 0;
        END IF;
        SET result = (a * 1.0) / b;
        RETURN result;
END;$$
DELIMITER;
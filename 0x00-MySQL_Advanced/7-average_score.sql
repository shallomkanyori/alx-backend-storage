-- Creates a stored procedure ComputeAverageScoreForUser that computes and
-- stores the average score for a student

-- Change delimiter
DELIMITER $$

-- Create stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	SELECT AVG(score) INTO avg_score
	  FROM corrections
	 WHERE corrections.user_id = user_id;

	UPDATE users
	   SET average_score = avg_score
	 WHERE id = user_id;
END$$

-- Reset delimiter
DELIMITER ;

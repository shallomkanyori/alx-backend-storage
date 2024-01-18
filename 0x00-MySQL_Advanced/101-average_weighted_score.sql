-- Creates a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and stores the average weighted score for all students.

-- Change delimiter
DELIMITER $$

-- Create procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users
	   SET average_score = (
		SELECT SUM(c.score * p.weight) / SUM(p.weight)
		  FROM corrections AS c
		       LEFT JOIN projects AS p
		       ON c.project_id = p.id
		       WHERE c.user_id = users.id
	);
END$$

-- Reset delimiter
DELIMITER ;

-- Creates a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and stores the average weighted score for a student.

-- Change delimiter
DELIMITER $$

-- Create procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE weight_avg FLOAT;

	SELECT SUM(score * weight)/SUM(weight) INTO weight_avg FROM (
		SELECT score, weight
		  FROM corrections AS c
		       LEFT JOIN projects AS p
		       ON c.project_id = p.id
		       WHERE c.user_id = user_id
	) AS scores_with_weights;

	UPDATE users
	   SET average_score = weight_avg
	 WHERE id = user_id;
END$$

-- Reset delimiter
DELIMITER ;

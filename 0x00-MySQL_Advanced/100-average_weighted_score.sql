-- This script will create a stored procedure named: ComputeAverageWeightedScoreForUser
-- :which will take in one param: user_id.

-- It will then compute the avg. wegtd score (AWS):
-- :for a user by adding/summing the product of scores and weights of the user from: `corrections` table, 
-- :add the total wgt, and then divide total wgtd score by total wgt,
-- :and update the `average_score` field of d user in d `users` table.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE total_weighted_score INT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;

    SELECT SUM(corrections.score * projects.weight)
        INTO total_weighted_score
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    SELECT SUM(projects.weight)
        INTO total_weight
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    IF total_weight = 0 THEN
        UPDATE users
            SET users.average_score = 0
            WHERE users.id = user_id;
    ELSE
        UPDATE users
            SET users.average_score = total_weighted_score / total_weight
            WHERE users.id = user_id;
    END IF;
END $$
DELIMITER;
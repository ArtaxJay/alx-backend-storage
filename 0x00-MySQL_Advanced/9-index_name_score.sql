-- This will create an index: idx_name_first_score
-- on the table names & d first letter of name & d score.
CREATE INDEX idx_name_first_score on names(name(1), score)
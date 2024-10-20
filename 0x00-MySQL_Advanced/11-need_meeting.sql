-- This script will create a view: need_meeting
-- this lists all students that have a score less than 80
-- and no last_meeting || greater than 1 month.

CREATE VIEW need_meeting AS SELECT name from students WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
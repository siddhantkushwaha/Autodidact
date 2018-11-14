DELIMITER $$
CREATE PROCEDURE user_tags(IN user_id INT(11))
BEGIN
	SELECT * FROM autodidact_forum.app_tag WHERE created_by_id=user_id;
END$$
DELIMITER ;
DELIMITER $$
CREATE PROCEDURE addTag(IN name VARCHAR(20),IN created_by_id INT(11))
BEGIN
	INSERT INTO app_tag (name,use_count,creation_time,created_by_id) VALUES (name,0,now(),created_by_id);
	SELECT 'adding tag' as '';
END$$
DELIMITER ;
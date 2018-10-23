DELIMITER $$
CREATE PROCEDURE add_tag(IN name VARCHAR(30),IN created_by_id INT(11))
BEGIN
	INSERT INTO app_tag (name,use_count,creation_time,created_by_id) VALUES (name,0,now(),created_by_id);
END$$
DELIMITER ;

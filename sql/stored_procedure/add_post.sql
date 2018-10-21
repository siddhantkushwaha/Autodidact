DELIMITER $$
CREATE PROCEDURE addPost(IN name VARCHAR(20),IN creation_time DATETIME(6),IN created_by INT(11))
BEGIN
	SET USE_COUNT = 0;
	INSERT INTO app_tag VALUES (name,USE_COUNT,creation_time,creation_time);
	print 'adding post';
END$$
DELIMITER ;
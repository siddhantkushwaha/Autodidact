DELIMITER $$
CREATE PROCEDURE addPost(IN title VARCHAR(100),IN creation_time DATETIME(6),IN description VARCHAR(500),IN created_by INT(11))
BEGIN
	INSERT INTO app_thread VALUES (title, 0, 0, 0, now(), description, created_by);
	print 'adding post';
END$$
DELIMITER ;
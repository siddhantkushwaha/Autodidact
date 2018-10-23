DELIMITER $$
CREATE PROCEDURE add_post(IN title VARCHAR(100),IN creation_time DATETIME(6),IN description VARCHAR(500),IN created_by INT(11))
BEGIN
	INSERT INTO app_post VALUES (title, 0, 0, 0, now(), description, created_by);
END$$
DELIMITER ;

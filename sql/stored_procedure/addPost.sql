DELIMITER $$
CREATE PROCEDURE addPost(IN title VARCHAR(100),IN description VARCHAR(500),IN created_by INT(11))
BEGIN
	INSERT INTO app_thread (title,view_count,upvote_count,downvote_count,creation_time,description,created_by_id) VALUES (title, 0, 0, 0, now(), description, created_by);
END$$
DELIMITER ;
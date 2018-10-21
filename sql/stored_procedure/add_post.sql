DELIMITER $$
CREATE PROCEDURE addPost(IN title VARCHAR(100),IN creation_time DATETIME(6),IN description VARCHAR(500),IN created_by INT(11))
BEGIN
	SET view_count = 0;
	SET upvote_count = 0;
	SET downvote_count = 0;

	INSERT INTO app_thread VALUES (title, view_count, upvote_count, downvote_count, creation_time, description, created_by);
	print 'adding post';
END$$
DELIMITER ;
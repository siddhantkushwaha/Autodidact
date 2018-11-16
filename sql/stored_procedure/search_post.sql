CREATE DEFINER=`autodidact_forum`@`localhost` PROCEDURE `search_post`(IN query varchar(100))
BEGIN
SELECT * from app_tag WHERE title LIKE  CONCAT('%' ,query,'%')  ORDER BY id;
END
CREATE DEFINER=`autodidact_forum`@`localhost` PROCEDURE `search_tag`(IN tag_name VARCHAR(50))
BEGIN
    SELECT * from app_tag WHERE name LIKE  CONCAT('%' ,tag_name,'%')  ORDER BY use_count DESC, id;
END
-- SELECT * from auth_user WHERE email LIKE '%uday%';
-- SELECT * from app_forumuser ORDER BY reputation DESC;
-- SELECT * from auth_user ORDER BY date_joined;
DELIMITER $$
CREATE PROCEDURE search_email(IN email VARCHAR(254))
BEGIN
	SELECT * from auth_user WHERE email LIKE  CONCAT('%' ,email,'%');
END$$
DELIMITER ;
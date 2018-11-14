-- SELECT * from auth_user WHERE email LIKE '%uday%';
-- SELECT * from app_forumuser ORDER BY reputation DESC;
-- SELECT * from auth_user ORDER BY date_joined;
DELIMITER $$
CREATE PROCEDURE search_email(IN email_id VARCHAR(254))
BEGIN
	SELECT * FROM app_forumuser WHERE django_user_id IN 
    ( SELECT id from auth_user WHERE email LIKE  CONCAT('%' ,email_id,'%') );
END$$
DELIMITER ;
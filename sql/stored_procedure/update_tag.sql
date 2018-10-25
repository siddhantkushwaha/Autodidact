DELIMITER $$
CREATE PROCEDURE update_tag(IN new_tag VARCHAR(50),IN old_tag VARCHAR(50))
BEGIN
    UPDATE app_tag SET name = new_tag WHERE name = old_tag;
END$$
DELIMITER ;
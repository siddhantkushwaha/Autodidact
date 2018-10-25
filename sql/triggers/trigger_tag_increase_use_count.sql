use autodidact_forum;
drop trigger if exists tag_increase_use_count;
delimiter //
CREATE TRIGGER tag_increase_use_count BEFORE INSERT ON app_post_tags
       FOR EACH ROW
       BEGIN
           UPDATE app_tag SET use_count = use_count + 1 WHERE id = NEW.tag_id;
       END;//
mysql> delimiter ;
use autodidact_forum;
drop trigger if exists tag_decrease_use_count;
delimiter //
CREATE TRIGGER tag_decrease_use_count BEFORE DELETE ON app_post_tags
       FOR EACH ROW
       BEGIN
           UPDATE app_tag SET use_count = use_count - 1 WHERE id = OLD.tag_id;
       END;//
mysql> delimiter ;
SELECT * FROM app_tag
INNER JOIN app_post_tags ON
app_post_tags.tag_id = app_tag.id
WHERE app_post_tags.post_id = 104;
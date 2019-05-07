test1;
iiiiiiiii
test2;
cew;
cece;
test3;

update user_info u set u.id = (select user_id from (select distinct user_id, username from workinghour) a
where u.real_name = a.username) where u.real_name in (select username from workinghour);

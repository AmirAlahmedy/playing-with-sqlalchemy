create table projects (
project_id int(11) not null auto_increment,
title varchar(30),
description varchar(255),
primary key(project_id)
);


create table tasks (
task_id int(11) not null auto_increment,
project_id int(11) not null,
description varchar(255),
 primary key(task_id), foreign key(project_id) references projects(project_id)
 );
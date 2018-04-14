drop table if exists account;
create table account (
  id integer primary key autoincrement,
  name text not null
);

drop table if exists menu;
create table menu (
  id integer primary key autoincrement,
  name text not null,
  price double not null
)

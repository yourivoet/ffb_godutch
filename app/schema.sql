drop table if exists account;
create table account (
  id integer primary key autoincrement,
  name text not null,
  tokens double not null
);

-- *********************************************
-- * SQL MySQL generation                      
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Tue Dec 12 14:38:21 2023 
-- * LUN file:  
-- * Schema: MLD/1-1 
-- ********************************************* 


-- Database Section
-- ________________ 

create database db_pybot;
use db_pybot;


-- Tables Section
-- _____________ 

create table playlist (
     id_playlist int not null auto_increment,
     name varchar(200) not null,
     constraint ID_playlist_ID primary key (id_playlist));

create table server (
     id_server int not null auto_increment,
     guildId bigint not null unique,
     name varchar(30) not null,
     constraint ID_server_ID primary key (id_server));

create table file (
     id_file int not null auto_increment,
     name varchar(200) not null,
     path varchar(350) not null,
     fk_server int not null,
     constraint ID_file_ID primary key (id_file));

create table music (
     id_file int not null,
     constraint FKfil_mus_ID primary key (id_file));

create table music_playlist (
     id_file int not null,
     id_playlist int not null,
     constraint ID_music_playlist_ID primary key (id_file, id_playlist));


-- Constraints Section
-- ___________________ 

alter table file add constraint FKis_composed_FK
     foreign key (fk_server)
     references server (id_server);

alter table music add constraint FKfil_mus_FK
     foreign key (id_file)
     references file (id_file);

alter table music_playlist add constraint FKmus_pla_FK
     foreign key (id_playlist)
     references playlist (id_playlist);

alter table music_playlist add constraint FKmus_mus
     foreign key (id_file)
     references music (id_file);


-- Index Section
-- _____________ 

create unique index ID_playlist_IND
     on playlist (id_playlist);

create unique index ID_server_IND
     on server (id_server);

create unique index ID_file_IND
     on file (id_file);

create index FKis_composed_IND
     on file (fk_server);

create unique index FKfil_mus_IND
     on music (id_file);

create unique index ID_music_playlist_IND
     on music_playlist (id_file, id_playlist);

create index FKmus_pla_IND
     on music_playlist (id_playlist);


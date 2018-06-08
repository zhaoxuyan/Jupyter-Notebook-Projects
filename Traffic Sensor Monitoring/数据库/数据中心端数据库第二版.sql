drop table if exists cdb$

drop table if exists cdsjb$

drop table if exists gcxmb$

/*==============================================================*/
/* Table: cdb                                                   */
/*==============================================================*/
create table cdb
(
   gcxmbm               varchar(16) not null comment '工程项目编码',
   cdbm                 varchar(16) not null comment '测点编码',
   cdmc                 varchar(100) not null comment '测点名称',
   cgqbm                varchar(100) comment '传感器编码',
   jldw                 varchar(10) not null comment '计量单位',
   sfqy                 char(1) not null default '1' comment '是否启用',
   sjlx                 char(1) not null comment '数据类型',
   sflb                 char(1) not null default '0' comment '是否滤波',
   lbfs                 smallint comment '滤波方式',
   lbcs                 text comment '滤波参数',
   bz                   varchar(254) comment '备注',
   primary key (gcxmbm, cdbm)
)
engine = InnoDB
auto_increment = 1
default charset = utf8
collate = utf8_general_ci$

alter table cdb comment '测点表'$

/*==============================================================*/
/* Table: cdsjb                                                 */
/*==============================================================*/
create table cdsjb
(
   gcxmbm               varchar(16) not null comment '工程项目编码',
   cdbm                 varchar(16) not null comment '测点编码',
   clsj                 datetime not null comment '测量时间',
   avg                  numeric(18,6) comment '均值',
   max                  numeric(18,6) comment '最大值',
   min                  numeric(18,6) comment '最小值',
   inst                 numeric(18,6) comment '瞬时值',
   tsz                  varchar(254) comment '特殊值',
   glz                  numeric(18,6) comment '关联值',
   primary key (gcxmbm, cdbm, clsj)
)
engine = InnoDB
auto_increment = 1
default charset = utf8
collate = utf8_general_ci$

alter table cdsjb comment '测点数据表'$

/*==============================================================*/
/* Table: gcxmb                                                 */
/*==============================================================*/
create table gcxmb
(
   gcxmbm               varchar(16) not null comment '工程项目编码',
   gcxmmc               varchar(200) not null comment '工程项目名称',
   primary key (gcxmbm)
)
engine = InnoDB
auto_increment = 1
default charset = utf8
collate = utf8_general_ci$

alter table gcxmb comment '工程项目表'$

alter table cdb add constraint FK_Relationship_1 foreign key (gcxmbm)
      references gcxmb (gcxmbm) on delete restrict on update restrict$

alter table cdsjb add constraint FK_Relationship_2 foreign key (gcxmbm, cdbm)
      references cdb (gcxmbm, cdbm) on delete restrict on update restrict$

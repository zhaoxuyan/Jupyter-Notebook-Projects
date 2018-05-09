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
collate = utf8_general_ci;

alter table cdb comment '测点表';

/*==============================================================*/
/* Table: cdsjb                                                 */
/*==============================================================*/
create table cdsjb
(
   cdsjid               int not null auto_increment comment '测点数据ID',
   gcxmbm               varchar(16) not null comment '工程项目编码',
   cdbm                 varchar(16) not null comment '测点编码',
   clsj                 datetime not null comment '测量时间',
   avg                  numeric(18,6) comment '均值',
   max                  numeric(18,6) comment '最大值',
   min                  numeric(18,6) comment '最小值',
   inst                 numeric(18,6) comment '瞬时值',
   tsz                  varchar(254) comment '特殊值',
   glz                  numeric(18,6) comment '关联值',
   primary key (cdsjid)
)
engine = InnoDB
auto_increment = 1
default charset = utf8
collate = utf8_general_ci;

alter table cdsjb comment '测点数据表';

/*==============================================================*/
/* Table: cgqpzmxb                                              */
/*==============================================================*/
create table cgqpzmxb
(
   sjcjtdh              varchar(16) not null comment '数据采集通道号',
   mxh                  smallint not null comment '明细号',
   sm                   varchar(64) not null comment '说明',
   zl                   varchar(200) not null comment '指令',
   jssjcd               smallint not null comment '接收数据长度',
   cgqbh                varchar(200) comment '传感器编号',
   ys                   smallint not null comment '延时',
   primary key (sjcjtdh, mxh)
)
engine = InnoDB
auto_increment = 1
default charset = utf8
collate = utf8_general_ci;

alter table cgqpzmxb comment '传感器配置明细表';

/*==============================================================*/
/* Table: cgqpzzb                                               */
/*==============================================================*/
create table cgqpzzb
(
   sjcjtdh              varchar(16) not null comment '数据采集通道号',
   tdmc                 varchar(200) not null comment '通道名称',
   IP                   varchar(16) not null comment 'IP',
   port                 int not null comment 'port',
   bz                   varchar(254) comment '备注',
   primary key (sjcjtdh)
)
engine = InnoDB
auto_increment = 1
default charset = utf8
collate = utf8_general_ci;

alter table cgqpzzb comment '传感器配置主表';

/*==============================================================*/
/* Table: cgqsjjxb                                              */
/*==============================================================*/
create table cgqsjjxb
(
   sjcjtdh              varchar(16) not null comment '数据采集通道号',
   mxh                  smallint not null comment '明细号',
   gcxmbm               varchar(16) not null comment '工程项目编码',
   cdbm                 varchar(16) not null comment '测点编码',
   avg_gs               text comment '均值公式',
   max_gs               text comment '最大值公式',
   min_gs               text comment '最小值公式',
   inst_gs              text comment '瞬时值公式',
   tsz_gs               text comment '特殊值公式',
   glz_gs               text comment '关联值公式',
   primary key (gcxmbm, sjcjtdh, mxh, cdbm)
)
engine = InnoDB
auto_increment = 1
default charset = utf8
collate = utf8_general_ci;

alter table cgqsjjxb comment '传感器数据解析表';

/*==============================================================*/
/* Table: cgqsjyzb                                              */
/*==============================================================*/
create table cgqsjyzb
(
   sjcjtdh              varchar(16) not null comment '数据采集通道号',
   mxh                  smallint not null comment '明细号',
   xh                   smallint not null comment 'xh',
   yzgs                 text not null comment '验证公式',
   primary key (sjcjtdh, mxh, xh)
)
engine = InnoDB
auto_increment = 1
default charset = utf8
collate = utf8_general_ci;

alter table cgqsjyzb comment '传感器数据验证表';

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
collate = utf8_general_ci;

alter table gcxmb comment '工程项目表';

alter table cdb add constraint FK_Relationship_1 foreign key (gcxmbm)
      references gcxmb (gcxmbm) on delete restrict on update restrict;

alter table cdsjb add constraint FK_Relationship_2 foreign key (gcxmbm, cdbm)
      references cdb (gcxmbm, cdbm) on delete restrict on update restrict;

alter table cgqpzmxb add constraint FK_Relationship_3 foreign key (sjcjtdh)
      references cgqpzzb (sjcjtdh) on delete restrict on update restrict;

alter table cgqsjjxb add constraint FK_Relationship_5 foreign key (sjcjtdh, mxh)
      references cgqpzmxb (sjcjtdh, mxh) on delete restrict on update restrict;

alter table cgqsjjxb add constraint FK_Relationship_6 foreign key (gcxmbm, cdbm)
      references cdb (gcxmbm, cdbm) on delete restrict on update restrict;

alter table cgqsjyzb add constraint FK_Relationship_4 foreign key (sjcjtdh, mxh)
      references cgqpzmxb (sjcjtdh, mxh) on delete restrict on update restrict;

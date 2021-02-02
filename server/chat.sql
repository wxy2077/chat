-- 用户表
CREATE TABLE `chat_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_delete` int(11) DEFAULT '0' COMMENT '逻辑删除:0=未删除,1=删除',
  `user_id` varchar(32) NOT NULL COMMENT '用户id',
  `username` varchar(32) NOT NULL COMMENT '登录用户名',
  `hashed_password` varchar(128) NOT NULL COMMENT 'hash后的密码',
  `email` varchar(128) DEFAULT NULL COMMENT '邮箱',
  `phone` varchar(16) DEFAULT NULL COMMENT '手机号',
  `nickname` varchar(128) DEFAULT NULL COMMENT '管理员昵称',
  `avatar` varchar(256) DEFAULT NULL COMMENT '管理员头像',
  `is_active` int(11) DEFAULT '0' COMMENT '邮箱是否激活 0=未激活 1=激活',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `ix_admin_user_email` (`email`),
  UNIQUE KEY `ix_admin_user_phone` (`phone`),
  KEY `ix_admin_user_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
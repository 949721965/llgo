CREATE DATABASE llgo DEFAULT CHARSET UTF8;
use llgo;

-- 招聘信息表
CREATE TABLE `employinfo`
(
    `id` INT NOT NULL,                   -- 索引值
    `category` CHAR(2) NOT NULL,         -- 职位分类
    `branch` VARCHAR(8) NOT NULL,        -- 职位分支
    `position` VARCHAR(18) NOT NULL,     -- 职位名称
    `jobname` VARCHAR(22) NOT NULL,      -- 工作名称
    `salarylower` TINYINT NOT NULL,      -- 薪资最低（单位k)
    `salaryupper` TINYINT NOT NULL,      -- 薪资最高（单位k)    
    `location` VARCHAR(16) NOT NULL,     -- 工作地点
    `experience` VARCHAR(12) NOT NULL,   -- 工作经验
    `education` CHAR(5) NOT NULL,        -- 学历要求
    `advantage` VARCHAR(24) NOT NULL,    -- 工作诱惑
    `duties` TEXT NOT NULL,              -- 工作职责
    `claim` TEXT NOT NULL,               -- 技能要求
    `companyname` VARCHAR(18) NOT NULL,  -- 公司名称
    `companyfield` VARCHAR(20) NOT NULL, -- 公司领域
    `financing` CHAR(5) NOT NULL,        -- 融资情况
    `scalelower` SMALLINT NOT NULL,      -- 公司规模（不小于）
    `scaleupper` SMALLINT NOT NULL,      -- 公司规模（不大于）
    PRIMARY KEY(`id`)
)ENGINE=MyISAM DEFAULT CHARSET=UTF8;

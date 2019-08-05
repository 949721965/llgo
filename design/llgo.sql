CREATE DATABASE llgo DEFAULT CHARSET UTF8;
use llgo;

CREATE TABLE `employ`
(
    `mark` INT NOT NULL,
    `category` CHAR(6) NOT NULL,
    `branch` VARCHAR(5) NOT NULL,
    `job` VARCHAR(10) NOT NULL,
    `job_name` varchar(20) NOT NULL,
    `salary_lower` TINYINT NOT NULL,
    `salary_upper` TINYINT NOT NULL,    
    `area` VARCHAR(10) NOT NULL,
    `experience` VARCHAR(5) NOT NULL,
    `education` CHAR(15) NOT NULL,
    `labels` VARCHAR(65) NOT NULL,
    `advantage` VARCHAR(45) NOT NULL,
    `requirement` TEXT NOT NULL,
    PRIMARY KEY(`mark`)
)ENGINE=MyISAM DEFAULT CHARSET=UTF8;

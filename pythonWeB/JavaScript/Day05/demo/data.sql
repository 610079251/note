CREATE DATABASE python;

USE python;

CREATE TABLE users(
   id SMALLINT UNSIGNED NOT NULL KEY AUTO_INCREMENT,
   username VARCHAR(20) NOT NULL UNIQUE,
   password VARCHAR(20) NOT NULL
);

INSERT users(username,password) VALUES('tom','tom');
INSERT users(username,password) VALUES('john','john');
INSERT users(username,password) VALUES('rose','rose');

-- SQL注入
-- 假设用户名: 123456
-- 假设密码为: a' or '1'='1
-- 此时SQL结果为
-- SELECT * FROM users WHERE username='123456' and password='a' or '1'='1';
-- 结果为数据表的全部记录,证明登录成功
-- 解决方案:将输入字符中的特殊符号替换为对应的HTML实体
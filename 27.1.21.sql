/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.5.23 : Database - mechfinder
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mechfinder` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `mechfinder`;

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `message` varchar(1000) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(1000) DEFAULT NULL,
  `complaint_date` date DEFAULT NULL,
  `replay` varchar(1000) DEFAULT NULL,
  `replay_date` date DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`complaint`,`complaint_date`,`replay`,`replay_date`) values 
(1,1,'hello','2020-09-22','world','2020-09-22'),
(2,14,'python','2020-09-22','flask','2020-09-22'),
(3,17,'hai','2020-09-22','hi','2020-10-17'),
(4,16,'ggg','2020-10-03','fdgsdgsf','2020-11-06'),
(5,14,'dhgfjsf','2021-01-03',NULL,NULL),
(6,17,'suhail','2021-01-09','nizam','2021-01-09'),
(7,17,'suhail','2021-01-09',NULL,NULL),
(8,17,'nizam','2021-01-09',NULL,NULL),
(9,17,'','2021-01-09',NULL,NULL),
(10,17,'fasil','2021-01-09',NULL,NULL),
(11,17,'yu','2021-01-25',NULL,NULL),
(12,17,'ggg','2021-01-25',NULL,NULL);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(1000) DEFAULT NULL,
  `feedback_date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`feedback_date`) values 
(1,1,'Hello world','2020-09-19'),
(2,2,'hai android','2020-09-19'),
(3,14,'gdhjfgas','2021-01-03'),
(4,17,'hai','2021-01-09'),
(5,17,'g','2021-01-26'),
(6,17,'g','2021-01-26');

/*Table structure for table `gallery` */

DROP TABLE IF EXISTS `gallery`;

CREATE TABLE `gallery` (
  `gallery_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`gallery_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `gallery` */

insert  into `gallery`(`gallery_id`,`shop_id`,`image`,`date`) values 
(1,2,'gallery_1.jpg','2020-09-11'),
(2,2,'gallery_2.jpg','2020-09-18'),
(3,2,'gallery_3.jpg','2020-09-18'),
(4,13,'gallery_4.jpg','2020-09-18'),
(5,13,'gallery_5.jpg','2020-09-18'),
(6,13,'gallery_6.jpg','2020-09-18'),
(15,10,'gallery_15.jpg','2020-10-19'),
(17,10,'gallery_17.jpg','2020-10-19'),
(18,10,'gallery_18.jpg','2020-10-19'),
(19,10,'gallery_19.jpg','2020-10-19');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'ajm','ajm','owner'),
(3,'fwlswb@hi2.in','asd','pending'),
(4,'donbr@hi2.in','as','owner'),
(5,'aj@gmail.com','12','rejected'),
(6,'ajm@gmail.com','123','owner'),
(7,'abc@gmail.com','123','pending'),
(9,'ajma@dsa.bo','sfdg','owner'),
(10,'jaz@gmail.com','123','owner'),
(11,'pk','123','admin'),
(12,'rahul@gmail.com','123','rejected'),
(14,'123@gmail.com','123','owner'),
(15,'apple@gmail.com','apple','pending'),
(16,'apple@gmail.com','123','owner'),
(17,'ajm@gmail.com','111','user'),
(18,'ggg','666','user'),
(19,'ggg','666','user'),
(20,'ggg','666','user'),
(21,'ajm','444','user'),
(22,'jdhdh','123','user'),
(23,'hdhdh','124','user'),
(24,'vshhs','444','user'),
(25,'hhhh','333','user'),
(26,'ysysysy','444','user'),
(27,'jjj','ggg','user'),
(28,'yyy','333','user'),
(29,'hshhs','123','user'),
(30,'hshhs','123','user'),
(31,'yuwue','t55','user'),
(32,'yuwue','t55','user'),
(33,'uueu','uuu','user'),
(34,'ghdgd','yy','user'),
(35,'hhh','uuu','user'),
(36,'ggg','gg','user'),
(37,'bh','y7','user'),
(38,'ghdhd','hhs','user'),
(39,'uusi','jjs','user'),
(40,'usus','yyy','user'),
(41,'ysys','susj','user'),
(42,'gsgs','hwhw','user'),
(43,'ggdhd','dbsb','user'),
(44,'ty','gg','user'),
(45,'7777','666','user'),
(46,'ueue','usus','user');

/*Table structure for table `news` */

DROP TABLE IF EXISTS `news`;

CREATE TABLE `news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `news_title` varchar(100) DEFAULT NULL,
  `news_description` varchar(1000) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `news` */

insert  into `news`(`news_id`,`date`,`news_title`,`news_description`,`image`) values 
(1,'2020-09-22','bro','ajmal','news_1.jpg');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`date`,`subject`,`description`,`image`) values 
(6,'2020-10-23','gseg','sfdgggggggggggggggggs','notification_6.jpg'),
(7,'2020-10-23','dfcdsa','aaaaaaaaaaaaa','notification_7.jpg'),
(8,'2021-01-19','jh,hwd','gajhdsg','notification_8.jpg'),
(9,'2021-01-19','hdjkas','djsjf','notification_9.jpg'),
(10,'2021-01-19','hdjkas','djsjf','notification_10.jpg'),
(11,'2021-01-19','dsfsddsf','dfsaf','notification_11.jpg'),
(12,'2021-01-19','dsfsddsf','dfsaf','notification_12.jpg'),
(13,'2021-01-19','hfkjsdh','jdshaj','notification_13.jpg'),
(14,'2021-01-19','hfkjds','hsdkjah','notification_14.jpg'),
(15,'2021-01-19','ihjksd','dhsfjkh','notification_15.jpg'),
(16,'2021-01-19','hjkhfkja','dsjkhad','notification_16.jpg'),
(17,'2021-01-19','hjkhfkja','dsjkhad','notification_17.jpg'),
(18,'2021-01-25','dsfds','dsfsdf','notification_18.jpg'),
(19,'2021-01-25','sd','dsfdsdf','notification_19.jpg'),
(20,'2021-01-26','fgds','fsddfgsf','notification_20.jpg');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_request_id` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_request_id` int(11) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `date` date DEFAULT NULL,
  `feedback` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`service_request_id`,`rating`,`date`,`feedback`) values 
(1,1,5,'2020-09-19','hai'),
(2,2,4,'2020-09-19','hai l'),
(3,3,32,'2020-09-19','rrrrrrrr'),
(4,4,4,'2020-09-24','simje b'),
(5,2,2,'2021-01-03','hkjhdkjfga'),
(6,10,2,'2021-01-27','sfsg'),
(7,16,3,'2021-01-27','df');

/*Table structure for table `service_request` */

DROP TABLE IF EXISTS `service_request`;

CREATE TABLE `service_request` (
  `service_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `vehichle_id` int(11) DEFAULT NULL,
  `request_date` date DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `payment` int(11) DEFAULT NULL,
  `workshop_id` int(11) DEFAULT NULL,
  `parts` int(10) DEFAULT NULL,
  `discount` int(10) DEFAULT NULL,
  PRIMARY KEY (`service_request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `service_request` */

insert  into `service_request`(`service_request_id`,`user_id`,`vehichle_id`,`request_date`,`description`,`status`,`payment`,`workshop_id`,`parts`,`discount`) values 
(1,14,1,'2020-09-19','hellow','pending',565,6,NULL,NULL),
(2,15,2,'2020-09-19','koi','pending',8787,10,NULL,NULL),
(3,16,4,'2020-09-19','bro','approved',33,10,0,0),
(4,17,32,'2020-09-19','simje','pending',245,14,NULL,NULL),
(5,17,99999,'2020-09-22','jaz ','approved',9999,10,NULL,NULL),
(6,14,6666,'2020-09-07','jaz 11','approved',6666,10,NULL,NULL),
(7,1,1111,'2020-09-02','1 111','done',1111,10,NULL,NULL),
(8,2,2222,'2020-09-22','2  2222','done',2222,10,NULL,NULL),
(9,17,3333,'2020-09-22','17 33333','done',17,10,NULL,NULL),
(10,15,3,'2020-10-02','hai','pending',55788,10,NULL,NULL),
(11,16,4,'2020-10-02','service history','done',566,10,NULL,NULL),
(12,15,5,'2020-10-12','test history','done',17,10,8,3),
(13,17,9,'2021-01-27',NULL,'pending',NULL,2,NULL,NULL),
(14,17,9,'2021-01-27',NULL,'pending',NULL,2,NULL,NULL),
(15,17,9,'2021-01-27',NULL,'pending',NULL,2,NULL,NULL),
(16,17,9,'2021-01-27',NULL,'pending',NULL,2,NULL,NULL),
(17,17,9,'2021-01-27',NULL,'pending',NULL,2,NULL,NULL);

/*Table structure for table `services` */

DROP TABLE IF EXISTS `services`;

CREATE TABLE `services` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `service` varchar(300) DEFAULT NULL,
  `vehichle_type` varchar(30) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `services` */

insert  into `services`(`service_id`,`shop_id`,`service`,`vehichle_type`,`amount`) values 
(1,2,'water service','3 wheeler',1),
(2,2,'Painting','3 wheeler',6525),
(3,10,'Painting','3 wheeler',55),
(4,10,'water service','3 wheeler',6965),
(5,13,'Painting','3 wheeler',12),
(6,13,'water service','3 wheeler',312),
(7,13,'water service','3 wheeler',3213),
(8,6,'Painting','3 wheeler',424),
(9,14,'water service','3 wheeler',44),
(10,14,'water service','3 wheeler',34),
(11,10,'Ac service','3 wheeler',444);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `login_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `user_image` varchar(50) DEFAULT NULL,
  `pincode` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`login_id`,`user_id`,`name`,`email`,`phone`,`place`,`city`,`district`,`user_image`,`pincode`) values 
(14,1,'suhail','suhail@gmail.com','958654545','vengara','mlp','mlp','4454545.jpg',NULL),
(15,2,'fasil','fasil@gmnail.com','676297','thennala','kl','kl','32568.jpeg',NULL),
(16,3,'nizam','nizam@gmail.com','5656868','chemmad','y','y','6567.jpeg',NULL),
(1,5,'arshad','arshad','565656556','tvm','tvm','tvm','65565.jpeg',NULL),
(2,6,'sahad','shad','6565665','cochi','cochi','cochi','54545454.jpeg',NULL),
(NULL,7,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(NULL,8,'\"+username+\"','\"+email+\"','\"+phone+\"',NULL,NULL,NULL,NULL,NULL),
(18,9,'syha','syha','333',NULL,NULL,NULL,NULL,NULL),
(19,10,'syha','syha','333',NULL,NULL,NULL,'profile_19.jpg',NULL),
(20,11,'syha','syha','333',NULL,NULL,NULL,'profile_20.jpg',NULL),
(21,12,'suhail','suhail','666',NULL,NULL,NULL,'profile_21.jpg',NULL),
(22,13,'fasil','fasil','3333',NULL,NULL,NULL,'profile_22.jpg',NULL),
(23,14,'hhh','hhh','666',NULL,NULL,NULL,'profile_23.jpg',NULL),
(24,15,'hwh','hwh','66464',NULL,NULL,NULL,'profile_24.jpg',NULL),
(25,16,'yyy','yyy','6336',NULL,NULL,NULL,'profile_25.jpg',NULL),
(17,17,'jashim','ajm@gmail.com','666','tttt','mlp','mlp','profile_17.jpg',365),
(27,18,'yyy','yyy','333',NULL,NULL,NULL,'profile_27.jpg',NULL),
(28,19,'ggg','ggg','666',NULL,NULL,NULL,'profile_28.jpg',NULL),
(29,20,'tyyy','tyyy','6664',NULL,NULL,NULL,'profile_29.jpg',NULL),
(30,21,'tyyy','tyyy','6664',NULL,NULL,NULL,'profile_30.jpg',NULL),
(31,22,'yy','yy','333',NULL,NULL,NULL,'profile_31.jpg',NULL),
(32,23,'yy','yy','333',NULL,NULL,NULL,'profile_32.jpg',NULL),
(33,24,'mm','mm','33',NULL,NULL,NULL,'profile_33.jpg',NULL),
(34,25,'iir','iir','6265',NULL,NULL,NULL,'profile_34.jpg',NULL),
(35,26,'iii','iii','6666',NULL,NULL,NULL,'profile_35.jpg',NULL),
(36,27,'hhh','hhh','336',NULL,NULL,NULL,'profile_36.jpg',NULL),
(37,28,'uh','uh','36',NULL,NULL,NULL,'profile_37.jpg',NULL),
(38,29,'yhe','yhe','66565',NULL,NULL,NULL,'profile_38.jpg',NULL),
(39,30,'jjw','jjw','6656',NULL,NULL,NULL,'profile_39.jpg',NULL),
(40,31,'ueu','ueu','3434',NULL,NULL,NULL,'profile_40.jpg',NULL),
(41,32,'uej','uej','665',NULL,NULL,NULL,'profile_41.jpg',NULL),
(42,33,'hwh','hwh','6464',NULL,NULL,NULL,'profile_42.jpg',NULL),
(43,34,'ywh','ywh','6464',NULL,NULL,NULL,'profile_43.jpg',NULL),
(44,35,'nizam','nizam','23','uue','7e7','u7e','profile_44.jpg',556),
(45,36,'ummer','ummer','333','888','888','888','profile_45.jpg',333),
(46,37,'yye','yye','6646','77','999','999','profile_46.jpg',9999);

/*Table structure for table `user_service` */

DROP TABLE IF EXISTS `user_service`;

CREATE TABLE `user_service` (
  `user_service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_request_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `user_service` */

insert  into `user_service`(`user_service_id`,`service_request_id`,`service_id`,`amount`) values 
(1,2,3,6666),
(2,2,11,7777),
(3,3,11,8),
(4,11,11,6565),
(5,3,3,16),
(6,3,3,9),
(7,12,3,5),
(8,12,11,7),
(9,14,2,6525),
(10,14,1,1),
(11,15,2,6525),
(12,15,1,1),
(13,16,2,6525),
(14,16,1,1),
(15,17,2,6525),
(16,17,1,1);

/*Table structure for table `vehicle` */

DROP TABLE IF EXISTS `vehicle`;

CREATE TABLE `vehicle` (
  `vehicle_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `vehicle_type` varchar(30) DEFAULT NULL,
  `company` varchar(30) DEFAULT NULL,
  `model` varchar(30) DEFAULT NULL,
  `manfctr_year` varchar(30) DEFAULT NULL,
  `image` varchar(30) DEFAULT NULL,
  `regno` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `vehicle` */

insert  into `vehicle`(`vehicle_id`,`user_id`,`vehicle_type`,`company`,`model`,`manfctr_year`,`image`,`regno`) values 
(1,14,'4 wheelar','ford','suv','2015','7465724.jpeg',NULL),
(2,15,'4 wheelar','ford','sg','2020','7853.jpeg',NULL),
(3,15,'2 wheelwer','ec','aw','4555','lfhdgj.jpeg',NULL),
(4,16,'3 wheelaer','j','hh','6775','jfdshg.jpeg',NULL),
(5,15,'6','ajm','s','888','j.jpg',NULL),
(6,14,'4','mm','hh','777','6652675.jpg',NULL),
(8,17,'3 wheeler','bajaj','yyy','33','vehicle_8.jpg','66'),
(9,17,'3 wheeler','bajaj','yyy','33','vehicle_9.jpg','66'),
(10,17,'3 wheeler','bajaj','yyy','33','vehicle_10.jpg','66'),
(11,46,'3 wheeler','bajaj','yyy','999','vehicle_11.jpg','888');

/*Table structure for table `vehicledb` */

DROP TABLE IF EXISTS `vehicledb`;

CREATE TABLE `vehicledb` (
  `vehicledb` int(11) NOT NULL,
  `vehicle_type` varchar(50) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`vehicledb`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `vehicledb` */

insert  into `vehicledb`(`vehicledb`,`vehicle_type`,`company`,`model`) values 
(1,'3 wheeler','bajaj','yyy'),
(2,'4 wheeler','toyota','etios'),
(3,'2 wheeler','hero','glamur'),
(4,'4 wheeler','maruthi','800');

/*Table structure for table `workshop` */

DROP TABLE IF EXISTS `workshop`;

CREATE TABLE `workshop` (
  `shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `shop_name` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `shop_lisence` varchar(30) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `lati` varchar(30) DEFAULT NULL,
  `longi` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`shop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `workshop` */

insert  into `workshop`(`shop_id`,`login_id`,`shop_name`,`place`,`city`,`district`,`pincode`,`email`,`shop_lisence`,`phone`,`lati`,`longi`) values 
(1,4,'rwte','fds','sfgsfd','dddddddddddddd',543555555,'donbr@hi2.in','worckshop_1.jpg','9048256015','1','23'),
(2,5,'ajm','ibz','mjr','mpm',676509,'aj@gmail.com','worckshop_2.jpg','9048256015','11.0510','76.0711'),
(3,6,'ajmal','ajm','go sg','sfdg',676509,'ajm@gmail.com','worckshop_3.jpg','9048256015','44','55'),
(4,7,'abc','abc','abc','abc',676509,'abc@gmail.com','worckshop_4.jpg','9048256015','34','56'),
(6,9,'yafir','ya','ya','gaffs ',676509,'ajma@dsa.bo','worckshop_6.jpg','9048256015','56','34'),
(7,10,'jaz1','mlp','mlp','mlp',676509,'jaz@gmail.com','worckshop_10.jpg','9048256015','11.0510','76.0711'),
(8,12,'rahul','rahul','rahul','rahul',6565,'rahul@gmail.com','worckshop_8.jpg','9048256015','34','45'),
(10,14,'simje','kl','kannur','kannur',674675,'123@gmail.com','worckshop_10.jpg','9048256015','67','45'),
(11,16,'apple','apple','apple','apple',3214,'apple@gmail.com','worckshop_11.jpg','56456357','89','34');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

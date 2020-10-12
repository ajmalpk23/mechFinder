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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`complaint`,`complaint_date`,`replay`,`replay_date`) values 
(1,1,'hello','2020-09-22','world','2020-09-22'),
(2,14,'python','2020-09-22','flask','2020-09-22'),
(3,17,'hai','2020-09-22','bro','2020-09-22'),
(4,16,'ggg','2020-10-03','wedfdsa','2020-10-03');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(1000) DEFAULT NULL,
  `feedback_date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`feedback_date`) values 
(1,1,'Hello world','2020-09-19'),
(2,2,'hai android','2020-09-19');

/*Table structure for table `gallery` */

DROP TABLE IF EXISTS `gallery`;

CREATE TABLE `gallery` (
  `gallery_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`gallery_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `gallery` */

insert  into `gallery`(`gallery_id`,`shop_id`,`image`,`date`) values 
(1,2,'gallery_1.jpg','2020-09-11'),
(2,2,'gallery_2.jpg','2020-09-18'),
(3,2,'gallery_3.jpg','2020-09-18'),
(4,13,'gallery_4.jpg','2020-09-18'),
(5,13,'gallery_5.jpg','2020-09-18'),
(6,13,'gallery_6.jpg','2020-09-18'),
(7,10,'gallery_7.jpg','2020-10-10'),
(8,10,'gallery_8.jpg','2020-10-10'),
(9,10,'gallery_9.jpg','2020-10-10'),
(10,10,'gallery_10.jpg','2020-10-10');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'ajm','ajm','owner'),
(3,'fwlswb@hi2.in','asd','pending'),
(4,'donbr@hi2.in','as','owner'),
(5,'aj@gmail.com','12','pending'),
(6,'ajm@gmail.com','123','owner'),
(7,'abc@gmail.com','123','pending'),
(9,'ajma@dsa.bo','sfdg','owner'),
(10,'jaz@gmail.com','123','owner'),
(11,'pk','123','admin'),
(12,'rahul@gmail.com','123','rejected'),
(14,'123@gmail.com','123','owner'),
(15,'apple@gmail.com','apple','pending'),
(16,'apple@gmail.com','123','owner');

/*Table structure for table `news` */

DROP TABLE IF EXISTS `news`;

CREATE TABLE `news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `news_title` varchar(100) DEFAULT NULL,
  `news_description` varchar(1000) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `news` */

insert  into `news`(`news_id`,`date`,`news_title`,`news_description`,`image`) values 
(1,'2020-09-22','bro','ajmal','news_1.jpg'),
(2,'2020-10-09','asg','test','news_2.jpg');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`date`,`subject`,`description`,`image`) values 
(1,'2020-09-05','dsgsfgs','sgfsfdg','notification_1.jpg'),
(2,'2020-09-12','abc hdgf','dafshjkadshkjfhd4534132dsfahdsafds3.\r\na3\r\na3dsfadsfb,jdsahgjkfads','notification_2.jpg'),
(3,'2020-09-22','asdas','adafewa','notification_3.jpg');

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`service_request_id`,`rating`,`date`,`feedback`) values 
(1,1,5,'2020-09-19','hai'),
(2,2,4,'2020-09-19','hai l'),
(3,3,32,'2020-09-19','rrrrrrrr'),
(4,4,4,'2020-09-24','simje b');

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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

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
(12,15,5,'2020-10-12','test history','done',17,10,8,3);

/*Table structure for table `services` */

DROP TABLE IF EXISTS `services`;

CREATE TABLE `services` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `service` varchar(300) DEFAULT NULL,
  `vehichle_type` varchar(30) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `services` */

insert  into `services`(`service_id`,`shop_id`,`service`,`vehichle_type`,`amount`) values 
(1,2,'water service','3 wheeler',1),
(2,2,'water service','3 wheeler',6525),
(3,10,'water service','3 wheeler',55),
(4,10,'water service','3 wheeler',6965),
(5,13,'water service','3 wheeler',12),
(6,13,'water service','3 wheeler',312),
(7,13,'water service','3 wheeler',3213),
(8,6,'water service','3 wheeler',424),
(9,14,'water service','3 wheeler',44),
(10,14,'water service','3 wheeler',34),
(11,10,'Ac service','3 wheeler',444);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `user_image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`name`,`email`,`phone`,`place`,`city`,`district`,`user_image`) values 
(1,14,'suhail','suhail@gmail.com','958654545','vengara','mlp','mlp','4454545.jpg'),
(2,15,'fasil','fasil@gmnail.com','676297','thennala','kl','kl','32568.jpeg'),
(3,16,'nizam','nizam@gmail.com','5656868','chemmad','y','y','6567.jpeg'),
(4,17,'jashim','jashim@gmail.com','54524','ibz','mlp','mlp','5648256.jpeg'),
(5,1,'arshad','arshad','565656556','tvm','tvm','tvm','65565.jpeg'),
(6,2,'sahad','shad','6565665','cochi','cochi','cochi','54545454.jpeg'),
(7,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `user_service` */

DROP TABLE IF EXISTS `user_service`;

CREATE TABLE `user_service` (
  `user_service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_request_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `user_service` */

insert  into `user_service`(`user_service_id`,`service_request_id`,`service_id`,`amount`) values 
(1,2,3,6666),
(2,2,11,7777),
(3,3,11,8),
(4,11,11,6565),
(5,3,3,16),
(6,3,3,9),
(7,12,3,5),
(8,12,11,7);

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
  PRIMARY KEY (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `vehicle` */

insert  into `vehicle`(`vehicle_id`,`user_id`,`vehicle_type`,`company`,`model`,`manfctr_year`,`image`) values 
(1,14,'4 wheelar','ford','suv','2015','7465724.jpeg'),
(2,15,'4 wheelar','ford','sg','2020','7853.jpeg'),
(3,15,'2 wheelwer','ec','aw','4555','lfhdgj.jpeg'),
(4,16,'3 wheelaer','j','hh','6775','jfdshg.jpeg'),
(5,15,'6','ajm','s','888','j.jpg');

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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `workshop` */

insert  into `workshop`(`shop_id`,`login_id`,`shop_name`,`place`,`city`,`district`,`pincode`,`email`,`shop_lisence`,`phone`,`lati`,`longi`) values 
(1,4,'rwte','fds','sfgsfd','dddddddddddddd',543555555,'donbr@hi2.in','worckshop_1.jpg','9048256015','45423','46534'),
(2,5,'ajm','ibz','mjr','mpm',676509,'aj@gmail.com','worckshop_2.jpg','9048256015','12','34'),
(3,6,'ajmal','ajm','go sg','sfdg',676509,'ajm@gmail.com','worckshop_3.jpg','9048256015','sdfg','fdgdsf'),
(4,7,'abc','abc','abc','abc',676509,'abc@gmail.com','worckshop_4.jpg','9048256015','66654','6565'),
(6,9,'yafir','ya','ya','gaffs ',676509,'ajma@dsa.bo','worckshop_6.jpg','9048256015','sfdg','fdsgsf'),
(7,10,'jaz1','mlp','mlp','mlp',676509,'jaz@gmail.com','worckshop_10.jpg','9048256015','55','66'),
(8,12,'rahul','rahul','rahul','rahul',6565,'rahul@gmail.com','worckshop_8.jpg','9048256015','5416','324152'),
(10,14,'simje','kl','kannur','kannur',674675,'123@gmail.com','worckshop_10.jpg','9048256015','67','888'),
(11,16,'apple','apple','apple','apple',3214,'apple@gmail.com','worckshop_11.jpg','56456357','thgfgf','sfgsdg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

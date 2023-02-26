-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.34


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema child
--

CREATE DATABASE IF NOT EXISTS child;
USE child;

--
-- Definition of table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `idadmin` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`idadmin`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` (`idadmin`,`username`,`password`) VALUES 
 (1,'admin','admin');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;


--
-- Definition of table `parent`
--

DROP TABLE IF EXISTS `parent`;
CREATE TABLE `parent` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ChildName` varchar(45) NOT NULL,
  `ParentName` varchar(45) NOT NULL,
  `phoneNumber` varchar(45) NOT NULL,
  `Emailid` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `AadharNo` varchar(45) NOT NULL,
  `photo` blob NOT NULL,
  `FIRcopy` blob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parent`
--

/*!40000 ALTER TABLE `parent` DISABLE KEYS */;
/*!40000 ALTER TABLE `parent` ENABLE KEYS */;


--
-- Definition of table `public`
--

DROP TABLE IF EXISTS `public`;
CREATE TABLE `public` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `PublicName` varchar(45) NOT NULL,
  `Mobilenumber` varchar(45) NOT NULL,
  `PublicAddress` varchar(45) NOT NULL,
  `PublicAadharNo` varchar(45) NOT NULL,
  `photo` blob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `public`
--

/*!40000 ALTER TABLE `public` DISABLE KEYS */;
/*!40000 ALTER TABLE `public` ENABLE KEYS */;


--
-- Definition of table `reg_parent`
--

DROP TABLE IF EXISTS `reg_parent`;
CREATE TABLE `reg_parent` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `mobilenumber` varchar(45) NOT NULL,
  `emailid` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `pincode` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reg_parent`
--

/*!40000 ALTER TABLE `reg_parent` DISABLE KEYS */;
/*!40000 ALTER TABLE `reg_parent` ENABLE KEYS */;


--
-- Definition of table `reg_volunty`
--

DROP TABLE IF EXISTS `reg_volunty`;
CREATE TABLE `reg_volunty` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `mobilenumber` varchar(45) NOT NULL,
  `emailid` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `pincode` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reg_volunty`
--

/*!40000 ALTER TABLE `reg_volunty` DISABLE KEYS */;
/*!40000 ALTER TABLE `reg_volunty` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

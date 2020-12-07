-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2020 at 11:44 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `users`
--

-- --------------------------------------------------------

--
-- Table structure for table `coursedetails`
--

CREATE TABLE `coursedetails` (
  `Course-Name` varchar(100) NOT NULL,
  `Fees` varchar(100) NOT NULL,
  `Duration` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `coursedetails`
--

INSERT INTO `coursedetails` (`Course-Name`, `Fees`, `Duration`) VALUES
('Programming', 'Rs.12000', '3 Months'),
('web-development', 'Rs.10000', '2 Months'),
('android-development', 'Rs.15000', '4 Month'),
('cloud-computing', 'Rs.12000', '2 Months\r\n'),
('database-management', 'Rs.9000', '1.5 Months'),
('network & security', 'Rs.8000', '2 Month');

-- --------------------------------------------------------

--
-- Table structure for table `courseregisteration`
--

CREATE TABLE `courseregisteration` (
  `username` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `courseregisteration`
--

INSERT INTO `courseregisteration` (`username`, `course`) VALUES
('viren', 'web-development'),
('veer', 'programming'),
('dave', 'cloud-computing'),
('virend', 'cloud-computing');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `Available-course` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`Available-course`) VALUES
('programming'),
('web-development'),
('android-development'),
('cloud-computing'),
('database-management'),
('network & security');

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `Username` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `Age` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `signup`
--

INSERT INTO `signup` (`Username`, `City`, `Age`) VALUES
('viren', 'Mumbai', 20),
('Veer', 'Jaipur', 22),
('viren dave', 'mumbai', 21);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

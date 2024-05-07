-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 07, 2024 at 10:59 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ppes`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(255) NOT NULL,
  `rfid` varchar(255) NOT NULL,
  `img` varchar(255) NOT NULL,
  `emp_name` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `time_inAm` varchar(255) NOT NULL,
  `time_outAm` varchar(255) NOT NULL,
  `time_inPm` varchar(255) NOT NULL,
  `time_outPm` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `rfid`, `img`, `emp_name`, `date`, `time_inAm`, `time_outAm`, `time_inPm`, `time_outPm`) VALUES
(9, '1438160345', 'static/assets/pics/437190466_198322000042476_7287341850275978152_n.png', 'Sam Sung', '2024-05-08', '04:20:50', '04:50:31', '-', '-'),
(10, '0188866075', 'static/assets/pics/309425388_466872745481320_6351313889051477041_n.jpg', 'bgdhs xvsz', '2024-05-08', '04:23:47', '-', '04:42:58', '-'),
(11, '1437418009', 'static/assets/pics/Blue Yellow Modern Computer Repair Service Medium Banner (24 x 36 in).png', 'nin anne', '2024-05-08', '04:24:24', '-', '-', '04:57:43');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `id` int(255) NOT NULL,
  `img` varchar(255) NOT NULL,
  `rfid` varchar(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`id`, `img`, `rfid`, `fname`, `lname`, `department`) VALUES
(2, 'static/assets/pics/Blue Yellow Modern Computer Repair Service Medium Banner (24 x 36 in).png', '1437418009', 'nin', 'anne', 'english'),
(3, 'static/assets/pics/309425388_466872745481320_6351313889051477041_n.jpg', '0188866075', 'bgdhs', 'xvsz', 'dvsvs'),
(6, 'static/assets/pics/437190466_198322000042476_7287341850275978152_n.png', '1438160345', 'Sam', 'Sung', 'english');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rfid` (`rfid`) USING BTREE;

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rfid` (`rfid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `data`
--
ALTER TABLE `data`
  ADD CONSTRAINT `data_ibfk_1` FOREIGN KEY (`rfid`) REFERENCES `employees` (`rfid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

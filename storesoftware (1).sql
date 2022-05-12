-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 22, 2021 at 04:03 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `storesoftware`
--

-- --------------------------------------------------------

--
-- Table structure for table `addtocart`
--

CREATE TABLE `addtocart` (
  `id` int(11) NOT NULL,
  `productid` varchar(255) NOT NULL,
  `userid` varchar(11) NOT NULL,
  `invoice` varchar(255) NOT NULL,
  `totalquantity` varchar(255) NOT NULL,
  `totalamt` varchar(255) NOT NULL,
  `curdate` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addtocart`
--

INSERT INTO `addtocart` (`id`, `productid`, `userid`, `invoice`, `totalquantity`, `totalamt`, `curdate`) VALUES
(409, '12', '6', '4042', '9', '4950', '2021-11-24'),
(410, '15', '6', '4042', '3', '60', '2021-11-24'),
(411, '12', '3', '8750', '6', '3300', '2021-11-24'),
(412, '20', '3', '8750', '6', '156', '2021-11-24'),
(413, '14', '2', '5773', '100', '500', '2021-11-24'),
(414, '20', '2', '5773', '100', '2600', '2021-11-24'),
(415, '13', '3', '9530', '100', '1000', '2021-11-24'),
(416, '20', '3', '9530', '10', '260', '2021-11-24'),
(417, '13', '6', '5540', '8', '80', '2021-11-24'),
(418, '20', '6', '5540', '9', '234', '2021-11-24'),
(419, '13', '7', '2070', '2', '20', '2021-11-24'),
(420, '21', '7', '2070', '6', '90', '2021-11-24'),
(421, '13', '7', '2881', '5', '50', '2021-11-24'),
(422, '21', '7', '2881', '8', '120', '2021-11-24'),
(423, '12', '3', '6757', '10', '5500', '2021-11-25'),
(424, '21', '3', '6757', '176', '2640', '2021-11-25'),
(425, '12', '6', '8535', '1', '0', '2021-11-25'),
(426, '13', '3', '3550', '1', '0', '2021-11-25'),
(427, '13', '3', '3550', '1', '0', '2021-11-25'),
(428, '12', '3', '2856', '1', '0', '2021-11-25'),
(429, '14', '3', '8256', '2', '10', '2021-11-25'),
(430, '12', '3', '8256', '20', '11000', '2021-11-25'),
(431, '20', '3', '8256', '2', '52', '2021-11-25'),
(432, '20', '3', '8256', '2', '52', '2021-11-25'),
(433, '13', '6', '2756', '12', '120', '2021-11-25'),
(434, '13', '6', '2756', '12', '120', '2021-11-25'),
(435, '12', '6', '8455', '1', '0', '2021-11-25'),
(436, '13', '6', '8455', '13', '130', '2021-11-25'),
(437, '13', '6', '8455', '1', '10', '2021-11-25'),
(438, '12', '3', '7273', '1', '0', '2021-11-25'),
(439, '12', '3', '7273', '3', '1650', '2021-11-25'),
(440, '12', '11', '9259', '1', '0', '2021-11-25'),
(441, '14', '11', '9259', '13', '65', '2021-11-25'),
(442, '13', '2', '3255', '12', '120', '2021-11-25'),
(443, '15', '2', '3255', '12', '240', '2021-11-25'),
(444, '12', '3', '8260', '2', '1100', '2021-11-25'),
(445, '14', '3', '8260', '2', '1100', '2021-11-25'),
(446, '13', '3', '6719', '1', '0', '2021-11-25'),
(447, '12', '7', '8788', '1', '0', '2021-11-25'),
(448, '13', '7', '8788', '500', '5000', '2021-11-25'),
(449, '12', '3', '1382', '2', '1100', '2021-11-25'),
(450, '12', '7', '8884', '19', '10450', '2021-11-25'),
(451, '12', '11', '3465', '1', '0', '2021-11-25'),
(452, '12', '3', '9183', '1', '0', '2021-11-25'),
(453, '12', '3', '9698', '1', '0', '2021-11-25'),
(454, '12', '3', '7302', '99', '54450', '2021-11-25'),
(455, '12', '3', '1871', '11', '6050', '2021-11-25'),
(456, '22', '3', '1871', '11', '6050', '2021-11-25'),
(457, '12', '3', '7720', '27', '14850', '2021-11-25'),
(458, '12', '11', '2157', '20', '11000', '2021-11-25'),
(459, '20', '11', '2157', '3', '78', '2021-11-25'),
(460, '12', '3', '3260', '9', '4950', '2021-11-25'),
(461, '12', '2', '2093', '90', '49500', '2021-11-25'),
(462, '12', '6', '2144', '1', '550', '2021-11-25'),
(463, '12', '2', '8160', '11', '6050', '2021-11-25'),
(464, '12', '11', '3525', '2', '1100', '2021-11-25'),
(465, '12', '3', '2666', '2', '1100', '2021-11-25'),
(466, '14', '7', '7746', '4', '20', '2021-11-25'),
(467, '12', '3', '7910', '10', '5500', '2021-12-04'),
(468, '20', '3', '7910', '2', '52', '2021-12-04'),
(469, '12', '6', '7654', '1', '550', '2021-12-19'),
(470, '12', '3', '3457', '2', '1100', '2021-12-19'),
(471, '12', '6', '2034', '0', '0', '2021-12-19'),
(472, '12', '6', '2034', '0', '0', '2021-12-19'),
(473, '12', '6', '2034', '299', '164450', '2021-12-19'),
(474, '12', '6', '3000', '9', '4950', '2021-12-19'),
(475, '12', '3', '3865', '1', '550', '2021-12-19'),
(476, '12', '6', '6574', '3', '1650', '2021-12-19'),
(477, '12', '3', '4854', '1', '550', '2021-12-22'),
(478, '12', '7', '8173', '28', '15400', '2021-12-22'),
(479, '12', '6', '9025', '2', '1100', '2021-12-22'),
(480, '12', '6', '2795', '26', '14300', '2021-12-22'),
(481, '12', '3', '4869', '65', '35750', '2021-12-22'),
(482, '12', '3', '4363', '26', '14300', '2021-12-22');

-- --------------------------------------------------------

--
-- Table structure for table `admin_register`
--

CREATE TABLE `admin_register` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_register`
--

INSERT INTO `admin_register` (`id`, `email`, `password`) VALUES
(2, '', 'riya123'),
(3, 'hetvi', 'pass');

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `id` int(11) NOT NULL,
  `pname` varchar(255) NOT NULL,
  `rate` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billing`
--

INSERT INTO `billing` (`id`, `pname`, `rate`) VALUES
(1, 'shampoo', 20);

-- --------------------------------------------------------

--
-- Table structure for table `cart_master`
--

CREATE TABLE `cart_master` (
  `id` int(11) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `invoice` varchar(255) NOT NULL,
  `totalamount` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart_master`
--

INSERT INTO `cart_master` (`id`, `user_id`, `invoice`, `totalamount`, `date`) VALUES
(71, '6', '8952', '4400', '2021-11-24'),
(72, '3', '5178', '10450', '2021-11-24'),
(73, '3', '2627', '4950', '2021-11-24'),
(74, '3', '7971', '1100', '2021-11-24'),
(75, '3', '4207', '120', '2021-11-24'),
(76, '3', '3538', '5000', '2021-11-24'),
(77, '6', '2190', '750', '2021-11-24'),
(78, '3', '7938', '2000', '2021-11-24'),
(79, '2', '6524', '5500', '2021-11-24'),
(80, '2', '6823', '44000', '2021-11-24'),
(81, '3', '4926', '49500', '2021-11-24'),
(82, '6', '7376', '100', '2021-11-24'),
(83, '11', '9963', '80', '2021-11-24'),
(84, '2', '3799', '45', '2021-11-24'),
(85, '3', '7876', '5000', '2021-11-24'),
(86, '2', '8731', '10450', '2021-11-24'),
(87, '2', '8731', '10450', '2021-11-24'),
(88, '3', '6035', '35', '2021-11-24'),
(89, '6', '4191', '700', '2021-11-24'),
(90, '3', '2501', '200', '2021-11-24'),
(91, '3', '2073', '600', '2021-11-24'),
(92, '6', '2496', '90', '2021-11-24'),
(93, '3', '8150', '11000', '2021-11-24'),
(94, '3', '9785', '60', '2021-11-24'),
(95, '6', '4042', '60', '2021-11-24'),
(96, '3', '8750', '156', '2021-11-24'),
(97, '2', '5773', '2600', '2021-11-24'),
(98, '3', '9530', '260', '2021-11-24'),
(99, '6', '5540', '234', '2021-11-24'),
(100, '7', '2070', '90', '2021-11-24'),
(101, '7', '2881', '120', '2021-11-24'),
(102, '3', '6757', '2640', '2021-11-25'),
(103, '3', '3550', '0', '2021-11-25'),
(104, '3', '1382', '1100', '2021-11-25'),
(105, '7', '8884', '10450', '2021-11-25'),
(106, '7', '8884', '10450', '2021-11-25'),
(107, '7', '8884', '10450', '2021-11-25'),
(108, '11', '3465', '0', '2021-11-25'),
(109, '3', '9183', '0', '2021-11-25'),
(110, '3', '9698', '0', '2021-11-25'),
(111, '3', '1871', '6050', '2021-11-25'),
(112, '3', '7720', '14850', '2021-11-25'),
(113, '11', '2157', '78', '2021-11-25'),
(114, '11', '2157', '78', '2021-11-25'),
(115, '3', '3260', '4950', '2021-11-25'),
(116, '2', '2093', '49500', '2021-11-25'),
(117, '6', '2144', '550', '2021-11-25'),
(118, '2', '8160', '6050', '2021-11-25'),
(119, '11', '3525', '1100', '2021-11-25'),
(120, '3', '2666', '1100', '2021-11-25'),
(121, '6', '7654', '550', '2021-12-19'),
(122, '3', '3457', '1100', '2021-12-19'),
(123, '2', '2841', '0', '2021-12-19'),
(124, '6', '2034', '0', '2021-12-19'),
(125, '6', '2034', '0', '2021-12-19'),
(126, '6', '2034', '0', '2021-12-19'),
(127, '6', '3000', '4950', '2021-12-19'),
(128, '3', '3865', '550', '2021-12-19'),
(129, '6', '6574', '1650', '2021-12-19'),
(130, '3', '4854', '550', '2021-12-22'),
(131, '7', '8173', '15400', '2021-12-22'),
(132, '6', '9025', '1100', '2021-12-22'),
(133, '6', '2795', '14300', '2021-12-22'),
(134, '6', '2795', '14300', '2021-12-22'),
(135, '3', '4869', '35750', '2021-12-22'),
(136, '3', '4363', '14300', '2021-12-22');

-- --------------------------------------------------------

--
-- Table structure for table `customer_info`
--

CREATE TABLE `customer_info` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_info`
--

INSERT INTO `customer_info` (`id`, `name`, `address`, `phone`, `age`, `email`, `gender`) VALUES
(2, 'hetvi', 'kahannagar society', 'null', 20, 'emailhetvi', 'Female'),
(3, 'Riya', '2,kahannagar society Talod', '88777545555', 36, 'hetvi@gmail.com', 'female'),
(6, 'jill', 'Gireraj society ', '56655555554', 19, 'hetviemail', 'Female'),
(7, 'vedant', 'Behind civil hospital', '9898526564', 20, 'vedant@gmail.com', 'male'),
(11, 'hetvi', 'kan', '698553322', 20, 'hetvi4448shah', 'Female');

-- --------------------------------------------------------

--
-- Table structure for table `product_master`
--

CREATE TABLE `product_master` (
  `id` int(11) NOT NULL,
  `cur_date` varchar(11) NOT NULL,
  `pname` varchar(255) NOT NULL,
  `pprice` int(11) NOT NULL,
  `ptitle` varchar(255) NOT NULL,
  `pquantity` int(11) NOT NULL,
  `pimage` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_master`
--

INSERT INTO `product_master` (`id`, `cur_date`, `pname`, `pprice`, `ptitle`, `pquantity`, `pimage`) VALUES
(12, '20210819', 'Sweeet', 550, 'Fruity Pebbles 300gm', 300, ''),
(13, '20210827', 'Biscuit', 10, 'parle-G', 87, ''),
(14, '20210828', 'AMUL', 5, 'SABAR BUtter Milk', 9, ''),
(15, '20210914', 'bottle', 20, 'bisler', 1, ''),
(20, '20210914', 'Breakfast', 26, 'Pasta(64g)', 1, ''),
(21, '20210914', 'Fast Food', 15, 'Maggie', 1, ''),
(22, '20210914', 'Juice', 15, 'Mango Fruti', 1, ''),
(23, '20210914', 'Shampoo', 12, 'Sunsilk (10g)', 1, ''),
(24, '20210914', ' Multipurpose Scissor', 17, '1668 Light Weight Multipurpose Scissor', 1, ''),
(25, '20210914', 'Reliance Digital\r\n', 1199, 'Reconnect RAWHB1001 Bluetooth Headphone', 1, ''),
(27, '20211125', 'vanilla cream', 80, 'cream', 30, ''),
(29, '20211125', 'Bata Sandal ', 499, 'Sandel', 100, '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addtocart`
--
ALTER TABLE `addtocart`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admin_register`
--
ALTER TABLE `admin_register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `billing`
--
ALTER TABLE `billing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cart_master`
--
ALTER TABLE `cart_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer_info`
--
ALTER TABLE `customer_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product_master`
--
ALTER TABLE `product_master`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addtocart`
--
ALTER TABLE `addtocart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=483;

--
-- AUTO_INCREMENT for table `admin_register`
--
ALTER TABLE `admin_register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `billing`
--
ALTER TABLE `billing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cart_master`
--
ALTER TABLE `cart_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=137;

--
-- AUTO_INCREMENT for table `customer_info`
--
ALTER TABLE `customer_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `product_master`
--
ALTER TABLE `product_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

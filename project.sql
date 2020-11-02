-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Feb 26, 2020 at 03:20 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(8) NOT NULL,
  `FullName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`, `FullName`) VALUES
('Saleh902', 'Sa1983@h', 'Saleh Saud'),
('sara99', 'sara', 'sara saleh');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type` varchar(20) NOT NULL,
  `category` varchar(20) NOT NULL,
  `price` double NOT NULL,
  `NO_item` int(11) NOT NULL,
  `pic` varchar(150) NOT NULL,
  `Description` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`, `type`, `category`, `price`, `NO_item`, `pic`, `Description`) VALUES
(1, 'Mortedella', 'Meats', 'Fresh', 12, 27, 'Chicken Mortedella Plain.png', 'Chicken Mortedella Plain'),
(2, 'Mandarin', 'FruitVegetables', 'Fresh', 4, 25, 'mandarin.png', 'Fresh Small and Sweet'),
(3, 'Akkawi Cheese', 'Diary', 'Fresh', 8, 9, 'Akkawi Cheese.png', 'Akkawi Cheese yummy!'),
(4, 'Butter', 'Diary', 'Fresh', 14, 25, 'butter.png', 'Unsalted Butter'),
(5, 'lays', 'Food1', 'FoodBeverages', 5, 15, 'chips.png', 'Salty and crispy'),
(6, 'Lamb', 'Meats', 'Fresh', 16, 20, 'sliced Lamb.png', 'Sliced Lamb'),
(7, 'chickpeas', 'Food1', 'FoodBeverages', 14, 30, 'chickPeas.png', 'Small and round'),
(8, 'Broccoli', 'FruitVegetables', 'Fresh', 7, 26, 'Broccoli.png', 'Fresh and healthy'),
(9, 'Italian Parmesan Cheese', 'Diary', 'Fresh', 16, 10, 'Italian Parmesan Cheese.png', 'For every meal'),
(10, 'FreshMilk', 'Diary', 'Fresh', 6, 16, 'Milk.png', 'Whole fat'),
(11, 'Lionbar', 'Food1', 'FoodBeverages', 5, 30, 'chocobar.png', 'Sweet and crunchy'),
(12, 'chickenBreastFillet', 'Meats', 'Fresh', 12, 28, 'chicken breast fillet.png', 'Easy to use'),
(13, 'Spinach', 'FruitVegetables', 'Fresh', 7, 29, 'SPINACH.png', 'Small and fresh leafs'),
(200, 'RanchDressing', 'Food1', 'FoodBeverages', 11, 26, 'RanchDressing.png', 'For every meal!!'),
(201, 'OatFlakes', 'Food2', 'OrganicFood', 21, 28, 'oatflakes.png', 'Organic Oat Flakes'),
(202, 'Carrots', 'Food2', 'OrganicFood', 11, 22, 'carrots.png', 'Mini organic carrots'),
(203, 'Water', 'Beverages', 'FoodBeverages', 10, 20, 'water.png', 'Pure and Clear'),
(204, 'Honey', 'Food1', 'FoodBeverages', 18, 26, 'honey.png', 'Black Wood Honey'),
(205, 'Fish', 'Meats', 'Fresh', 6, 25, 'FreshHamam.png', 'Fresh Hamam Fishes'),
(206, 'Strawberry', 'FruitVegetables', 'Fresh', 4, 20, 'strawberry.png', 'Large and Fresh'),
(207, 'Cereal', 'Food1', 'FoodBeverages', 18, 15, 'WheatCereal.png', 'Wheat Cereal for ever day breakfast'),
(208, 'Bread', 'Food1', 'FoodBeverages', 7, 24, 'WhiteSlicedBread.png', 'White sliced bread'),
(209, 'InstantCoffee', 'Food1', 'FoodBeverages', 24, 28, 'InstantCoffee.png', 'Instant Coffee roasted perfectly'),
(210, 'AlmondMilk', 'Drinks', 'OrganicFood', 24, 23, 'almondmilk.png', ''),
(211, 'Pepsi', 'Beverages', 'FoodBeverages', 8, 26, 'pepsi.png', ''),
(212, 'PeanutButter', 'Food1', 'FoodBeverages', 21, 27, 'PeanutButter.png', 'Smooth and Creamy'),
(213, 'Spaghetti', 'Food2', 'OrganicFood', 20, 29, 'WheatSpaghetti.png', 'Organic Wheat Spaghetti'),
(215, 'Tomatoes', 'Food2', 'OrganicFood', 6, 28, 'cherrytomato.png', 'Organic Cherry tomatoes'),
(216, 'OrangeJuice', 'Beverages', 'FoodBeverages', 12, 21, 'orangejuice.png', 'Fresh Orange juice'),
(218, 'CoconutOil', 'Food2', 'OrganicFood', 36, 26, 'coconutoil.png', 'Organic Coconut Oil'),
(219, 'OliveOil', 'Food2', 'OrganicFood', 18, 22, 'organicoliveoil.png', 'Organic Olive Oil'),
(220, 'pepperSouce', 'Food1', 'FoodBeverages', 17, 25, 'papperSauce.png', ' Spicy!!                            ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=221;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

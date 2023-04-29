-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2023 at 05:34 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `workshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `akses_masuk`
--

CREATE TABLE `akses_masuk` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `waktu_masuk` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `akses_masuk`
--

INSERT INTO `akses_masuk` (`id`, `id_user`, `waktu_masuk`) VALUES
(1, 4, '2023-04-28 11:28:53'),
(2, 1, '2023-04-27 11:28:53'),
(3, 4, '2023-04-29 22:27:28');

-- --------------------------------------------------------

--
-- Table structure for table `identitas`
--

CREATE TABLE `identitas` (
  `id_user` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `npm_nip` varchar(20) NOT NULL,
  `prodi` enum('RKS','RPK','RK') NOT NULL,
  `jk` enum('L','P') NOT NULL,
  `no_telp` varchar(12) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `role` enum('owner','admin','user') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `identitas`
--

INSERT INTO `identitas` (`id_user`, `nama`, `username`, `npm_nip`, `prodi`, `jk`, `no_telp`, `pass`, `role`) VALUES
(1, 'Adek Muhammad Zulkham R K', 'adekmzrk', '1918101469', 'RPK', 'P', '085648844927', '4993b2e58e43436bc2d347838b87772e', 'user'),
(4, 'Alviana Juni S', 'vivi', '1918101231', 'RKS', 'P', '085647788432', 'c3bb6f719742fd1e5768d6d1361cfb49', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `reservasi`
--

CREATE TABLE `reservasi` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `waktu` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reservasi`
--

INSERT INTO `reservasi` (`id`, `id_user`, `waktu`) VALUES
(1, 4, '2023-04-30 11:27:33'),
(2, 1, '2023-05-17 12:40:00'),
(3, 4, '2023-04-13 11:28:31'),
(5, 1, '2023-05-09 23:34:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `akses_masuk`
--
ALTER TABLE `akses_masuk`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `identitas`
--
ALTER TABLE `identitas`
  ADD PRIMARY KEY (`id_user`);

--
-- Indexes for table `reservasi`
--
ALTER TABLE `reservasi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `akses_masuk`
--
ALTER TABLE `akses_masuk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `identitas`
--
ALTER TABLE `identitas`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `reservasi`
--
ALTER TABLE `reservasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

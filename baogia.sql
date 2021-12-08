-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2021 at 11:42 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `baogia`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add product', 8, 'add_product'),
(30, 'Can change product', 8, 'change_product'),
(31, 'Can delete product', 8, 'delete_product'),
(32, 'Can view product', 8, 'view_product'),
(33, 'Can add volume', 9, 'add_volume'),
(34, 'Can change volume', 9, 'change_volume'),
(35, 'Can delete volume', 9, 'delete_volume'),
(36, 'Can view volume', 9, 'view_volume'),
(37, 'Can add material', 10, 'add_material'),
(38, 'Can change material', 10, 'change_material'),
(39, 'Can delete material', 10, 'delete_material'),
(40, 'Can view material', 10, 'view_material'),
(41, 'Can add announced', 11, 'add_announced'),
(42, 'Can change announced', 11, 'change_announced'),
(43, 'Can delete announced', 11, 'delete_announced'),
(44, 'Can view announced', 11, 'view_announced'),
(45, 'Can add fee shipping', 12, 'add_feeshipping'),
(46, 'Can change fee shipping', 12, 'change_feeshipping'),
(47, 'Can delete fee shipping', 12, 'delete_feeshipping'),
(48, 'Can view fee shipping', 12, 'view_feeshipping'),
(49, 'Can add packaging level1', 13, 'add_packaginglevel1'),
(50, 'Can change packaging level1', 13, 'change_packaginglevel1'),
(51, 'Can delete packaging level1', 13, 'delete_packaginglevel1'),
(52, 'Can view packaging level1', 13, 'view_packaginglevel1'),
(53, 'Can add packaging level2', 14, 'add_packaginglevel2'),
(54, 'Can change packaging level2', 14, 'change_packaginglevel2'),
(55, 'Can delete packaging level2', 14, 'delete_packaginglevel2'),
(56, 'Can view packaging level2', 14, 'view_packaginglevel2'),
(57, 'Can add packing worker', 15, 'add_packingworker'),
(58, 'Can change packing worker', 15, 'change_packingworker'),
(59, 'Can delete packing worker', 15, 'delete_packingworker'),
(60, 'Can view packing worker', 15, 'view_packingworker'),
(61, 'Can add stamp', 16, 'add_stamp'),
(62, 'Can change stamp', 16, 'change_stamp'),
(63, 'Can delete stamp', 16, 'delete_stamp'),
(64, 'Can view stamp', 16, 'view_stamp');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_vietnamese_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_vietnamese_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_vietnamese_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_vietnamese_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_vietnamese_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$9v5XlXsER4Ea9fzUbaYi7D$IH6F0tQoPwg3SeRcZtwWHHK0oWtBscrloZaKmVqA2QE=', '2021-12-02 01:49:06.474457', 1, 'songmv', '', '', 'songmv.oni@gmail.com', 1, 1, '2021-12-02 01:48:14.556531');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_vietnamese_ci DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8_vietnamese_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-12-02 01:50:17.019864', '1', 'Gia công Serume', 1, '[{\"added\": {}}]', 7, 1),
(2, '2021-12-02 01:50:33.890104', '2', 'Gia công Cream', 1, '[{\"added\": {}}]', 7, 1),
(3, '2021-12-02 01:51:25.784510', '3', 'Dầu gội dầu xả', 1, '[{\"added\": {}}]', 7, 1),
(4, '2021-12-02 01:51:35.908115', '4', 'Mặt nạ', 1, '[{\"added\": {}}]', 7, 1),
(5, '2021-12-02 01:51:49.683160', '5', 'Sữa rửa mặt', 1, '[{\"added\": {}}]', 7, 1),
(6, '2021-12-02 01:51:57.927614', '6', 'Son môi', 1, '[{\"added\": {}}]', 7, 1),
(7, '2021-12-02 01:52:06.429912', '7', 'Tạo kiểu tóc', 1, '[{\"added\": {}}]', 7, 1),
(8, '2021-12-02 01:52:16.896139', '8', 'Remover', 1, '[{\"added\": {}}]', 7, 1),
(9, '2021-12-02 01:52:36.267301', '9', 'Bộ Makupe trang điểm', 1, '[{\"added\": {}}]', 7, 1),
(10, '2021-12-02 01:52:51.046077', '10', 'Lotion, toner', 1, '[{\"added\": {}}]', 7, 1),
(11, '2021-12-02 01:53:03.112109', '11', 'Sản phẩm tẩy rửa', 1, '[{\"added\": {}}]', 7, 1),
(12, '2021-12-02 01:53:18.175064', '3', 'Dầu gội, dầu xả', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean danh m\\u1ee5c\"]}}]', 7, 1),
(13, '2021-12-02 01:53:58.335912', '9', 'Bộ Makupe trang điểm', 2, '[{\"changed\": {\"fields\": [\"URL\"]}}]', 7, 1),
(14, '2021-12-02 03:01:10.719147', '1', 'Serum trị mụn', 1, '[{\"added\": {}}]', 8, 1),
(15, '2021-12-02 03:07:39.661957', '1', 'Serum trị mụn', 2, '[{\"changed\": {\"fields\": [\"URL\"]}}]', 8, 1),
(16, '2021-12-02 03:08:23.231376', '2', 'Cream chống nắng', 1, '[{\"added\": {}}]', 8, 1),
(17, '2021-12-02 03:44:51.142020', '3', 'Cream trị thâm mụn', 1, '[{\"added\": {}}]', 8, 1),
(18, '2021-12-02 03:59:41.602267', '1', '30ml', 1, '[{\"added\": {}}]', 9, 1),
(19, '2021-12-02 03:59:51.169950', '2', '50ml', 1, '[{\"added\": {}}]', 9, 1),
(20, '2021-12-02 04:00:02.480246', '3', '100ml', 1, '[{\"added\": {}}]', 9, 1),
(21, '2021-12-02 04:00:14.249271', '4', '30ml', 1, '[{\"added\": {}}]', 9, 1),
(22, '2021-12-02 04:00:21.640907', '5', '50ml', 1, '[{\"added\": {}}]', 9, 1),
(23, '2021-12-02 04:00:28.425030', '6', '100ml', 1, '[{\"added\": {}}]', 9, 1),
(24, '2021-12-02 04:00:36.708732', '7', '30ml', 1, '[{\"added\": {}}]', 9, 1),
(25, '2021-12-02 04:00:42.726080', '8', '50ml', 1, '[{\"added\": {}}]', 9, 1),
(26, '2021-12-02 04:00:53.240930', '9', '100ml', 1, '[{\"added\": {}}]', 9, 1),
(27, '2021-12-03 02:46:08.189427', '1', 'Loại A', 1, '[{\"added\": {}}]', 10, 1),
(28, '2021-12-03 02:46:24.570288', '2', 'Loại B', 1, '[{\"added\": {}}]', 10, 1),
(29, '2021-12-03 02:50:14.777278', '1', 'Serum trị mụn 30ml', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean dung t\\u00edch\"]}}]', 9, 1),
(30, '2021-12-03 02:50:28.446353', '2', 'Serum trị mụn 50ml', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean dung t\\u00edch\"]}}]', 9, 1),
(31, '2021-12-03 02:50:40.925239', '3', 'Serum trị mụn 100ml', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean dung t\\u00edch\"]}}]', 9, 1),
(32, '2021-12-03 02:50:52.523731', '4', 'Cream chống nắng 30ml', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean dung t\\u00edch\"]}}]', 9, 1),
(33, '2021-12-03 02:51:05.070009', '5', 'Cream chống nắng 50ml', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean dung t\\u00edch\"]}}]', 9, 1),
(34, '2021-12-03 02:51:17.212280', '6', 'Cream chống nắng 100ml', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean dung t\\u00edch\"]}}]', 9, 1),
(35, '2021-12-03 02:51:28.850465', '7', 'Cream trị thâm mụn 30ml', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean dung t\\u00edch\"]}}]', 9, 1),
(36, '2021-12-03 02:51:39.219501', '8', 'Cream trị thâm mụn 50ml', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean dung t\\u00edch\"]}}]', 9, 1),
(37, '2021-12-03 02:51:50.183068', '9', 'Cream trị thâm mụn 100ml', 2, '[{\"changed\": {\"fields\": [\"T\\u00ean dung t\\u00edch\"]}}]', 9, 1),
(38, '2021-12-03 02:52:16.449771', '1', 'Loại A', 2, '[{\"changed\": {\"fields\": [\"Dung t\\u00edch\"]}}]', 10, 1),
(39, '2021-12-03 02:52:26.964068', '2', 'Loại B', 2, '[{\"changed\": {\"fields\": [\"Dung t\\u00edch\"]}}]', 10, 1),
(40, '2021-12-03 02:52:51.851642', '3', 'Loại A', 1, '[{\"added\": {}}]', 10, 1),
(41, '2021-12-03 02:53:02.364847', '3', 'Loại A', 2, '[{\"changed\": {\"fields\": [\"Gi\\u00e1 nguy\\u00ean li\\u1ec7u\"]}}]', 10, 1),
(42, '2021-12-03 02:53:17.724312', '4', 'Loại B', 1, '[{\"added\": {}}]', 10, 1),
(43, '2021-12-03 03:05:55.005797', '1', 'Loại A', 2, '[{\"changed\": {\"fields\": [\"Ghi ch\\u00fa\"]}}]', 10, 1),
(44, '2021-12-03 03:06:02.966554', '2', 'Loại B', 2, '[{\"changed\": {\"fields\": [\"Ghi ch\\u00fa\"]}}]', 10, 1),
(45, '2021-12-03 03:06:09.925058', '3', 'Loại A', 2, '[{\"changed\": {\"fields\": [\"Ghi ch\\u00fa\"]}}]', 10, 1),
(46, '2021-12-03 03:06:27.285753', '4', 'Loại B', 2, '[{\"changed\": {\"fields\": [\"Ghi ch\\u00fa\"]}}]', 10, 1),
(47, '2021-12-03 08:04:36.363766', '1', 'Bao bì cream trị thâm mụn', 1, '[{\"added\": {}}]', 13, 1),
(48, '2021-12-03 08:06:53.855406', '2', 'Bao bì cream trị thâm mụn 01', 1, '[{\"added\": {}}]', 13, 1),
(49, '2021-12-03 09:20:50.511406', '1', 'Bao bì c2 Cream trị thâm mụn 01', 1, '[{\"added\": {}}]', 14, 1),
(50, '2021-12-03 09:21:29.463255', '2', 'Bao bì c2 Cream trị thâm mụn 02', 1, '[{\"added\": {}}]', 14, 1),
(51, '2021-12-03 09:23:05.820476', '1', 'Bao bì c2 Cream trị thâm mụn 01', 2, '[{\"changed\": {\"fields\": [\"Dung t\\u00edch\"]}}]', 14, 1),
(52, '2021-12-03 10:08:50.026030', '1', 'Gói tem nhãn Cream  trị thâm mụn 01', 1, '[{\"added\": {}}]', 16, 1),
(53, '2021-12-03 10:09:31.350981', '2', 'Gói tem nhãn Cream  trị thâm mụn 02', 1, '[{\"added\": {}}]', 16, 1),
(54, '2021-12-03 10:10:08.640493', '1', 'Gói tem nhãn Cream  trị thâm mụn 01', 2, '[{\"changed\": {\"fields\": [\"Dung t\\u00edch\"]}}]', 16, 1),
(55, '2021-12-04 07:17:18.156961', '1', 'Gói nhân công đóng gói 01', 1, '[{\"added\": {}}]', 15, 1),
(56, '2021-12-04 07:17:45.675670', '2', 'Gói nhân công đóng gói 02', 1, '[{\"added\": {}}]', 15, 1),
(57, '2021-12-04 07:24:33.582558', '1', 'Gói công bố 01', 1, '[{\"added\": {}}]', 11, 1),
(58, '2021-12-04 07:24:53.901296', '2', 'Gói công bố 02', 1, '[{\"added\": {}}]', 11, 1),
(59, '2021-12-04 07:28:38.091028', '2', 'Gói công bố 02', 2, '[{\"changed\": {\"fields\": [\"Dung t\\u00edch\"]}}]', 11, 1),
(60, '2021-12-04 07:39:59.014354', '1', 'Gói vận chuyển nội thành', 1, '[{\"added\": {}}]', 12, 1),
(61, '2021-12-04 07:40:20.814433', '2', 'Gói vận chuyển ngoại thành', 1, '[{\"added\": {}}]', 12, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(11, 'quote', 'announced'),
(7, 'quote', 'category'),
(12, 'quote', 'feeshipping'),
(10, 'quote', 'material'),
(13, 'quote', 'packaginglevel1'),
(14, 'quote', 'packaginglevel2'),
(15, 'quote', 'packingworker'),
(8, 'quote', 'product'),
(16, 'quote', 'stamp'),
(9, 'quote', 'volume'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-12-01 10:31:29.155053'),
(2, 'auth', '0001_initial', '2021-12-01 10:31:29.607813'),
(3, 'admin', '0001_initial', '2021-12-01 10:31:29.728613'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-12-01 10:31:29.740441'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-12-01 10:31:29.755261'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-12-01 10:31:29.827268'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-12-01 10:31:29.893706'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-12-01 10:31:29.947165'),
(9, 'auth', '0004_alter_user_username_opts', '2021-12-01 10:31:29.956437'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-12-01 10:31:30.001911'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-12-01 10:31:30.005973'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-12-01 10:31:30.014919'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-12-01 10:31:30.033549'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-12-01 10:31:30.052488'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-12-01 10:31:30.108395'),
(16, 'auth', '0011_update_proxy_permissions', '2021-12-01 10:31:30.117884'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-12-01 10:31:30.135838'),
(18, 'quote', '0001_initial', '2021-12-01 10:31:30.758921'),
(19, 'quote', '0002_auto_20211201_1530', '2021-12-01 10:31:31.805305'),
(20, 'sessions', '0001_initial', '2021-12-01 10:31:31.864897'),
(21, 'quote', '0003_auto_20211201_2125', '2021-12-02 01:48:46.274250'),
(22, 'quote', '0004_auto_20211201_2130', '2021-12-02 01:48:46.353279'),
(23, 'quote', '0005_alter_category_slug', '2021-12-02 01:48:46.420947'),
(24, 'quote', '0006_auto_20211202_0956', '2021-12-02 02:56:44.100642'),
(25, 'quote', '0007_alter_product_slug', '2021-12-02 03:00:26.195676'),
(26, 'quote', '0008_material_note', '2021-12-03 03:01:58.149542');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_vietnamese_ci NOT NULL,
  `session_data` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('bs30m5fl8xqjfq88o7dqqht3aq3ucj4r', '.eJxVjDsOwjAQBe_iGlmJ40-Wkp4zWLveNQ4gR4qTCnF3iJQC2jcz76UibmuJW5MlTqzOqlen340wPaTugO9Yb7NOc12XifSu6IM2fZ1ZnpfD_Tso2Mq3Dh546ILkMED2I5JID5Y9GusscRodAlBwzhAEdBYBbXKewJss0hn1_gDkIDf0:1msbDe:BoQfvwezm-Ypn78uymColBTufAHAB8wqs1YZEfv8t4w', '2021-12-16 01:49:06.478538');

-- --------------------------------------------------------

--
-- Table structure for table `quote_announced`
--

CREATE TABLE `quote_announced` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `price` double NOT NULL,
  `note` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `create_at` date NOT NULL,
  `update_at` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `volume_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_announced`
--

INSERT INTO `quote_announced` (`id`, `name`, `price`, `note`, `create_at`, `update_at`, `status`, `product_id`, `volume_id`) VALUES
(1, 'Gói công bố 01', 200000, 'Ghi chú tạm thời', '2021-12-04', '2021-12-04', 1, 3, 7),
(2, 'Gói công bố 02', 1000000, 'Ghi chú tạm thời', '2021-12-04', '2021-12-04', 1, 3, 7);

-- --------------------------------------------------------

--
-- Table structure for table `quote_category`
--

CREATE TABLE `quote_category` (
  `create_at` date NOT NULL,
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `slug` varchar(500) COLLATE utf8_vietnamese_ci NOT NULL,
  `update_at` date NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_category`
--

INSERT INTO `quote_category` (`create_at`, `id`, `name`, `slug`, `update_at`, `status`) VALUES
('2021-12-02', 1, 'Gia công Serume', 'gia-cong-serume', '2021-12-02', 1),
('2021-12-02', 2, 'Gia công Cream', 'gia-cong-cream', '2021-12-02', 1),
('2021-12-02', 3, 'Dầu gội, dầu xả', 'dau-goi-dau-xa-3', '2021-12-02', 1),
('2021-12-02', 4, 'Mặt nạ', 'mat-na', '2021-12-02', 1),
('2021-12-02', 5, 'Sữa rửa mặt', 'sua-rua-mat', '2021-12-02', 1),
('2021-12-02', 6, 'Son môi', 'son-moi', '2021-12-02', 1),
('2021-12-02', 7, 'Tạo kiểu tóc', 'tao-kieu-toc', '2021-12-02', 1),
('2021-12-02', 8, 'Remover', 'remover', '2021-12-02', 1),
('2021-12-02', 9, 'Bộ Makupe trang điểm', 'bo-makupe-trang-iem-9', '2021-12-02', 1),
('2021-12-02', 10, 'Lotion, toner', 'lotion-toner', '2021-12-02', 1),
('2021-12-02', 11, 'Sản phẩm tẩy rửa', 'san-pham-tay-rua', '2021-12-02', 1);

-- --------------------------------------------------------

--
-- Table structure for table `quote_feeshipping`
--

CREATE TABLE `quote_feeshipping` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `price` double NOT NULL,
  `note` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `create_at` date NOT NULL,
  `update_at` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `volume_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_feeshipping`
--

INSERT INTO `quote_feeshipping` (`id`, `name`, `price`, `note`, `create_at`, `update_at`, `status`, `product_id`, `volume_id`) VALUES
(1, 'Gói vận chuyển nội thành', 150000, 'Ghi chú tạm thời', '2021-12-04', '2021-12-04', 1, 3, 7),
(2, 'Gói vận chuyển ngoại thành', 500000, 'Ghi chú tạm thời', '2021-12-04', '2021-12-04', 1, 3, 7);

-- --------------------------------------------------------

--
-- Table structure for table `quote_material`
--

CREATE TABLE `quote_material` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `price` double NOT NULL,
  `status` tinyint(1) NOT NULL,
  `create_at` date NOT NULL,
  `update_at` date NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `volume_id` bigint(20) NOT NULL,
  `note` longtext COLLATE utf8_vietnamese_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_material`
--

INSERT INTO `quote_material` (`id`, `name`, `price`, `status`, `create_at`, `update_at`, `product_id`, `volume_id`, `note`) VALUES
(1, 'Loại A', 15000, 1, '2021-12-03', '2021-12-03', 3, 7, 'Không có gì'),
(2, 'Loại B', 1200, 1, '2021-12-03', '2021-12-03', 3, 7, 'Không có gì'),
(3, 'Loại A', 5000, 1, '2021-12-03', '2021-12-03', 3, 8, 'Không có gì'),
(4, 'Loại B', 4500, 1, '2021-12-03', '2021-12-03', 3, 8, 'Không có gì');

-- --------------------------------------------------------

--
-- Table structure for table `quote_packaginglevel1`
--

CREATE TABLE `quote_packaginglevel1` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `type_packaging` varchar(50) COLLATE utf8_vietnamese_ci NOT NULL,
  `image` varchar(512) COLLATE utf8_vietnamese_ci NOT NULL,
  `type_material` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `quantity_provider_sell` int(11) NOT NULL,
  `min_order` int(11) NOT NULL,
  `provider` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `price` double NOT NULL,
  `quantity_can_order_with_price` int(11) NOT NULL,
  `time_to_send` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `note` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `volume_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_packaginglevel1`
--

INSERT INTO `quote_packaginglevel1` (`id`, `name`, `type_packaging`, `image`, `type_material`, `quantity_provider_sell`, `min_order`, `provider`, `price`, `quantity_can_order_with_price`, `time_to_send`, `note`, `create_at`, `update_at`, `status`, `product_id`, `volume_id`) VALUES
(1, 'Bao bì cream trị thâm mụn', 'Hộp', 'media/upload/images/2021/12/in-vo-hop-giay-gia-re.jpg', 'PET', 10000, 1000, 'Thái Hương', 10000, 1000, 'Hàng sẵn kho giao hàng trong khoảng thời gian 2-3 ngày\r\nHàng đợi sản xuất time tầm 5-7 ngày tùy thuộc vào số lượng', 'Không có ghi chú gì', '2021-12-03 08:04:36.360884', '2021-12-03 08:04:36.360884', 1, 3, 7),
(2, 'Bao bì cream trị thâm mụn 01', 'Hộp', 'media/upload/images/2021/12/mau-bao-bi-giay-1.jpg', 'HDPE', 10000, 1000, 'Công ty VISS', 10000, 1000, 'Tùy từng thời điểm, do dịch Covid nên thời gian không thể chắc chắn', 'Ở đây chúng tôi không ghi chú', '2021-12-03 08:06:53.854378', '2021-12-03 08:06:53.854378', 1, 3, 7);

-- --------------------------------------------------------

--
-- Table structure for table `quote_packaginglevel2`
--

CREATE TABLE `quote_packaginglevel2` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `price` double NOT NULL,
  `type_packaging` varchar(50) COLLATE utf8_vietnamese_ci NOT NULL,
  `note` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `create_at` date NOT NULL,
  `update_at` date NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `volume_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_packaginglevel2`
--

INSERT INTO `quote_packaginglevel2` (`id`, `name`, `price`, `type_packaging`, `note`, `status`, `create_at`, `update_at`, `product_id`, `volume_id`) VALUES
(1, 'Bao bì c2 Cream trị thâm mụn 01', 5000, 'Hộp', 'Đây là ghi chú chúng tôi tạo ra để làm ví dụ', 1, '2021-12-03', '2021-12-03', 3, 7),
(2, 'Bao bì c2 Cream trị thâm mụn 02', 7000, 'Hộp', 'Cái này chỉ là ghi chú tạm thời có thể sửa được', 1, '2021-12-03', '2021-12-03', 3, 7);

-- --------------------------------------------------------

--
-- Table structure for table `quote_packingworker`
--

CREATE TABLE `quote_packingworker` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `price` double NOT NULL,
  `note` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `create_at` date NOT NULL,
  `update_at` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `volume_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_packingworker`
--

INSERT INTO `quote_packingworker` (`id`, `name`, `price`, `note`, `create_at`, `update_at`, `status`, `product_id`, `volume_id`) VALUES
(1, 'Gói nhân công đóng gói 01', 500000, 'Ghi chú tạm thời', '2021-12-04', '2021-12-04', 1, 3, 7),
(2, 'Gói nhân công đóng gói 02', 60000, 'Ghi chú tạm thời', '2021-12-04', '2021-12-04', 1, 3, 7);

-- --------------------------------------------------------

--
-- Table structure for table `quote_product`
--

CREATE TABLE `quote_product` (
  `create_at` datetime(6) NOT NULL,
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `unique_product` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `slug` varchar(500) COLLATE utf8_vietnamese_ci NOT NULL,
  `price` double NOT NULL,
  `quantity` int(11) NOT NULL,
  `update_at` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `cover_image` varchar(512) COLLATE utf8_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_product`
--

INSERT INTO `quote_product` (`create_at`, `id`, `name`, `unique_product`, `slug`, `price`, `quantity`, `update_at`, `status`, `category_id`, `cover_image`) VALUES
('2021-12-02 03:00:39.000000', 1, 'Serum trị mụn', 'P50B9A5V', 'serum-tri-mun', 50000, 5000, '2021-12-02 03:07:39.657964', 1, 1, 'media/upload/products/2021/12/linh_huong.jpg'),
('2021-12-02 03:07:44.000000', 2, 'Cream chống nắng', 'P25BBCFV', 'cream-chong-nang', 60000, 5000, '2021-12-02 03:08:23.230249', 1, 2, 'media/upload/products/2021/12/Main-asus-A556U-i5-6200-Đổi-main.png'),
('2021-12-02 03:44:06.000000', 3, 'Cream trị thâm mụn', 'P46F9F9V', 'cream-tri-tham-mun', 5000, 6000, '2021-12-02 03:44:51.139675', 1, 2, 'media/upload/products/2021/12/174713711_288449169604705_6242996822541452532_n.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `quote_stamp`
--

CREATE TABLE `quote_stamp` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `type_stamp` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `price` double NOT NULL,
  `note` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `create_at` date NOT NULL,
  `update_at` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `volume_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_stamp`
--

INSERT INTO `quote_stamp` (`id`, `name`, `type_stamp`, `price`, `note`, `create_at`, `update_at`, `status`, `product_id`, `volume_id`) VALUES
(1, 'Gói tem nhãn Cream  trị thâm mụn 01', 'Hộp', 1500, 'Cái này là dữ liệu demo cho ghi chú', '2021-12-03', '2021-12-03', 1, 3, 7),
(2, 'Gói tem nhãn Cream  trị thâm mụn 02', 'Hộp', 2000, 'Cái này lại là text ví dụ chèn vào ghi chú', '2021-12-03', '2021-12-03', 1, 3, 7);

-- --------------------------------------------------------

--
-- Table structure for table `quote_volume`
--

CREATE TABLE `quote_volume` (
  `id` bigint(20) NOT NULL,
  `name` varchar(50) COLLATE utf8_vietnamese_ci NOT NULL,
  `unique_volume` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `create_at` date NOT NULL,
  `update_at` date NOT NULL,
  `product_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Dumping data for table `quote_volume`
--

INSERT INTO `quote_volume` (`id`, `name`, `unique_volume`, `status`, `create_at`, `update_at`, `product_id`) VALUES
(1, 'Serum trị mụn 30ml', 'VEFF7F7P', 1, '2021-12-02', '2021-12-03', 1),
(2, 'Serum trị mụn 50ml', 'VFA7851P', 1, '2021-12-02', '2021-12-03', 1),
(3, 'Serum trị mụn 100ml', 'V923031P', 1, '2021-12-02', '2021-12-03', 1),
(4, 'Cream chống nắng 30ml', 'V2D176CP', 1, '2021-12-02', '2021-12-03', 2),
(5, 'Cream chống nắng 50ml', 'V362CCEP', 1, '2021-12-02', '2021-12-03', 2),
(6, 'Cream chống nắng 100ml', 'VEB2368P', 1, '2021-12-02', '2021-12-03', 2),
(7, 'Cream trị thâm mụn 30ml', 'VA4C0C2P', 1, '2021-12-02', '2021-12-03', 3),
(8, 'Cream trị thâm mụn 50ml', 'V588D20P', 1, '2021-12-02', '2021-12-03', 3),
(9, 'Cream trị thâm mụn 100ml', 'VD59E87P', 1, '2021-12-02', '2021-12-03', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `quote_announced`
--
ALTER TABLE `quote_announced`
  ADD PRIMARY KEY (`id`),
  ADD KEY `quote_announced_product_id_83a9950b_fk_quote_product_id` (`product_id`),
  ADD KEY `quote_announced_volume_id_4b4741c7_fk_quote_volume_id` (`volume_id`);

--
-- Indexes for table `quote_category`
--
ALTER TABLE `quote_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `quote_category_slug_b64e8fa8_uniq` (`slug`);

--
-- Indexes for table `quote_feeshipping`
--
ALTER TABLE `quote_feeshipping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `quote_feeshipping_product_id_011e7a3d_fk_quote_product_id` (`product_id`),
  ADD KEY `quote_feeshipping_volume_id_27cddb4d_fk_quote_volume_id` (`volume_id`);

--
-- Indexes for table `quote_material`
--
ALTER TABLE `quote_material`
  ADD PRIMARY KEY (`id`),
  ADD KEY `quote_material_product_id_52b8ca4e_fk_quote_product_id` (`product_id`),
  ADD KEY `quote_material_volume_id_dc894a2f_fk_quote_volume_id` (`volume_id`);

--
-- Indexes for table `quote_packaginglevel1`
--
ALTER TABLE `quote_packaginglevel1`
  ADD PRIMARY KEY (`id`),
  ADD KEY `quote_packaginglevel1_product_id_6072a601_fk_quote_product_id` (`product_id`),
  ADD KEY `quote_packaginglevel1_volume_id_3cafd9c2_fk_quote_volume_id` (`volume_id`);

--
-- Indexes for table `quote_packaginglevel2`
--
ALTER TABLE `quote_packaginglevel2`
  ADD PRIMARY KEY (`id`),
  ADD KEY `quote_packaginglevel2_product_id_2564ef27_fk_quote_product_id` (`product_id`),
  ADD KEY `quote_packaginglevel2_volume_id_92fe90a7_fk_quote_volume_id` (`volume_id`);

--
-- Indexes for table `quote_packingworker`
--
ALTER TABLE `quote_packingworker`
  ADD PRIMARY KEY (`id`),
  ADD KEY `quote_packingworker_product_id_89ba381a_fk_quote_product_id` (`product_id`),
  ADD KEY `quote_packingworker_volume_id_9ce346b5_fk_quote_volume_id` (`volume_id`);

--
-- Indexes for table `quote_product`
--
ALTER TABLE `quote_product`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `quote_product_unique_product_9d0f26de_uniq` (`unique_product`),
  ADD UNIQUE KEY `quote_product_slug_2c9f63b6_uniq` (`slug`),
  ADD KEY `quote_product_category_id_9c86eb94_fk_quote_category_id` (`category_id`);

--
-- Indexes for table `quote_stamp`
--
ALTER TABLE `quote_stamp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `quote_stamp_product_id_dcb04ab8_fk_quote_product_id` (`product_id`),
  ADD KEY `quote_stamp_volume_id_c2ee0398_fk_quote_volume_id` (`volume_id`);

--
-- Indexes for table `quote_volume`
--
ALTER TABLE `quote_volume`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `quote_volume_unique_volume_22496788_uniq` (`unique_volume`),
  ADD KEY `quote_volume_product_id_3ae00c47_fk_quote_product_id` (`product_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `quote_announced`
--
ALTER TABLE `quote_announced`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `quote_category`
--
ALTER TABLE `quote_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `quote_feeshipping`
--
ALTER TABLE `quote_feeshipping`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `quote_material`
--
ALTER TABLE `quote_material`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `quote_packaginglevel1`
--
ALTER TABLE `quote_packaginglevel1`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `quote_packaginglevel2`
--
ALTER TABLE `quote_packaginglevel2`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `quote_packingworker`
--
ALTER TABLE `quote_packingworker`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `quote_product`
--
ALTER TABLE `quote_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `quote_stamp`
--
ALTER TABLE `quote_stamp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `quote_volume`
--
ALTER TABLE `quote_volume`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `quote_announced`
--
ALTER TABLE `quote_announced`
  ADD CONSTRAINT `quote_announced_product_id_83a9950b_fk_quote_product_id` FOREIGN KEY (`product_id`) REFERENCES `quote_product` (`id`),
  ADD CONSTRAINT `quote_announced_volume_id_4b4741c7_fk_quote_volume_id` FOREIGN KEY (`volume_id`) REFERENCES `quote_volume` (`id`);

--
-- Constraints for table `quote_feeshipping`
--
ALTER TABLE `quote_feeshipping`
  ADD CONSTRAINT `quote_feeshipping_product_id_011e7a3d_fk_quote_product_id` FOREIGN KEY (`product_id`) REFERENCES `quote_product` (`id`),
  ADD CONSTRAINT `quote_feeshipping_volume_id_27cddb4d_fk_quote_volume_id` FOREIGN KEY (`volume_id`) REFERENCES `quote_volume` (`id`);

--
-- Constraints for table `quote_material`
--
ALTER TABLE `quote_material`
  ADD CONSTRAINT `quote_material_product_id_52b8ca4e_fk_quote_product_id` FOREIGN KEY (`product_id`) REFERENCES `quote_product` (`id`),
  ADD CONSTRAINT `quote_material_volume_id_dc894a2f_fk_quote_volume_id` FOREIGN KEY (`volume_id`) REFERENCES `quote_volume` (`id`);

--
-- Constraints for table `quote_packaginglevel1`
--
ALTER TABLE `quote_packaginglevel1`
  ADD CONSTRAINT `quote_packaginglevel1_product_id_6072a601_fk_quote_product_id` FOREIGN KEY (`product_id`) REFERENCES `quote_product` (`id`),
  ADD CONSTRAINT `quote_packaginglevel1_volume_id_3cafd9c2_fk_quote_volume_id` FOREIGN KEY (`volume_id`) REFERENCES `quote_volume` (`id`);

--
-- Constraints for table `quote_packaginglevel2`
--
ALTER TABLE `quote_packaginglevel2`
  ADD CONSTRAINT `quote_packaginglevel2_product_id_2564ef27_fk_quote_product_id` FOREIGN KEY (`product_id`) REFERENCES `quote_product` (`id`),
  ADD CONSTRAINT `quote_packaginglevel2_volume_id_92fe90a7_fk_quote_volume_id` FOREIGN KEY (`volume_id`) REFERENCES `quote_volume` (`id`);

--
-- Constraints for table `quote_packingworker`
--
ALTER TABLE `quote_packingworker`
  ADD CONSTRAINT `quote_packingworker_product_id_89ba381a_fk_quote_product_id` FOREIGN KEY (`product_id`) REFERENCES `quote_product` (`id`),
  ADD CONSTRAINT `quote_packingworker_volume_id_9ce346b5_fk_quote_volume_id` FOREIGN KEY (`volume_id`) REFERENCES `quote_volume` (`id`);

--
-- Constraints for table `quote_product`
--
ALTER TABLE `quote_product`
  ADD CONSTRAINT `quote_product_category_id_9c86eb94_fk_quote_category_id` FOREIGN KEY (`category_id`) REFERENCES `quote_category` (`id`);

--
-- Constraints for table `quote_stamp`
--
ALTER TABLE `quote_stamp`
  ADD CONSTRAINT `quote_stamp_product_id_dcb04ab8_fk_quote_product_id` FOREIGN KEY (`product_id`) REFERENCES `quote_product` (`id`),
  ADD CONSTRAINT `quote_stamp_volume_id_c2ee0398_fk_quote_volume_id` FOREIGN KEY (`volume_id`) REFERENCES `quote_volume` (`id`);

--
-- Constraints for table `quote_volume`
--
ALTER TABLE `quote_volume`
  ADD CONSTRAINT `quote_volume_product_id_3ae00c47_fk_quote_product_id` FOREIGN KEY (`product_id`) REFERENCES `quote_product` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

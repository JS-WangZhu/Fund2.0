/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : localhost:3306
 Source Schema         : fund

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : 65001

 Date: 27/12/2020 18:04:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for favor
-- ----------------------------
DROP TABLE IF EXISTS `favor`;
CREATE TABLE `favor`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `favorid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `user` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 31 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of favor
-- ----------------------------
INSERT INTO `favor` VALUES (1, '005827', 'wz', '易方达蓝筹精选混合');
INSERT INTO `favor` VALUES (2, '000118', 'wz', '广发聚鑫债券A');
INSERT INTO `favor` VALUES (3, '003984', 'wz', '嘉实新能源新材料股票A');
INSERT INTO `favor` VALUES (4, '003095', 'wz', '中欧医疗健康混合A');
INSERT INTO `favor` VALUES (5, '161725', 'wz', '招商中证白酒指数分级');
INSERT INTO `favor` VALUES (6, '009319', 'wz', '南方成长先锋混合C');
INSERT INTO `favor` VALUES (7, '000118', 'wzl', '广发聚鑫债券A(');
INSERT INTO `favor` VALUES (8, '320007', 'wzl', '诺安成长混合');
INSERT INTO `favor` VALUES (9, '161726', 'wzl', '招商国证生物医药指数分级');
INSERT INTO `favor` VALUES (10, '161725', 'wzl', '招商中证白酒指数分级');
INSERT INTO `favor` VALUES (11, '008087', 'wzl', '华夏中证5G通信主题ETF联接C');
INSERT INTO `favor` VALUES (12, '002611', 'wzl', '博时黄金ETF联接C');
INSERT INTO `favor` VALUES (13, '001630', 'wzl', '天弘中证计算机ETF联接C');
INSERT INTO `favor` VALUES (14, '110035', 'wzl', '易方达双债增强债券A');

SET FOREIGN_KEY_CHECKS = 1;

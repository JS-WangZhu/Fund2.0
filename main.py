
# 主程序入口
from getInfo import getGegu, getJijin
from readTxt import GetData
from colorama import init, Fore, Back, Style
import prettytable as pt
import time
import platform
import os

# 定义颜色类
init(autoreset=False)
class Colored(object):
    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.LIGHTRED_EX + s + Fore.RESET
    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET
    def yellow(self, s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET
    def white(self,s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET
    def blue(self,s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET

if __name__ == '__main__':
    while True:
        d = GetData()
        # 大盘
        # 判断大盘红绿
        def compareDapanNum(s1, s2):
            color = Colored()
            if float(str(s1)[:-1]) > 0.00:
                return color.red('+' + s1), color.red(s2)
            elif float(str(s1)[:-1]) < 0.00:
                return color.green(s1), color.green(s2)
            else:
                return color.white(s1), color.white(s2)
    #     ggc = d.getGgCode()
        shangz_jg, shangz_zd, shenz_jg, shenz_zd, chuangyb_jg, chuangyb_zd = 0, 0, 0, 0, 0, 0

        sh = getGegu('sh000001')
        sz = getGegu('sz399001')
        cyb = getGegu('sz399006')
        if sh != False:
            shangz_zuoshou = float(sh['gegu_zuoshou'])
            shangz_jg = float(sh['gegu_xianjia'])
            cha = shangz_jg - shangz_zuoshou
            if cha > 0:
                shangz_zd = cha / shangz_zuoshou
            else:
                shangz_zd = -(-cha / shangz_zuoshou)
            shangz_zd = str(round(shangz_zd*100, 2))+'%'
        if sz != False:
            shenz_zuoshou = float(sz['gegu_zuoshou'])
            shenz_jg = float(sz['gegu_xianjia'])
            cha = shenz_jg - shenz_zuoshou
            zhangfu = 0
            if cha > 0:
                shenz_zd = cha / shenz_zuoshou
            else:
                shenz_zd = -(-cha / shenz_zuoshou)
            shenz_zd = str(round(shenz_zd * 100, 2)) + '%'
        if cyb != False:
            chuangyb_zuoshou = float(cyb['gegu_zuoshou'])
            chuangyb_jg = float(cyb['gegu_xianjia'])
            cha = chuangyb_jg - chuangyb_zuoshou
            if cha > 0:
                chuangyb_zd = cha / chuangyb_zuoshou
            else:
                chuangyb_zd = -(-cha / chuangyb_zuoshou)
            chuangyb_zd = str(round(chuangyb_zd * 100, 2)) + '%'
        shangz_zd, shangz_jg = compareDapanNum(str(shangz_zd), str(shangz_jg))
        shenz_zd, shenz_jg = compareDapanNum(str(shenz_zd), str(shenz_jg))
        chuangyb_zd, chuangyb_jg = compareDapanNum(str(chuangyb_zd), str(chuangyb_jg))
        # 绘表
        tb_dapan = pt.PrettyTable(['大盘', '上证指数', '深证成指', '创业板指'])
        tb_dapan.add_row(['价格', shangz_jg, shenz_jg, chuangyb_jg])
        tb_dapan.add_row(['涨幅', shangz_zd, shenz_zd, chuangyb_zd])
        


        # 基金
        jjc = d.getJjCode()
        # 判断基金红绿 flag=1,估值 flag=0,净值 用于优化终端显示效果
        def compareNum(s, flag=0):
            color = Colored()
            if s != '--':
                if float(str(s)[:-1]) > 0.00:
                    return color.red('+' + s)
                elif float(str(s)[:-1]) < 0.00:
                    return color.green(s)
                else:
                    return color.white(s)
            else:
                return color.white(s)
        tb_jj = pt.PrettyTable()
        tb_jj.field_names = ["基金代码", "基金名称", "估值涨幅", "估值更新", "净值涨幅", "净值更新"]
        for i in jjc:
            jj, jj_jin = getJijin(i.strip())
            if jj != False:
                jjcode = i
                name, guzhi, gutime = jj['name'], jj['gszzl'] + '%', jj['gztime']
                try:
                    guzhi = compareNum(guzhi, flag=0)
                    jingzhi = float(str(jj_jin).split('"')[1].split(',')[1])
                    jingzhip = float(str(jj_jin).split('"')[1].split(',')[3])
                    jingzhitime = str(jj_jin).split('"')[1].split(',')[4]
                    jingzhizd = 0
                    cha = jingzhi - jingzhip
                    if cha > 0:
                        jingzhizd = cha / jingzhip
                    else:
                        jingzhizd = -(-cha / jingzhip)
                    jingzhizd = str(round(jingzhizd * 100, 2)) + '%'
                    jingzhizd = compareNum(jingzhizd, flag=1)
                    tb_jj.add_row([i, name, guzhi, gutime, jingzhizd, jingzhitime])
                except:
                    jingzhizd = '-'
                    jingzhizd = '-'
                    tb_jj.add_row([i, name, guzhi, gutime, jingzhizd, jingzhitime])

        # 显示
        if platform.system().lower() == 'windows':
            os.system("cls")
        elif platform.system().lower() == 'linux':
            os.system("clear")
        elif platform.system().lower() == 'darwin':
            os.system("clear")
        print(tb_dapan)
        print(tb_jj)
        
        time.sleep(5)

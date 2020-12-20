# 读取my.txt内容
class GetData():
    def getJjCode(self):
        f = open('my_jijin.txt', 'r', encoding='utf-8')
        jj_codes = f.readlines()
        return jj_codes

    def getGgCode(self):
        f = open('my_gegu.txt', 'r', encoding='utf-8')
        gg_codes = f.readlines()
        return gg_codes
import flask
import requests
import json

# 查询接口
def getGegu(gu_code):
    gegu = requests.get('http://hq.sinajs.cn/list=' + gu_code)
    gegu_status = gegu.status_code
    if gegu_status != 200:
        return False
    allinfo = gegu.text.split('"')[1].split(',')
    # print(allinfo)
    gegu_name = allinfo[0]
    # 今开
    gegu_jinkai = allinfo[1]
    # 昨收
    gegu_zuoshou = allinfo[2]
    # 现价
    gegu_xianjia = allinfo[3]
    # 今高
    gegu_jingao = allinfo[4]
    # 今低
    gegu_jindi = allinfo[5]
    # 竞买
    gegu_jingmai = allinfo[6]
    # 竞卖
    gegu_jingnai = allinfo[7]
    # 成交数
    gegu_chengjiaoshu = allinfo[8]
    # 成交额
    gegu_chengjiaoe = allinfo[9]
    # 买1
    gegu_mai1 = allinfo[10]
    # 买1价
    gegu_mai1p = allinfo[11]
    # 买2
    gegu_mai2 = allinfo[12]
    # 买2价
    gegu_mai2p = allinfo[13]
    # 买3
    gegu_mai3 = allinfo[14]
    # 买3价
    gegu_mai3p = allinfo[15]
    # 买4
    gegu_mai4 = allinfo[16]
    # 买4价
    gegu_mai4p = allinfo[17]
    # 买5
    gegu_mai5 = allinfo[18]
    # 买5价
    gegu_mai5p = allinfo[19]
    # 卖1
    gegu_nai1 = allinfo[20]
    # 卖1价
    gegu_nai1p = allinfo[21]
    # 卖2
    gegu_nai2 = allinfo[22]
    # 卖2价
    gegu_nai2p = allinfo[23]
    # 卖3
    gegu_nai3 = allinfo[24]
    # 卖3价
    gegu_nai3p = allinfo[25]
    # 卖4
    gegu_nai4 = allinfo[26]
    # 卖4价
    gegu_nai4p = allinfo[27]
    # 卖5
    gegu_nai5 = allinfo[28]
    # 卖5价
    gegu_nai5p = allinfo[29]
    # 日期
    gegu_date = allinfo[30]
    # 时间
    gegu_time = allinfo[31]
    res_info = {'gegu_name': gegu_name, 'gegu_jinkai': gegu_jinkai, 'gegu_zuoshou': gegu_zuoshou, 'gegu_xianjia': gegu_xianjia,\
            'gegu_jingao': gegu_jingao, 'gegu_jingmai':gegu_jingmai,'gegu_jingnai':gegu_jingnai,'gegu_chengjiaoshu':gegu_chengjiaoshu,\
            'gegu_chengjiaoe':gegu_chengjiaoe,'gegu_mai1':gegu_mai1,'gegu_mai1p':gegu_mai1p,'gegu_mai2':gegu_mai2,\
            'gegu_mai2p':gegu_mai2p,'gegu_mai3':gegu_mai3,'gegu_mai3p':gegu_mai3p,'gegu_mai4':gegu_mai4,'gegu_mai4p':gegu_mai4p,\
            'gegu_mai5':gegu_mai5,'gegu_mai5p':gegu_mai5p,'gegu_nai1':gegu_nai1,'gegu_nai1p':gegu_nai1p,'gegu_nai2':gegu_nai2,\
            'gegu_nai2p':gegu_nai2p,'gegu_nai3':gegu_nai3,'gegu_nai3p':gegu_nai3p,'gegu_nai4':gegu_nai4,'gegu_nai4p':gegu_nai4p,\
            'gegu_nai5':gegu_nai5,'gegu_nai5p':gegu_nai5p,'gegu_date':gegu_date,'gegu_time':gegu_time}
    return res_info

# res {'fundcode': '003095', 'name': '中欧医疗健康混合A', 'jzrq': '2020-12-17', 'dwjz': '3.2840', 'gsz': '3.2822', 'gszzl': '-0.06', 'gztime': '2020-12-18 15:00'}
def getJijin(ji_code):
    jijin_gu = requests.get('http://fundgz.1234567.com.cn/js/' + ji_code + '.js?rt=1463558676006')
    jijin_jin = requests.get('http://hq.sinajs.cn/list=f_'+ji_code)
    status = jijin_gu.status_code
    if status != 200:
        return False
    jijin_info = json.loads(jijin_gu.text[8:-2])
    return jijin_info, jijin_jin.text


import pymysql
from flask import Flask, render_template, url_for, request, json, jsonify
import json
import requests
# 打开数据库连接
from getInfo import getJijin

def startdb():
    db = pymysql.connect("localhost", "root", "123456", "fund")
    return db

def queryData(user):
    db = startdb()
    cursor = db.cursor()
    sql = 'SELECT * FROM favor WHERE user=%s'
    cursor.execute(sql, user)
    db_data = cursor.fetchall()
    db.close()
    return db_data

def insertData(id, user, name):
    db = startdb()
    cursor = db.cursor()
    sql = "INSERT INTO favor VALUES(null, '%s', '%s', '%s')" %(id, user, name)
    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()
    except:
        db.close()
        return False
    return True

def deleteData(user, id):
    db = startdb()
    cursor = db.cursor()
    sql = "DELETE FROM favor WHERE user='%s' and favorid='%s'" % (user, id)
    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()
    except:
        db.close()
        return False
    return True

app = Flask(__name__)
#设置编码
app.config['JSON_AS_ASCII'] = False


@app.route('/getFavor', methods=['POST', 'GET'])  # 关于route（）里面可以写url，提交的方式
def get_data():
    user = request.args['user']
    if user == '':
        return jsonify({'response_code': '404', 'response_body': []})
    udata = queryData(user)
    tmp = {'response_code': 200, 'response_body': []}
    for i in udata:
        favor_id = i[1]
        favor_name = i[3]
        tmp['response_body'].append({'id': favor_id, 'name': favor_name})
    return jsonify(tmp)

@app.route('/addFavor', methods=['POST', 'GET'])  # 关于route（）里面可以写url，提交的方式
def add_data():
    user = request.args['user']
    id = request.args['jjid']
    name = request.args['jjname']
    r = insertData(id, user, name)
    if r == False:
        return jsonify({'response_code': '400', 'response_body': []})
    else:
        return jsonify({'response_code': '200'})

@app.route('/delFavor', methods=['POST', 'GET'])  # 关于route（）里面可以写url，提交的方式
def del_data():
    user = request.args['user']
    id = request.args['jjid']
    r = deleteData(user, id)
    if r == False:
        return jsonify({'response_code': '400', 'response_body': []})
    else:
        return jsonify({'response_code': '200'})


if __name__ == '__main__':
    # insertData("000002", "wz", "xxx")
    app.debug = True
    # 跨域支持
    def after_request(resp):
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    app.after_request(after_request)
    app.run(host='0.0.0.0', port=50005)

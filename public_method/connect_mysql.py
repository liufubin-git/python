"""连接数据库"""

import pymysql
import logging


class ConnectMysql(object):
    """在实例化对象的时候，需要传入数据库连接的信息"""
    def __init__(self, host, user, password, port):
        """初始化实例的时候连接数据库"""
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.conn = pymysql.connect(host=self.host,  # 连接数据库
                                    port=self.port,
                                    user=self.user,
                                    password=self.password,
                                    charset='utf8'
                                    )

    def fetchall(self, sql):
        """返回数据的所有结果"""
        cursor = self.conn.cursor()                       # 建立游标
        try:
            cursor.execute(sql)                           # 游标执行sql语句
            logging.debug('执行sql：', sql)
        except Exception as e:                            # 对执行的语句进行异常判断，有异常就输出对应的异常并且返回False
            print('sql错误：', e)
            logging.error(e)
            logging.error(sql)
            return False
        row = cursor.fetchall()
        cursor.close()                                    # 关闭游标
        self.conn.close()                                 # 关闭连接
        return row                                       # 返回语句结果


connect = ConnectMysql(host='192.168.1.18', user='ai_dept_weinan', password='XSAPORHXmNcVlGVkMVtJ', port=3306)
sql1 = 'SELECT * FROM rz_combination_master.cm_user WHERE cellphone = 13345678999'
result1 = connect.fetchall(sql1)
print(result1)

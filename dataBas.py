
'''数据库'''


import  pymysql


class sqlHander:
    handdb = pymysql.connect('localhost', 'root', '666666', 'db1')
    handcu = handdb.cursor()

    # 创建列表
    def creatTab(self,tabname):
        check = "DROP TABLE IF EXISTS %s" % (tabname)
        self.handcu.execute(check)

        sql = """CREATE TABLE %s (
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,
                 SEX CHAR(1),
                 INCOME FLOAT )""" % (tabname)
        self.handcu.execute(sql)

    # 插入
    def insertData(self,firname = 'ios',lasname = 'xiaoming',age = 20,sex = 'M',incom = 1000):
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('%s', '%s','%d','%s','%.f')"""%(firname,lasname,age,sex,incom)
        try:
            self.handcu.execute(sql)
            # 提交
            self.handdb.commit()
        except:
            print('失败了')
            # 回滚
            self.handdb.rollback()

    # 查询
    def searchData(self,searchsql):
        try:
            self.handcu.execute(searchsql)
            # 提交
            self.handdb.commit()
            return self.handcu.fetchall()
        except:
            print('失败了')
            # 回滚
            self.handdb.rollback()
            return None


   # 更新数据/删除数据
    def funcpData(self,upsql):
        try:
            self.handcu.execute(upsql)
            # 提交
            self.handdb.commit()
        except:
            print('失败了')
            # 回滚
            self.handdb.rollback()

    # 删除数据



    def close(self):
        self.handdb.close()



hand = sqlHander()
hand.creatTab('iOS')
hand.insertData()
# 搜索
searSql = "SELECT * FROM EMPLOYEE  WHERE INCOME > 1000"
result = hand.searchData(searSql)
for row in result:
    print(row)

# 删除
delesql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
hand.funcpData(delesql)


# 更改
upsql = "UPDATE EMPLOYEE SET AGE = AGE + 1 , SEX = 'N'"
hand.funcpData(upsql)


hand.close()

#





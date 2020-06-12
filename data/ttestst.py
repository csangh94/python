import pymysql

def count_all(): # 정보 검색
    conn = pymysql.connect(host='localhost', port=3708, user='root', password='1234', db='big3', charset='utf8')
    curs = conn.cursor()
    sql = "select * from counttable"
    curs.execute(sql)
    rows = curs.fetchall()
    return rows
    conn.close()
def count2(): # 정보 검색
    conn = pymysql.connect(host='localhost', port=3708, user='root', password='1234', db='big3', charset='utf8')
    curs = conn.cursor()
    sql = "select * from counttable where countint >=10"
    curs.execute(sql)
    rows = curs.fetchall()
    return rows
    conn.close()
def count3(): # 정보 검색
    conn = pymysql.connect(host='localhost', port=3708, user='root', password='1234', db='big3', charset='utf8')
    curs = conn.cursor()
    sql = "select * from counttable where countint >=10 order by countint desc limit 10"
    curs.execute(sql)
    rows = curs.fetchall()
    return rows
    conn.close()

print(count2())
print(count3())
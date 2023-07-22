import requests
import pymysql

try:
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0913', db='simpletest_db', charset='utf8')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS testsimple (simple INT)")
    cur.execute("INSERT INTO testsimple VALUES (1)")

    conn.commit()
    conn.close()

    print("MySQL 연결 및 데이터 삽입 성공!")

except pymysql.Error as e:
    print("MySQL 오류 발생:", e)
# web_server_url = "http://165.246.116.20:80"
#
# response = requests.get(web_server_url)
# data = response.text
#
# print(data)
#
# lines = data.split("\n")
#
# ip_address = ''
#
# if len(lines) >= 4:
#     ip_address = lines[2].split(": ")[1]
#
# temperature = text=lines[3]
#
# print(ip_address)
# print(temperature)




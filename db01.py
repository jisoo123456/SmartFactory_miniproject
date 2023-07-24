import requests
import pymysql
import time
import tkinter as tk
from tkinter import messagebox

# 데이터베이스에 온도 데이터를 삽입하는 함수
def insert_temperature_to_mysql(temperature):
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='0913', db='miniproject_db', charset='utf8')
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS temperature_data (id INT AUTO_INCREMENT PRIMARY KEY, temperature FLOAT)")
        cur.execute("INSERT INTO temperature_data (temperature) VALUES (%s)", (temperature,))

        conn.commit()
        conn.close()

        print("MySQL에 데이터 삽입 성공!")

    except pymysql.Error as e:
        print("MySQL 오류 발생:", e)

# 웹 서버에서 온도 데이터를 가져오는 함수
def get_temperature_from_web_server(url):
    try:
        response = requests.get(url)
        data = response.json()

        temperature = data["temperature_celsius"]
        return temperature

    except requests.exceptions.RequestException as e:
        print("웹 서버에서 데이터 가져오기 오류:", e)
        return None

# 온도 데이터 리스트로부터 평균 온도를 계산하는 함수
def calculate_average_temperature(temperature_list):
    if not temperature_list:
        return 0

    total_temperature = sum(temperature_list)
    average_temperature = total_temperature / len(temperature_list)
    return average_temperature

# Tkinter 애플리케이션 생성
app = tk.Tk()
app.title("온도 데이터 확인")
app.geometry("300x100")

# 평균 온도 표시 레이블
lbl_average_temperature = tk.Label(app, text="", font=("Helvetica", 20))
lbl_average_temperature.pack()

# 주기적으로 평균 온도 표시 업데이트 함수
def update_average_temperature():
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='0913', db='miniproject_db', charset='utf8')
        cur = conn.cursor()

        cur.execute("SELECT temperature FROM temperature_data")
        rows = cur.fetchall()
        temperature_list = [float(row[0]) for row in rows]

        average_temperature = calculate_average_temperature(temperature_list)
        conn.close()

        lbl_average_temperature.config(text=f"평균 온도: {average_temperature:.2f} °C")

    except pymysql.Error as e:
        print("MySQL 오류 발생:", e)

    app.after(600000, update_average_temperature)  # 10분(600000밀리초)마다 업데이트

# Tkinter 이벤트 루프 시작
app.after(0, update_average_temperature)  # 애플리케이션 시작 시 최초 업데이트 호출
app.mainloop()

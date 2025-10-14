
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__, template_folder='html_files')


@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")

    userName = request.form.get("user")
    passWord = request.form.get("pwd")
    mobile = request.form.get("mobile")

    # 1、连接MySQL
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='future', charset='utf8mb4', db='mysql')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2、执行SQL
    sql = "insert into admin(user_name, pass_word, mobile) values(%s, %s, %s)"
    cursor.execute(sql, [userName, passWord, mobile])
    conn.commit()

    # 3、关闭连接
    cursor.close()
    conn.close()


    return "xxx"



@app.route("/show/user")
def show_user():
    # 1、连接MySQL
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='future', charset='utf8mb4', db='mysql')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2、执行SQL
    sql = "select * from admin"
    cursor.execute(sql)
    dataList = cursor.fetchall()

    # 3、关闭连接
    cursor.close()
    conn.close()

    return render_template('show_user.html', data_list=dataList)




if __name__ == '__main__':
    app.run()







from flask import Flask, render_template, request

# 配置模板文件夹为html_files
app = Flask(__name__, template_folder='html_files')


# 创建了网址 /show/info 和 函数index 的对应关系
# 以后用户在浏览器上访问 /show/info, 网站自动执行 index
@app.route("/show/info", methods=['GET'])
def index():

    # 1. 接受用户通过GET形式发送过来的数据
    print(request.args)
    # 2.给用户再返回结果


    # return "中国联通"

    # return """<h1> 中国 </h1>
    #         <span style='color:red;'>联通</span>"""

    # Flask内部会自动打开这个文件，并读取内容，将内容给用户返回。
    # 默认: 去当前项目目录的templates文件夹中找    （但是我这里一开始设置了默认的文件夹为html_files）
    return render_template("index.html")



@app.route("/get/news")
def get_news():
    return render_template("get_news.html")



# 学习案例:用户注册
@app.route("/register")
def register():
    return render_template("register.html")



@app.route("/new_register", methods=['GET'])
def new_register():
    return render_template("new_register.html")



if __name__ == '__main__':
    app.run()



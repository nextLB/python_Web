
from flask import Flask, render_template

# 配置模板文件夹为html_files
app = Flask(__name__, template_folder='html_files')


# 创建了网址 /show/info 和 函数index 的对应关系
# 以后用户在浏览器上访问 /show/info, 网站自动执行 index
@app.route("/show/info")
def index():
    # return "中国联通"

    # return """<h1> 中国 </h1>
    #         <span style='color:red;'>联通</span>"""

    # Flask内部会自动打开这个文件，并读取内容，将内容给用户返回。
    # 默认: 去当前项目目录的templates文件夹中找    （但是我这里一开始设置了默认的文件夹为html_files）
    return render_template("index.html")




if __name__ == '__main__':
    app.run()





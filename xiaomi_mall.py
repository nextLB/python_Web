
from flask import Flask, render_template, request

# 配置模板文件夹为html_files
app = Flask(__name__, template_folder='html_files')


# 创建了网址 /show/info 和 函数index 的对应关系
# 以后用户在浏览器上访问 /show/info, 网站自动执行 index
@app.route("/xiaomi_mall", methods=['GET'])
def xiaomi_mall():
    return render_template("xiaomi_mall.html")



if __name__ == '__main__':
    app.run()



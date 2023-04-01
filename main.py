from flask import Flask, render_template

app = Flask(__name__)

# 主頁面


@app.route("/")
def home():
    return render_template("main.html")

# 關於我


@app.route("/about/")
def about():
    return render_template("about.html")


# 主程式進入點
if __name__ == "__main__":
    app.run()

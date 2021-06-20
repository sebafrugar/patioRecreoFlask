from flask import Flask, render_template
app = Flask(__name__)   


@app.route('/play')
def recreo():
    return render_template("recreo.html",cuadrado="",num_time=3)


@app.route('/play/<num>')
def recreo_num(num):
    return render_template("recreo.html",cuadrado="",num_time=int(num))

@app.route('/play/<num>/<color>')
def recreo_num_color(num,color):
    return render_template("recreo.html",cuadrado="",num_time=int(num),color=color)


if __name__=="__main__":   
    app.run(debug=True)
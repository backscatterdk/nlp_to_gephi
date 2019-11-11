from flask import Flask, render_template, request, redirect

from nlp_to_net import start_nlp, draw_nodes

app = Flask(__name__)

global_nlp = start_nlp()


@app.route("/", methods=["GET", "POST"])
def hello(nlp=global_nlp):
    if request.method == "POST":

        req = request.form

        draw_nodes(text=req['Text'], nlp=global_nlp)

        return redirect(request.url)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

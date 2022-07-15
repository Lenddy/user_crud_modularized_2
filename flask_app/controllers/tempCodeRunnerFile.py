@app.route("/show_one/<int:num>")
def show_one(num):
    data= {"id":num}
    show_one = User.show_one(data)
    return render_template("show_one_user.html",show_one = show_one)
    
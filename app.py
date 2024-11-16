from flask import Flask, request, render_template
from test import testfun
import model


app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "<h1> Hello! </h1>"


# URL/<username>
# example:URL/Allen URL/Spark
@app.route("/<username>")
def greeting(username):
    output_html = f"""
    <h1>
        Hi {username}
    </h1>
    """
    return output_html


@app.route("/api/v2/department/dep_id/<string:dep_id>/emp_id/<int:emp_id>")
def get_employee(dep_id: str, emp_id: int):
    query_sql = f"""
    select
        emp_name,
        emp_id,
        emp_seat
    from emp
    where dep_id = '{dep_id}'
    and emp_id = '{emp_id}'
    """
    print(type(dep_id))
    print(type(emp_id))
    # db connect(query_sql)
    return {
        "emp_name": "Spark Liao",
        "emp_id": "123",
        "emp_seat": "22",
    }

# [GET] URL/hello?username=Allen&age=22


@app.route("/hello")
def hello():
    # return None if user do not gave the parameter
    username = request.args.get("username")
    age = request.args.get("age")

    if not username:
        return "What the fuck? Your name?"
    if not age:
        return "What the fuck? How old are son of bitch?"

    return f"Hello {username}, you are {age} years old."


# [POST] URL/hello_post  form_data = {"username": "Allen"}
@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    form_html = """
    <form method="post" action="/hello_post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <input type="submit" value="Submit">
    </form>
    """

    request_method = request.method
    username = request.form.get("username")

    if request_method == "POST":
        if len(username) > 0:
            form_html += f"""
            <h1>Hello! {username}</h1>"""
        else:
            form_html += f"""
            <h1>What's your name?</h1>"""

    return form_html


# URL//two_sum/<int:x>/<int:y>
@app.route("/two_sum/<int:x>/<int:y>")
def two_sum(x: int, y: int) -> str:
    return str(testfun(x, y))


@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                           column=column)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

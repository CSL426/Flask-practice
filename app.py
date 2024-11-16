from flask import Flask

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


# [GET] URL/hello?username=Allen&age=22
@app.route("/api/v2/apartment/dep_id/<dep_id>/<emp_id>")
def get_employee(dep_id, emp_id):
    query_sql = f"""
    select
        emp_name,
        emp_id,
        emp_seat
    from emp
    where dep_id = '{dep_id}'
    and emp_id = '{emp_id}'
    """
    # db connect(query_sql)
    return {
        "emp_name": "Spark Liao",
        "emp_id": "123",
        "emp_seat": "22",
    }


# [POST] URL/hello_post  form_data = {"username": "Allen"}
if __name__ == "__main__":
    app.run()

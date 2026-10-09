from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import mysql.connector

app = FastAPI()


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="company"
    )


@app.get("/", response_class=HTMLResponse)
def home():
    return show_page()


@app.post("/add-employee", response_class=HTMLResponse)
def add_employee(
    employee_id: int = Form(...),
    employee_name: str = Form(...),
    father_name: str = Form(...),
    age: int = Form(...),
    address: str = Form(...),
    phone: str = Form(""),
    job_title: str = Form(""),
    salary: float = Form(0),
    joining_date: str = Form("")
):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
    INSERT INTO employee
    (
        employee_id,
        employee_name,
        father_name,
        age,
        address,
        phone,
        job_title,
        salary,
        joining_date
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        employee_id,
        employee_name,
        father_name,
        age,
        address,
        phone,
        job_title,
        salary,
        joining_date if joining_date else None
    )

    cursor.execute(sql, values)
    connection.commit()

    cursor.close()
    connection.close()

    return show_page()


def show_page():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            employee_id,
            employee_name,
            father_name,
            age,
            address,
            phone,
            job_title,
            salary,
            joining_date
        FROM employee
    """)

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    with open("index.html", "r", encoding="utf-8") as file:
        html = file.read()

    table = """
    <h2>Employee Records</h2>

    <table border="1" cellpadding="8">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Father Name</th>
            <th>Age</th>
            <th>Address</th>
            <th>Phone</th>
            <th>Job Title</th>
            <th>Salary</th>
            <th>Joining Date</th>
        </tr>
    """

    for employee in employees:
        table += "<tr>"

        for value in employee:
            table += f"<td>{value if value is not None else ''}</td>"

        table += "</tr>"

    table += """
    </table>
    """

    html = html.replace("</body>", table + "</body>")

    return HTMLResponse(content=html)
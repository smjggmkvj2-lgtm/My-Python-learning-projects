import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ALLOWED_STATUSES = ["Open", "In Progress", "Closed"]
ALLOWED_PRIORITIES = ["Low", "Medium", "High"]
def init_db():
    connection = sqlite3.connect("tickets.db")
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            priority TEXT NOT NULL DEFAULT 'Medium',
            created_at TEXT
        )
    """)
    columns = connection.execute("PRAGMA table_info(tickets)").fetchall()
    column_names = [column[1] for column in columns]
    if "created_at" not in column_names:
        connection.execute("ALTER TABLE tickets ADD COLUMN created_at TEXT")
    if "priority" not in column_names:
        connection.execute("ALTER TABLE tickets ADD COLUMN priority TEXT NOT NULL DEFAULT 'Medium'")
    connection.commit()
    connection.close()
@app.route("/")
def home():
    status_filter = request.args.get("status", "All")
    if status_filter != "All" and status_filter not in ALLOWED_STATUSES:
        status_filter = "All"
    connection = sqlite3.connect("tickets.db")
    connection.row_factory = sqlite3.Row
    if status_filter == "All":
        tickets = connection.execute(
            "SELECT * FROM tickets ORDER BY id DESC"
        ).fetchall()
    else:
        tickets = connection.execute(
            """
            SELECT * FROM tickets
            WHERE status = ?
            ORDER BY id DESC
            """,
            (status_filter,)
        ).fetchall()
    connection.close()
    return render_template("index.html", tickets=tickets, status_filter=status_filter)

@app.route("/create", methods=["GET", "POST"])
def create_ticket():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "Medium")
        if priority not in ALLOWED_PRIORITIES:
            priority = "Medium"
        created_at = datetime.now().strftime("%d-%m-%Y %H:%M")
        if not title or not description:
            return render_template("create_ticket.html", error="Title and description are required.", title=title, description=description, priority=priority)
        connection = sqlite3.connect("tickets.db")
        connection.execute(
            """
            INSERT INTO tickets (title, description, priority, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (title, description, priority, created_at)
        )
        connection.commit()
        connection.close()

        return redirect(url_for("home"))
    return render_template("create_ticket.html")
@app.route("/edit/<int:ticket_id>", methods=["GET", "POST"])
def edit_ticket(ticket_id):
    connection = sqlite3.connect("tickets.db")
    connection.row_factory = sqlite3.Row
    ticket = connection.execute(
        "SELECT * FROM tickets WHERE id = ?",
        (ticket_id,)
    ).fetchone()
    if ticket is None:
        connection.close()
        return "Ticket not found.", 404
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "Medium")
        if priority not in ALLOWED_PRIORITIES:
            priority = "Medium"
        if not title or not description:
            connection.close()
            entered_ticket = {
                "title": title,
                "description": description,
                "priority": priority
            }
            return render_template("edit_ticket.html", ticket=entered_ticket, error="Title and description are required.")
        connection.execute(
            """
            UPDATE tickets
            SET title = ?, description = ?, priority = ?
            WHERE id = ?
            """,
            (title, description, priority, ticket_id)
        )
        connection.commit()
        connection.close()
        return redirect(url_for("home"))
    connection.close()
    return render_template("edit_ticket.html", ticket=ticket)
@app.route("/update-status/<int:ticket_id>", methods=["POST"])
def update_status(ticket_id):
    new_status = request.form.get("status", "")
    if new_status not in ALLOWED_STATUSES:
        return "Invalid status.", 400
    connection = sqlite3.connect("tickets.db")
    cursor = connection.execute(
        """
        UPDATE tickets
        SET status = ?
        WHERE id = ?
        """,
        (new_status, ticket_id)
    )

    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        return "Ticket not found.", 404
    return redirect(url_for("home"))
@app.route("/delete/<int:ticket_id>", methods=["POST"])
def delete_ticket(ticket_id):
    connection = sqlite3.connect("tickets.db")
    cursor = connection.execute(
        "DELETE FROM tickets WHERE id = ?", 
        (ticket_id,)
        )
    connection.commit()
    connection.close()
    if cursor.rowcount == 0:
        return "Ticket not found.", 404
    return redirect(url_for("home"))
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
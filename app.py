import flask
import psycopg2
import psycopg2.extras

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    DB_HOST = "ec2-67-202-63-147.compute-1.amazonaws.com"
    DB_NAME = "d7j127qpvbukdo"
    DB_USER = "zvtclmedqrwqwd"
    DB_PASS = "ceea7532a0c5ea5d15d3fb1636be39bdabbeb4a34d3fece0a6c606d589d530a2"

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM characters;")
    row_headers = [x[0] for x in cur.description]  # this will extract row headers
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    conn.commit()
    cur.close()
    conn.close()
    all_characters = json_data
    return all_characters


if __name__ == '__main__':
    app.run()

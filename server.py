from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote_plus
import os

api_key = os.environ.get("GOOGLE_MAPS_API_KEY")

def get_body_params(body):
    if not body:
        return {}
    parameters = body.split("&")

    # split each parameter into a (key, value) pair, and escape both
    def split_parameter(parameter):
        k, v = parameter.split("=", 1)
        k_escaped = unquote_plus(k)
        v_escaped = unquote_plus(v)
        return k_escaped, v_escaped

    body_dict = dict(split_parameter(x) for x in parameters)
    print(f"Parsed parameters as: {body_dict}")
    # return a dictionary of the parameters
    return body_dict


def submission_to_table_rows(item):

    return f"""
    <tr>
        <td>{item['name']}</td>
        <td>{item['creature_type']}</td>
        <td>{item['stage_of_life']}</td>
        <td>{item['location']}</td>
        <td>{item['phone_number']}</td>
        <td><a href="{item['website']}">{item['website']}</a></td>
    </tr>
    """

# NOTE: Please read the updated function carefully, as it has changed from the
# version in the previous homework. It has important information in comments
# which will help you complete this assignment.
def handle_req(url, body=None):
    """
    The url parameter is a *PARTIAL* URL of type string that contains the path
    name and query string.

    If you enter the following URL in your browser's address bar:
    `http://localhost:4131/myform.html?name=joe` then the `url` parameter will have
    the value "/myform.html?name=joe"

    This function should return two strings in a list or tuple. The first is the
    content to return, and the second is the content-type.
    """

    # Get rid of any query string parameters
    url, *_ = url.split("?", 1)
    # Parse any form parameters submitted via POST
    parameters = get_body_params(body)

    if url == "/" or url == "/myguests.html":
        return open("static/html/myguests.html").read(), "text/html"
    elif url == "/myform.html":
        return open("static/html/myform.html").read(), "text/html"
    if url == "/stocks.html":
        return open("static/html/stocks.html").read(), "text/html"
    elif url == "/mywelcome.html":
        return open("static/html/mywelcome.html", encoding="utf-8").read(), "text/html"
    elif url == "/img/gophers-mascot.png":
        return open("static/img/gophers-mascot.png", "br").read(), "image/png"
    # NOTE: The files you return will likely be different for your server, but the code to
    # show you examples of how yours may look. You will need to change the paths
    # to match the files you want to serve. Before you do that, make sure you
    # understand what the code is doing, specifically with the MIME types and
    # opening some files in binary mode, i.e. `open(..., "br")`.
    elif url == "/css/myguest.css":
        return open("static/css/myguest.css").read(), "text/css"
    elif url == "/css/mywelcome.css":
        return open("static/css/mywelcome.css").read(), "text/css"
    elif url == "/css/myform.css":
        return open("static/css/myform.css").read(), "text/css"
    elif url == "/css/stocks.css":
        return open("static/css/stocks.css").read(), "text/css"
    elif url == "/js/script.js":
        return open("static/js/script.js").read(), "text/javascript"
    elif url == "/js/formMap.js":
        return open("static/js/formMap.js").read(), "text/javascript"
    elif url == "/js/index.js":
        return open("static/js/index.js").read(), "text/javascript"
    elif url == "/js/tableImage.js":
        return open("static/js/tableImage.js").read(), "text/javascript"
    elif url == "/img/keller.jpg":
        return open("static/img/keller.jpg", "br").read(), "image/jpeg"
    elif url == "/img/rec.jpg":
        return open("static/img/rec.jpg", "br").read(), "image/jpeg"
    elif url == "/img/walter.jpg":
        return open("static/img/walter.jpg", "br").read(), "image/jpeg"
    elif url == "/img/Tate.png":
        return open("static/img/Tate.png", "br").read(), "image/png"
    elif url == "/img/compsci.jpg":
        return open("static/img/compsci.jpg", "br").read(), "image/jpeg"
    elif url == "/img/UMN.jpg":
        return open("static/img/UMN.jpg", "br").read(), "image/jpeg"
    elif url == "/img/Lind.jpg":
        return open("static/img/Lind.jpg", "br").read(), "image/jpeg"
    # TODO: Update the HTML below to match your other pages and
    # implement the `submission_to_table_rows` function.
    elif url == "/guestlog.html":
        return (
            f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title> Guest Submission </title>
                    <style>
        html, body {{
            height: 100%;
            margin: 0;
        }}
        body {{
            background-color: #4a5c60;
        }}
        #navigation {{
            display: flex;
            background: linear-gradient(45deg, maroon 55%, gold 45%);
        }}
        #navigation > div {{
            padding: 10px;
            color: white;
        }}
        #navigation > div > a {{
            color: white;
            text-decoration: none;
        }}
        .container {{
            display: flex;
            justify-content: center;
            margin-top: 60px;
        }}
        table {{
            border-collapse: collapse;
            background-color: white;
            width: 70%;
        }}
        th, td {{
            border: 1px solid grey;
            padding: 12px;
        }}
        th {{
            background-color: #ddd;
        }}
    </style>
            </head>
            <body>
                    <div id="navigation">
                        <div><a href="mywelcome.html">Welcome page</a></div>
                        <div><a href="myform.html">Form Input</a></div>
                        <div><a href="myguests.html">Guest info</a></div>
                    </div>
                <h1> My New Guests </h1>
                <div class="container">
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Type of Creature</th>
                                <th>Stage of Life</th>
                                <th>Location</th>
                                <th>Phone</th>
                                <th>Website</th>
                            </tr>
                        </thead>
                        <tbody>
                            {submission_to_table_rows(parameters)}
                        </tbody>
                    </table>
                </div>
            </body>
            </html>""",
            "text/html; charset=utf-8",
        )
    else:
        return open("static/html/404.html").read(), "text/html; charset=utf-8"


# Don't change content below this. It would be best if you just left it alone.


class RequestHandler(BaseHTTPRequestHandler):
    def __c_read_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        body = str(body, encoding="utf-8")
        return body

    def __c_send_response(self, message, response_code, headers):
        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # Send the first line of response.
        self.protocol_version = "HTTP/1.1"
        self.send_response(response_code)

        # Send headers (plus a few we'll handle for you)
        for key, value in headers.items():
            self.send_header(key, value)
        self.send_header("Content-Length", str(len(message)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)

    def do_GET(self):
        # Call the student-edited server code.
        message, content_type = handle_req(self.path)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        self.__c_send_response(
            message,
            200,
            {
                "Content-Type": content_type,
                "Content-Length": len(message),
                "X-Content-Type-Options": "nosniff",
            },
        )

    def do_POST(self):
        body = self.__c_read_body()
        message, content_type = handle_req(self.path, body)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        self.__c_send_response(
            message,
            200,
            {
                "Content-Type": content_type,
                "Content-Length": len(message),
                "X-Content-Type-Options": "nosniff",
            },
        )


def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ("", PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()


run()

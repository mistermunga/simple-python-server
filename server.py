import http.server
import json
import weather_updater

PORT = 9999
DIRECTORY = "resources"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == "/weather":
            weather = weather_updater.get_weather()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(weather).encode())
        else:
            super().do_GET()


if __name__ == "__main__":
    weather_updater.update_weather()

    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
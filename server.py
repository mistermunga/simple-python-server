import http.server
import json
import threading
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


def listen_for_exit(httpd_process):
    while True:
        user_input = input()
        if user_input.strip().upper() == "EXIT":
            print("Shutting down server...")
            httpd_process.shutdown()
            break


if __name__ == "__main__":
    weather_updater.update_weather()

    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        print("Type EXIT to stop the server.")

        exit_thread = threading.Thread(target=listen_for_exit, args=(httpd,), daemon=True)
        exit_thread.start()

        httpd.serve_forever()
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import SimpleHTTPServer

PORT = 10157

class AjaxHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""

    def do_POST(self):
        """Handle a post request by returning the squer of the number.
           """
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        #Send the html massage
        self.wfile.write("Egils Ilsters, 161REB157")
        return

try:
    server = HTTPServer(('',PORT), AjaxHandler)
    print 'Startrd AJAX handler on port' , PORT
    server.serve_forever()

except KeyboardInterrupt:
    print '^C receved, shutting down the web server'
    server.socked.close()

# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
from utils import TwitterTimelineMixin
from config import PORT_NUMBER


class myHandler(BaseHTTPRequestHandler, TwitterTimelineMixin):

    def do_GET(self):
        if self.path == "/":
            self.path = "/api-embed.html"
        if self.path == "/timeline.json":
            return self.timeline_json()

        try:
            sendReply = False
            if self.path.endswith(".html"):
                self.path = '/templates' + self.path  # switch to templates
                mimetype = 'text/html'
                sendReply = True
            if sendReply is True:
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def runner():
    try:
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        stinfo = 'Webserver wird gestartet auf Port {}'.format(PORT_NUMBER)
        print (stinfo)
        server.serve_forever()

    except KeyboardInterrupt:
        print ('...Webserver wird heruntergefahren')
        server.socket.close()


if __name__ == '__main__':
    runner()

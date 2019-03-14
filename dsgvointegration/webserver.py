# -*- coding: utf-8 -*-

import sys
from os import curdir, sep

from dsgvointegration.utils import TwitterTimelineMixin
from dsgvointegration.config import (PORT_NUMBER, TEMPLATE_FOLDER)

if sys.version_info < (3, 0):
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
else:
    from http.server import BaseHTTPRequestHandler, HTTPServer


class myHandler(BaseHTTPRequestHandler, TwitterTimelineMixin):

    def do_GET(self):
        if self.path == "/":
            self.path = "/api-embed.html"
        if self.path == "/timeline.json":
            return self.timeline_json()

        try:
            sendReply = False
            if self.path.endswith(".html"):
                self.path = '/{}{}'.format(TEMPLATE_FOLDER, self.path)
                mimetype = 'text/html'
                sendReply = True
            if sendReply is True:
                fpath = '{}{}{}'.format(curdir, sep, self.path)
                f = open(fpath, 'rb')
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))


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

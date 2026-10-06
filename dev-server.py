#!/usr/bin/env python3
"""Vývojový server: každá "subdoména" se obsluhuje z vlastní složky.

  http://bezrutiny.localhost:8080          -> hlavni/
  http://program.bezrutiny.localhost:8080  -> program/
  http://vyzva.bezrutiny.localhost:8080    -> vyzva/

Spuštění:  python3 dev-server.py [port]
(Chrome, Firefox i novější macOS překládají *.localhost na tento počítač.)
"""
import http.server, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
FOLDERS = {"program": "program", "vyzva": "vyzva"}


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        host = (self.headers.get("Host") or "").split(":")[0].lower()
        folder = None
        for tld in ("bezrutiny.localhost", "bezrutiny.cz"):
            if host == tld:
                folder = "hlavni"
            elif host.endswith("." + tld):
                folder = FOLDERS.get(host[: -len(tld) - 1])
        self.directory = os.path.join(ROOT, folder) if folder else ROOT
        return super().translate_path(path)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler) as srv:
        print("Běží na http://bezrutiny.localhost:%d" % port)
        srv.serve_forever()

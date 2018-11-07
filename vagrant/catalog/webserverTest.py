from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Product

engine = create_engine('sqlite:///Amazon.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        try:

            if self.path.endswith("/amazon"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<H1>DEPARTMENTS</H1>"
                output += "</br></br>"
                output += '''<a href="/amazon/newcat">Create a new Category</a></br>'''

                cat = session.query(Category).all()
                for item in cat:
                    output += "<html><body>"
                    output += "<h2> %s </h2>" % item.name
                    output += '''<a href="https://example.com">edit</a></br>'''
                    output += '''<a href="https://example.com">delete</a>'''
                    output += "</br></br>"
                    print (item.name)
                    prod = session.query(Product).join(Category).filter(Product.category_id==item.id).all()
                    output += "<ul>"
                    for itemprod in prod:
                        output += "<h4><li> %s </h4></li>" % itemprod.name
                        print (itemprod.name)
                    print ("\n")
                    output += "</ul>"

#                    menu = session.query(MenuItem).join(Restaurant).filter(MenuItem.restaurant_id==Restaurant.id).all()
#                    for menuitem in menu:
#                        output += "<h2> %s </h2>" % menuitem.name
#                        print menuitem.name
                output += "</body></html>"
                print ("\n")
                self.wfile.write(output)
                return

            if self.path.endswith("/amazon/newcat"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/amazon/newcat'><h2>Would you like to create a new Category?</h2><input name="newcat" type="text" ><input type="submit" value="Create"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print (output)
                return


        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/amazon/newcat"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newcat')

                category = Category(name = messagecontent[0])
                print ("New category : %s" % category.name)
                session.add(category)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/amazon')
                self.end_headers()

        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print ("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()

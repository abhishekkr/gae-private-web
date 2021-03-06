"""[gae_gen_txt.py]
this module will generate the text required for files to be created
in a new Google AppEngine suitable to act as a Flat Web
___
"""

def txt_index_yml():
  return """indexes:

# AUTOGENERATED

# This index.yaml is automatically updated whenever the dev_appserver
# detects that a new type of query is run.  If you want to manage the
# index.yaml file manually, remove the above marker line (the line
# saying "# AUTOGENERATED").  If you want to manage some indexes
# manually, move them above the marker line.  The index.yaml file is
# automatically uploaded to the admin console when you next deploy
# your application using appcfg.py.""" 

def txt_app_yml(gae_app_name):
  return """application: """ + gae_app_name + """
version: 1
runtime: python
api_version: 1

handlers:
- url: /flat_web
  static_dir: flat_web/
  login: admin  

- url: /
  script: main.py
  login: required
"""

def txt_main_py():
  return """\"\"\"[ main.py ]
it's just here to redirect '/' to '/index.htm'
the redirect-link could be changed by changing the link below
\"\"\"

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class MainHandler(webapp.RequestHandler):
  def get(self):
    self.redirect('/flat_web/index.htm')
  def post(self):
    self.redirect('/flat_web/index.htm')

def main():
  application = webapp.WSGIApplication(
    [
          ('/', MainHandler),
        ], debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
"""

def txt_flat_root(gae_app_name):
  return """<html>
  <head>
  	<title>""" + gae_app_name + """</title>
  </head>
  <body>
  	<h1>""" + gae_app_name + """</h1>
	<h3>Your own Static Content Website served by Google AppEngine</h3>
	<h5 stylw="float:bottom; margin-bottom:5px;">
		created by using 
		<a href="https://github.com/abhishekkr/gae-flat-web">
			https://github.com/abhishekkr/gae-flat-web
		</a>
	</h5>
  </body>
</html>"""

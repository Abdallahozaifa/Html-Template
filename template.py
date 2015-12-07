import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
        def write(self, *a, **kw):
                self.response.out.write(*a, **kw)

        def render_str(self, template, **params):
                t = jinja_env.get_template(template)
                return t.render(params)

        def render(self, template, **kw):
                self.write(self.render_str(template, **kw))

class MainPage(Handler):
		def get(self):
				   self.render("template.html")

class AboutPage(Handler):
		def get(self):
				   self.render("about.html")				   

class InterestsPage(Handler):
		def get(self):
				   self.render("interests.html")

class ContactPage(Handler):
		def get(self):
				   self.render("contact.html")

app = webapp2.WSGIApplication([('/', MainPage),
								('/about.html', AboutPage),
								('/interests.html', InterestsPage), 
								('/contact.html', ContactPage)])
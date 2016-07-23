#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2
from google.appengine.ext import ndb

#setting up jinja
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class FeedbackComment(ndb.Model):
    name = ndb.StringProperty(required=False)
    comment = ndb.StringProperty(required=True)
    date_and_time = ndb.DateProperty(required=True)

#homepage handler
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.write(template.render())

class SadHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('mood-pages.html')
        self.response.write(template.render({"mood": "Sad"}))

class HappyHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('mood-pages.html')
        self.response.write(template.render({"mood": "Happy"}))

class LitHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('mood-pages.html')
        self.response.write(template.render({"mood": "Lit"}))

class TrumpHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('trump.html')
        self.response.write(template.render())

class FeedbackHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('feedback.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sad', SadHandler),
    ('/happy', HappyHandler),
    ('/lit', LitHandler),
    ('/trump', TrumpHandler),
    ('/feedback', FeedbackHandler)
], debug=True)

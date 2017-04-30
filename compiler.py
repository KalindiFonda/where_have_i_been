
import os
import webapp2
import jinja2

from google.appengine.ext import ndb
from google.appengine.api import urlfetch
import urllib

import ast
import loc_data
import time # for delay
import keys

template_dir = os.path.join(os.path.dirname(__file__), "templates")
JINJA_ENVIRONMENT  = jinja2.Environment(
                loader = jinja2.FileSystemLoader(template_dir),
                autoescape = True)


class Location(ndb.Model):
    """location object"""
    loc_coordinates = ndb.PickleProperty()
    loc_name =  ndb.StringProperty()
    loc_country =  ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


def populate():
    """populate db with some days"""
    locations = loc_data.loc_data
    for l in locations:
        location_instance = Location( loc_coordinates = l["loc_coordinates"], loc_name = l["loc_name"], loc_country = l["loc_country"])
        location_instance.put()
    time.sleep(.1)


def get_tot():
    entries = Location.query().fetch()

    if not entries:
        # if DB empty create some entries
        populate()
        entries = Location.query().fetch()

    template_values = {
        "locations" : entries,
        "google_maps_url": "https://maps.googleapis.com/maps/api/js?key=" + keys.google_maps_key + "&libraries=places"
    }

    return template_values


def get_template_values(template):

    get_values_function_mapper = {
        "index" : get_tot,
        "input": get_tot,
    }

    if template in get_values_function_mapper:
        return get_values_function_mapper[template]()

    return {}


def get_loc_info(loc_input):
    api_key = keys.api_key
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(urllib.quote(loc_input, safe=''), api_key)
    result = urlfetch.fetch(url=url, validate_certificate = False).content
    result = ast.literal_eval(result)
    try:
        latitude = result['results'][0]['geometry']['location']['lat']
        longitude = result['results'][0]['geometry']['location']['lng']
        loc_coordinates = {"lng": longitude,"lat":latitude}
        loc = loc_input.split(",")
        loc_name, loc_country = loc[0], loc[-1]
        target = {"loc_name": loc_name, "loc_country": loc_country, "loc_coordinates": loc_coordinates}
        return target
    except:
        print result.content


class Page(webapp2.RequestHandler):

    def get(self, reg_input="index"):

        template_values = get_template_values(reg_input)
        html_template = reg_input + ".html"
        template = JINJA_ENVIRONMENT.get_template(html_template)
        self.response.write(template.render(template_values))


    def post(self, reg_input="index"):

        loc_full_name = self.request.get("location")
        loc_info = get_loc_info(loc_full_name)

        location = Location(
            loc_name = loc_info["loc_name"],
            loc_country = loc_info["loc_country"],
            loc_coordinates = loc_info["loc_coordinates"]
        )

        location.put()
        time.sleep(.1)

        self.redirect('/' + reg_input)


app = webapp2.WSGIApplication([(r'/', Page), ('/(\w+)', Page)], debug = True)
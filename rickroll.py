import os

from flask import Blueprint, redirect

from hacker_urls import HACKER_URLS

rickroll_bp = Blueprint('rickroll_bp', __name__)

CLASSIC_RICKROLL_URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Here is your chance to change the redirect url with an environment variable.
RICKROLL_URL = os.getenv('RICKROLL_URL', CLASSIC_RICKROLL_URL)

_rickroll_logger = None


def set_rickroll_logger(logger):
    _rickroll_logger = logger


@rickroll_bp.endpoint("rickroll")
@rickroll_bp.route("/rickroll")
def rickroll(**kwargs):
    #          ^^^ Them thar' kwargs lets a fella put patterns in the url rules such as '/owa/<ima>/<hunk>'
    if _rickroll_logger:
        _rickroll_logger() # Your logger can grab the request object and then find the goodies like the source IP.
    return redirect(RICKROLL_URL)


def route_hacker_urls(blueprint=None, endpoint="rickroll", bad_urls=None):
    # I haven't tried this with a different blueprint or endpoint. So test well if you change the defaults.
    if blueprint is None:
        blueprint = rickroll_bp
    if bad_urls is None:
        bad_urls = HACKER_URLS
    for rule in bad_urls:
        blueprint.add_url_rule(rule, endpoint=endpoint)
    return blueprint

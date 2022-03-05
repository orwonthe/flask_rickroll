from flask import Flask, Blueprint

# This is just sample code, to show y'all how to use route_hacker_urls".

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static',
)


# I used the create_app technique because I got it working that way.
# With Flask, you don't need to get many PRs deep before you need it anyway.
def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp, url_prefix='/')
    # Note the local import.
    # That is, I think, just me being cautious.
    # Flask can get mighty frisky when a fella tries to get fancy.
    from rickroll import route_hacker_urls
    app.register_blueprint(route_hacker_urls(), url_prefix='/')  # Note: absolute prefix
    return app


@home_bp.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    create_app().run()

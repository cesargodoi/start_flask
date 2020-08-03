{%- if dyna -%}
from dynaconf import FlaskDynaconf


def init_app(app):
    FlaskDynaconf(app)
    app.config.load_extensions("EXTENSIONS")

{%- else -%}
def init_app(app):
    app.config['SECRET_KEY'] = 'super_secret'
    {%- if sqlal %}
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{{ proj }}.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'darkly'
    
    {%- else %}
    # here we pass the settings of our project
    {% endif %}
    {% if afp and sqlal %}
    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
        app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    {%- endif %}
{%- endif %}
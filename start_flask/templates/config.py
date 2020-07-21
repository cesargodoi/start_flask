def init_app(app):
    {% if sqlal %}
    app.config['SECRET_KEY'] = 'super_secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{{ proj }}.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'darkly'
    
    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
        app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    {% else %}
    # here we pass the settings of our project
    pass

    {% endif %}

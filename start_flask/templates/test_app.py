def test_app_is_created(app):
    assert app.name == '{{ proj }}.app'


def test_config_is_loaded(config):
    assert config['DEBUG'] is False # is True if FLASK_ENV=development


def test_request_returns_404(client):
    assert client.get('/some_invalid_route').status_code == 404
    
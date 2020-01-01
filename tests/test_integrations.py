import os
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'TEST'
    client = app.test_client()
    with app.app_context():
        pass
    app.app_context().push()
    yield client


def test_index(client):
    rv = client.get('/homepage')
    assert rv.status_code == 200

def test_register(client):
    rv = client.get('/register')
    assert rv.status_code == 200

def test_signIn(client):
    rv = client.get('/signin')
    assert rv.status_code == 200

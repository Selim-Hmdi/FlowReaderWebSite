import os
import pytest
from app import app
from flask import url_for


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
    rv = client.get('/')
    assert rv.status_code == 200

def test_register(client):
    rv = client.get('/register')
    assert rv.status_code == 200

def test_login(client):
    rv = client.get('/login')
    assert rv.status_code == 200

def test_flow(client):
    rv = client.get('/flow')
    assert rv.status_code == 302

"""
Tests for secure_app web pages.
Command: pytest secure_app/tests --cov=secure_app --cov-report term-missing:skip-covered
"""

import pytest

from django.shortcuts import reverse

from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model

pytestmark = pytest.mark.django_db


def test_index_page_get_success(client):
    """Test index page get success."""

    r = client.get(reverse('index'))

    assert r.status_code == 200
    assert b'<title>SecureX</title>' in r.content


def test_register_page_get_success(client):
    """Test register page get success."""

    r = client.get(reverse('register'))

    assert r.status_code == 200
    assert b'<title>SecureX | Register</title>' in r.content


def test_register_has_protected_form(client):
    r = client.get(reverse('register'))

    assert r.status_code == 200
    assert 'register_form' in r.context
    assert 'csrf_token' in r.context


def test_register_create_user_success(client):
    """Test post request to register page creates user successfully."""

    data = {
        'username': 'test_user',
        'email': 'test_email@example.com',
        'password1': 'test_pass_123',
        'password2': 'test_pass_123'
    }

    r = client.post(reverse('register'), data=data)
    messages_received = list(get_messages(r.wsgi_request))
    user = get_user_model().objects.filter(username=data['username'])

    assert r.status_code == 302
    assert r['Location'] == reverse('login')
    assert len(messages_received) == 1
    assert messages_received[0].message == 'Account was created successfully!'
    assert user.exists()
    assert len(user) == 1
    assert user[0].email == data['email']  # noqa


def test_register_invalid_data_fails(client):
    """Test post request to register page with invalid data fails."""

    data = {
        'username': 'test_user',
        'email': 'asdf',
        'password1': 'test_pass_123',
        'password2': 'test_pass_123'
    }

    r = client.post(reverse('register'), data=data)
    messages_received = list(get_messages(r.wsgi_request))
    user = get_user_model().objects.filter(username=data['username'])

    assert r.status_code == 302
    assert len(messages_received) == 1
    assert messages_received[0].message == 'Invalid data provided.'
    assert not user.exists()


def test_login_page_get_success(client):
    """Test login page get success."""

    r = client.get(reverse('login'))

    assert r.status_code == 200
    assert b'<title>SecureX | Login</title>' in r.content


def test_dashboard_page_get_success(client, sample_user):
    """Test dashboard page get success."""

    client.force_login(sample_user)
    r = client.get(reverse('dashboard'))

    assert r.status_code == 200
    assert b'<title>SecureX | Dashboard</title>' in r.content

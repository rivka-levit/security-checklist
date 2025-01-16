"""
Tests for secure_app web pages.
Command: pytest secure_app/tests --cov=secure_app --cov-report term-missing:skip-covered
"""

import pytest

from django.shortcuts import reverse

pytestmark = pytest.mark.django_db


def test_index_page_get_success(client):
    """Test index page get success."""

    r = client.get(reverse('index'))

    assert r.status_code == 200
    assert b'<title>Secure Checklist</title>' in r.content


def test_register_page_get_success(client):
    """Test register page get success."""

    r = client.get(reverse('register'))

    assert r.status_code == 200
    assert b'<title>Secure Checklist | Register</title>' in r.content


def test_login_page_get_success(client):
    """Test login page get success."""

    r = client.get(reverse('login'))

    assert r.status_code == 200
    assert b'<title>Secure Checklist | Login</title>' in r.content


def test_dashboard_page_get_success(client, sample_user):
    """Test dashboard page get success."""

    client.force_login(sample_user)
    r = client.get(reverse('dashboard'))

    assert r.status_code == 200
    assert b'<title>Secure Checklist | Dashboard</title>' in r.content

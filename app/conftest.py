import pytest

from django.contrib.auth import get_user_model


@pytest.fixture()
def sample_user():
    return get_user_model().objects.create(
        email='sample@example.com',
        password='test_pass_123',
        username='sample_user'
    )

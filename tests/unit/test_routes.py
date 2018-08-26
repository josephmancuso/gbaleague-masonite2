from masonite.testing import UnitTest
from app.User import User
import pytest
from orator.orm import Factory

class MockUser(User):
    id = 1

factory = Factory()

@factory.define(User)
def users_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email()
    }

class TestRoutes(UnitTest):

    def test_only_league_owner_can_view_requests(self):
        user = factory(User).make()
        user.id = 1
        assert self.get('/league/1/requests') \
            .user(user) \
            .status('200 OK')

    def test_not_league_owner_throws_exception(self):
        user = factory(User).make()

        with pytest.raises(Exception):
            self.get('/league/1/requests') \
                .user(user) \
                .status('200 OK')


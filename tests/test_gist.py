from pytest import raises
from blogist.gist import Gist, WrongUsername


def test_user_not_found():
    username = 'meiyouzhegeren'
    with raises(WrongUsername, match=f'{username} is not found in GitHub.'):
        g = Gist(username)

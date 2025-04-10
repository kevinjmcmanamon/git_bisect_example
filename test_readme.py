import pytest


class TestReadMe:

    def test_the_bug_does_not_appear_in_readme(self):
        with open('README.md') as readme:
            if 'THE BUG' in readme.read():
                pytest.fail("bug found")


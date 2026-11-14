import unittest
from app import app, home, about, changes, apiKey

class TestHome(unittest.TestCase):

    def test_home_returns_expected_value(self):
        with app.app_context():
            result = home()

            self.assertEqual(result.json, {
                'message': 'Welcome Hello world!',
                'status': 'success',
                'health check': 'OK',
            })

    def test_about_returns_expected_value(self):
        with app.app_context():
            result = about()

            self.assertEqual(result.json, {
        'name': 'Devarshi Nichite',
        'working': 'Jenkins Multipipeline Branch',
        'status': 'online',
        'branch': 'feature/test',
        'origin': 'main'
    })

    def test_changes_returns_expected_value(self):
        with app.app_context():
            result = changes()

            self.assertEqual(result.json, {
        'change': 'only change happen is this one on feature/branch',
        'visibility': 'if this is visible via pull request/merge request it means changes and pushes on all other files are visiblie excluding the Jenkinsfile in root directory'
    })

    def test_apiKey_returns_expected_value(self):
        with app.app_context():
            result = apiKey()

            self.assertEqual(result.json, [{
                'name': 'joe biden',
                'log': 'soddddaaaa',
                'status': 200
                },
                {
                    'name': 'doland trump',
                    'log': 'obamnaa',
                    'status': 200
                }])

if __name__ == '__main__':
    unittest.main()
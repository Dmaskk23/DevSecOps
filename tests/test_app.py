import unittest, time
from src.app import app

class TestCurrencyAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_convert_endpoint(self):
        start_time = time.time()
        response = self.app.get('/convert')
        duration = time.time() - start_time
        
        print(f'API Response time: {duration:.3f} seconds')
        
        # Перевіряємо чи затримка не більша за 1.5 секунди
        self.assertLess(duration, 1.5, 'API latency is too high!')
        
        # Перевіряємо статус код та вміст JSON
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'SUCCESS')
        self.assertIn('USD_to_UAH', response.json['data'])

if __name__ == '__main__':
    unittest.main()
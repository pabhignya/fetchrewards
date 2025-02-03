import unittest
import json
import uuid
from app import app  # Assuming your Flask app is named `app.py`

class FlaskAppTests(unittest.TestCase):
    # Set up the Flask test client
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_process_receipt_valid(self):
        # Sample valid receipt data for POST request
        receipt_data = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
      {
        "shortDescription": "Mountain Dew 12PK",
        "price": "6.49"
      },{
        "shortDescription": "Emils Cheese Pizza",
        "price": "12.25"
      },{
        "shortDescription": "Knorr Creamy Chicken",
        "price": "1.26"
      },{
        "shortDescription": "Doritos Nacho Cheese",
        "price": "3.35"
      },{
        "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
        "price": "12.00"
      }
    ],
    "total": "35.35"
  }
        # POST the data to the /receipts/process endpoint
        response = self.client.post('/receipts/process', json=receipt_data)
        
        # Check that the response status is 201 Created
        self.assertEqual(response.status_code, 201)

        # Parse the response JSON
        data = json.loads(response.data)

        # Ensure the response contains the ID
        self.assertIn('id', data)

        # Store the generated ID for later use
        receipt_id = data['id']

        # Ensure the ID is a valid UUID
        try:
            uuid.UUID(receipt_id)
        except ValueError:
            self.fail("Generated ID is not a valid UUID")

        # Now check the points for this receipt via the GET request
        response_points = self.client.get(f'/receipts/{receipt_id}/points')

        # Check if the points response status is 200 OK
        self.assertEqual(response_points.status_code, 200)

        # Parse the response JSON for points
        points_data = json.loads(response_points.data)

        # Ensure points are calculated correctly 
        self.assertIn('points', points_data)
        self.assertEqual(points_data['points'], 28) 

    def test_process_receipt_missing_data(self):
        # Send a POST request with no data
        response = self.client.post('/receipts/process', json={})
        
        # Check that the response status is 400 Bad Request
        self.assertEqual(response.status_code, 400)

        # Check if the response contains the error message
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'No data provided')

    def test_get_points_invalid_id(self):
        # Send a GET request with a non-existent receipt ID
        invalid_id = str(uuid.uuid4()) 
        response = self.client.get(f'/receipts/{invalid_id}/points')

        # Check that the response status is 404 Not Found
        self.assertEqual(response.status_code, 404)

        # Check the error message
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Receipt not found')  

if __name__ == '__main__':
    unittest.main()

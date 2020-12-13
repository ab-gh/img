from django.test import Client, TestCase
from .models import User, Image
import json


# Create your tests here.

class ApiTestCase(TestCase, Client):
    """
    Unit tests for API responses
    """
    def setUp(self):
        ## Test strings
        self.test = {}
        self.test['username'] = "testUser"
        self.test['title'] = "testTitle"
        self.test['content'] = "testContent"
        self.test['image'] = str.encode("testImage")

        ## Create test objects
        user = User.objects.create(username=self.test['username'])
        image = Image.objects.create(title=self.test['title'], content=self.test['content'], image=self.test['image'], user=user)

        ## Assign object IDs (should all be 1)
        self.test['user'] = user.id
        self.test['image_id'] = image.id

    def test_api(self):
        """
        Test HTTP responses for API
        """
        c = Client()

        ## /api/image response codes
        ## get image: OK
        self.assertEqual(c.get(f"/api/image/{self.test['image_id']}").status_code, 200)
        ## post, put, patch, image: MethodNotAllowed
        self.assertEqual(c.post(f"/api/image/{self.test['image_id']}").status_code, 405)
        self.assertEqual(c.put(f"/api/image/{self.test['image_id']}").status_code, 405)
        self.assertEqual(c.patch(f"/api/image/{self.test['image_id']}").status_code, 405)
        ## get image-1: NotFound
        self.assertEqual(c.get(f"/api/image/{self.test['image_id']-1}").status_code, 404)
        

    def test_image(self):
        """
        Test Image model
        """
        c = Client()

        ## get image
        response = c.get(f"/api/image/{self.test['image_id']}")
        data = json.loads(response.content)

        self.assertEqual(data['title'], self.test['title'])
        self.assertEqual(data['content'], self.test['content'])
        self.assertEqual(data['image'], self.test['image'].decode())
        self.assertEqual(data['user']['id'], self.test['user'])
        self.assertEqual(data['user']['username'], self.test['username'])
        


        

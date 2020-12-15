from django.test import Client, TestCase
from .models import User, Image
import json
import base64
import magic


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
        encoded = open("api/tests/decode.jpg", "rb")
        mime = magic.Magic(mime=True)
        self.test['mime'] = mime.from_file(encoded.name)
        self.test['image'] = f"data:{self.test['mime']};base64,{base64.b64encode(encoded.read()).decode('utf-8')}"

        ## Create test objects
        user = User.objects.create(username=self.test['username'])
        image = Image.objects.create(title=self.test['title'], content=self.test['content'], image=self.test['image'], mime=self.test['mime'], user=user)

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
        self.assertEqual(c.get(f"/api/images/{self.test['image_id']}").status_code, 200)
        ## post, put, patch, image: MethodNotAllowed
        self.assertEqual(c.post(f"/api/images/{self.test['image_id']}").status_code, 405)
        self.assertEqual(c.put(f"/api/images/{self.test['image_id']}").status_code, 405)
        self.assertEqual(c.patch(f"/api/images/{self.test['image_id']}").status_code, 405)
        ## get image-1: NotFound
        self.assertEqual(c.get(f"/api/images/{self.test['image_id']-1}").status_code, 404)
        

    def test_image(self):
        """
        Test Image model
        """
        c = Client()

        ## get image
        response = c.get(f"/api/images/{self.test['image_id']}")
        data = json.loads(response.content)
        decoded = open("api/tests/decode.jpg", "rb").read()
        self.assertEqual(data['title'], self.test['title'])
        self.assertEqual(data['content'], self.test['content'])
        self.assertEqual(base64.b64decode(data['image'].split(",")[1]), decoded)
        self.assertEqual(data['image'].split(",")[0], f"data:{self.test['mime']};base64")
        self.assertEqual(data['user']['id'], self.test['user'])
        self.assertEqual(data['user']['username'], self.test['username'])
        


        

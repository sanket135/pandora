from django.test import TestCase
from api.views import classifier, uploadpeople, companyemployees, persons
from api.models import User
import time
import json

# Create your tests here.

class PandoraTestCase(TestCase):
    def setUp(self):
        pass

    """
    def test_classifier(self):
        print("Starting Fruits and Vegetables Classifier Test...")

        #Change it to any names it will classify from world's database
        fruitlist = ['grapes','mango','banana','kiwi']
        vegetablelist = ['chilli','eggplant','peas','potato']

        for fruit in fruitlist:
            self.assertEqual(classifier(fruit), 'fruit')

        for vegetable in vegetablelist:
            self.assertEqual(classifier(vegetable), 'vegetable')
        print("Classifier Test Completed")
    
    

    def test_uploadpeople(self):
        print("Starting Upload People Data Test...")
        env = 'test'
        request = ''
        uploadpeople(None, env)
        time.sleep(7)
        users = User.objects.all()
        count = users.count()
        self.assertEqual(count, 3)
        print("Upload People Test Completed")
    """

    def test_persons(self):
        print("Starting Two People given Data Test...")
        env = 'test'
        request = ''
        uploadpeople(None, env)
        time.sleep(7)
        result = persons(None, persononename="Carmella0", persontwoname="Bonnie2")
        result = json.loads(result.content)
        print(result)
        expected = {'personone': {'id': 1, 'name': 'Carmella Lambert', 'age': 61, 'address': '628 Sumner Place, Sperryville, American Samoa, 9819', 'phone': '+1 (910) 567-3630'}, 'persontwo': {'id': 3, 'name': 'Bonnie Bass', 'age': 54, 'address': '455 Dictum Court, Nadine, Mississippi, 6499', 'phone': '+1 (823) 428-3710'}, 'friends': {2: {'id': 2, 'name': 'Decker Mckenzie', 'eyeColor': 'brown', 'has_died': False}}}
        self.assertEqual(json.dumps(result), json.dumps(expected))

    def test_companygiven(self):
        pass







from django.test import TestCase
from api.views import classifier, uploadpeople, companyemployees, persons

# Create your tests here.

class PandoraTestCase(TestCase):
    def setUp(self):
        pass

    def test_classifier(self):

        #Change it to any names it will classify from world's database
        fruitlist = ['grapes','mango','banana','kiwi']
        vegetablelist = ['chilli','eggplant','peas','potato']

        for fruit in fruitlist:
            self.assertEqual(classifier(fruit), 'fruit')

        for vegetable in vegetablelist:
            self.assertEqual(classifier(vegetable), 'vegetable')


    def test_persons(self):
        pass



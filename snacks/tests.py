from django.test import TestCase
  
from django.urls import reverse
# Create your tests here.
class snacksTests(TestCase):
    def test_snack_list_page_status(self):
            url = reverse('snack_list')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_snack_detail_page_status(self):
            url = reverse('snack_detail')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)        

    def test_snack_list_page_snack_list_template(self):
            url = reverse('snack_list')
            response = self.client.get(url)
            self.assertTemplateUsed(response, 'snack_list.html')
            self.assertTemplateUsed(response, 'base.html')
         
    def test_home_page_snack_detail_template(self):
            url = reverse('snack_detail')
            response = self.client.get(url)
            self.assertTemplateUsed(response, 'snack_detail.html')
            self.assertTemplateUsed(response, 'base.html')
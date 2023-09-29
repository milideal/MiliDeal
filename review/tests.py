from django.test import TestCase
from rest_framework.test import APIRequestFactory

from bson import json_util
import json

from user.models import User
from store.models import StoreModel
from review.models import Review


# Create your tests here.
class ReviewTestCase(TestCase):
    email = "test@test.com"
    nickname = "test"
    store_slug = "test-test"
    review_text = "test!"

    def test_create_review(self):

        store = StoreModel.objects.create(slug=self.store_slug)
        user = User.objects.create(email=self.email, nickname=self.nickname)
        review = Review.objects.create(
                review_of=store, 
                author=user,
                review=self.review_text, 
                score=3
            )
        review_id = review._id

        retrieved_review = Review.objects.get(pk=review_id)
        self.assertEqual(self.review_text, retrieved_review.review)

    def test_view(self):
        factory = APIRequestFactory()
        store = StoreModel.objects.create(slug=self.store_slug)
        user = User.objects.create()
        
        request = factory.post(
            "/review/", 
            {
                "review": self.review_text,
                "score": 2,
            }, 
            format='json'
        )

        

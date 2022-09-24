from django.test import TestCase
from .models import PersonModel


class Person(TestCase):
    def setUp(self) -> None:
        PersonModel.objects.create(name="qTich", age=22, address="Empty", work="Empty")

    def test_MPerson(self) -> None:
        for gobject in (
                PersonModel.objects.get(name="qTich"),
                PersonModel.objects.get(id=1),
        ):
            self.assertEqual(gobject.age, 22)
            self.assertEqual(gobject.address, "Empty")
            self.assertEqual(gobject.work, "Empty")

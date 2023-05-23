# Create your tests here.
from django.test import TestCase
from apps.university.models import OTM


class OTMTestCase(TestCase):
    def setUp(self):
        self.parent_otm = OTM.objects.create(title='Parent OTM', is_active=True)
        self.child_otm = OTM.objects.create(title='Child OTM', is_active=True, parent_category=self.parent_otm)

    def test_otm_fields(self):
        self.assertEqual(self.parent_otm.parent_category, None)
        self.assertEqual(self.parent_otm.title, 'Parent OTM')
        self.assertTrue(self.parent_otm.is_active)
        self.assertIsNotNone(self.parent_otm.date_created)

        self.assertEqual(self.child_otm.parent_category, self.parent_otm)
        self.assertEqual(self.child_otm.title, 'Child OTM')
        self.assertTrue(self.child_otm.is_active)
        self.assertIsNotNone(self.child_otm.date_created)

    def test_str_representation(self):
        expected_str = self.parent_otm.title
        self.assertEqual(str(self.parent_otm), expected_str)

    def test_children_relation(self):
        self.assertIn(self.child_otm, self.parent_otm.children.all())

    def test_limit_choices_to(self):
        self.assertEqual(OTM.objects.count(), 2)

        otm_without_parent = OTM.objects.create(title='OTM without parent', is_active=True)
        self.assertEqual(OTM.objects.count(), 3)

        otm_with_parent = OTM.objects.create(title='OTM with parent', is_active=True, parent_category=self.parent_otm)
        self.assertEqual(OTM.objects.count(), 4)

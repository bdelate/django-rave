# stdlib imports

# django imports
from django.test import TestCase

# 3rd party imports
from rest_framework.exceptions import ValidationError

# project imports
from djangorave.serializers import TransactionSerializer
from djangorave.tests.factories import PaymentMethodModelFactory, UserFactory


class TestTransactionSerializer(TestCase):
    """Test suite for the TransactionSerializer"""

    def test_validate_reference(self):
        """Ensure the serializer raises an exception for an invalid
        payment_method_id or user_id """
        payment_method = PaymentMethodModelFactory()
        user = UserFactory()

        expected_response = f"{payment_method.id}__test__{user.id}"
        actual_response = TransactionSerializer.validate_reference(
            self=None, value=expected_response
        )
        self.assertEqual(expected_response, actual_response)

        with self.assertRaises(ValidationError) as e:
            TransactionSerializer.validate_reference(
                self=None, value=f"123__test__{user.id}"
            )
        self.assertEqual(e.exception.detail[0], "Payment method does not exist")

        with self.assertRaises(ValidationError) as e:
            TransactionSerializer.validate_reference(
                self=None, value=f"{payment_method.id}__test__123"
            )
        self.assertEqual(e.exception.detail[0], "User does not exist")

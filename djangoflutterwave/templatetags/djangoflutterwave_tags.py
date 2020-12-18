# stdlib imports
import json

# django imports
from django.shortcuts import reverse
from django.utils import timezone
from django import template

# 3rd party imports

# project imports
from djangoflutterwave import settings


register = template.Library()


@register.simple_tag()
def pay_button_params(user_pk: str, plan_pk: str) -> str:
    """Returns params required when submitting a payment request to flutterwave.

    Returns:
        tx_ref: created by combining plan_pk, timestamp and user_pk
        redirect_url: transaction detail page to redirect to
        public_key: public key from settings
    """
    now = timezone.now().timestamp()
    tx_ref = f"{plan_pk}__{now}__{user_pk}"
    redirect_url = reverse(
        "djangoflutterwave:transaction_detail", kwargs={"tx_ref": tx_ref}
    )
    return json.dumps(
        {
            "tx_ref": tx_ref,
            "redirect_url": redirect_url,
            "public_key": settings.FLW_PUBLIC_KEY,
        }
    )

"""
Copyright (C) 2009-2010, Tay Ray Chuan

Please see LICENCE for licensing details.
"""

from livesettings import config_value
from payment.forms import PaymentContactInfoForm
from signals_ahoy.signals import form_init

from settings import *

def mark_shipping_fields(sender, form=None, **kwards):
    """
    Change with fields are made required by satchmo by default.

    Please read the README for more details.
    """

    def _make_field_required(field, name):
        field.required = True

        # Follow what satchmo does to indicate a field is required.
        field.label = (field.label or name) + '*'

    # Respect SHOP.REQUIRED_BILLING_DATA; in addition to satchmo
    for f in config_value('SHOP', 'REQUIRED_BILLING_DATA'):
        ship_label = "ship_%s" % f
        if not form.fields.has_key(ship_label):
            continue
        if not form.fields[ship_label].required:
            _make_field_required(form.fields[ship_label], f)

form_init.connect(mark_shipping_fields, sender=PaymentContactInfoForm)

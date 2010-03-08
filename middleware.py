"""
Copyright (C) 2009-2010, Tay Ray Chuan

Please see LICENCE for licensing details.
"""

from payment.views.contact import contact_info_view
from satchmo_store.shop.models import Cart
from settings import *

class AnonymousCheckoutMiddleware(object):
    """
    Hook onto payment.views.contact.contact_info_view() (which handles checkout
    step 1).

    All fields except shipping fields (`ship_<field>`) will be filled with dummy
    data. You can safely leave these fields out of your form template.

    (For whatever reason, you could probably use this for other subclasses
    of ContactInfoForm.)

    Please read the README for more details.
    """
    def process_view(self, request, view_func, view_args, view_kwargs):
        # is this a submit?
        if not request.method == 'POST' \
            or not view_func == contact_info_view:
            return None

        data = request.POST.copy()

        # fill in all billing and contact fields
        for f in BILLING_FIELDS + PERSONAL_FIELDS:
            data[f] = BLANK_DATA

        data['email'] = BLANK_EMAIL
        data['copy_address'] = False

        for f in BILLING_FIELDS:
            ship_label = 'ship_%s' % f
            if not data.has_key(ship_label):
                data[ship_label] = BLANK_DATA
            data[f] = data[ship_label]

        request.POST = data

        # continue processing please
        return None

"""
Copyright (C) 2009-2010, Tay Ray Chuan

Please see LICENCE for licensing details.
"""

# The bare minimum - needed to calculate shipping costs.
BILLING_FIELDS_REQUIRED = ('street1', 'city', 'country', 'postal_code')

# Satchmo thinks these are required, but we don't.
BILLING_FIELDS_OPTIONAL = ('addressee', 'street2', 'state')

BILLING_FIELDS = BILLING_FIELDS_REQUIRED + BILLING_FIELDS_OPTIONAL

# Contact details.
PERSONAL_FIELDS = ('first_name', 'last_name', 'email', 'phone')

Anonymous Checkout for Satchmo
==============================

Description
-----------

If you only want to collect enough information from your customer to start
shipping products, then this project may be useful for you.

Only shipping information is collected; for billing and contact information,
it is assumed that you will refer to your payment gateway of choice (see the
FAQ for more).

Usage
-----

#. Activate our middleware::

     MIDDLEWARE_CLASSES = (
       ...
       'satchmo_anon_checkout.middleware.AnonymousCheckoutMiddleware',
       ...
     )

   We're not really choosy about where you put the middleware specification.

#. Activate our signal listeners::

     INSTALLED_APPS = (
       ...
       'satchmo_anon_checkout',
       ...
     )

   There aren't any django-style models, so you don't have to bother running
   ``syncdb``.

#. Modify the template for step 1 of the checkout process; remove the contact
   form and the billing fields, the ship addressee, and the "copy address"
   field.

FAQ
---

How do I identify my customer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the customer doesn't fill in personal information, it isn't immediately
obvious how this is done. (A Contact object will still be created by satchmo,
but it will contain dummy info.)

When your payment gateway processes an order, Satchmo updates the order's
transaction ID. You can then use that to link an order to a customer.

Similarly, for billing information, you should refer to your payment gateway.
The billing info stored in Satchmo is simply a copy of the shipping information
entered at checkout-time.

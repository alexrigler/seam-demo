from datetime import datetime  # remember to handle datetimes in real world
import json
from pprint import pprint
from django.http import HttpResponse
from django.views.generic import View
from seam import Seam
from svix.webhooks import Webhook, WebhookVerificationError


DUMMY_DEVICE_ID = ""
DUMMY_ACCESS_CODE_ID = ""
DUMMY_SECRET = ""

with open("reservation.json") as reservation_payload:
    reservation_data = json.load(reservation_payload)


pprint(reservation_data)
# export SEAM_API_KEY=*** environment variable picked up here
# Seam will automatically use the SEAM_API_KEY environment variable if you don't provide an api_key to `Seam()`
seam = Seam()

# Retrieve all authroized locks and select the first lock.
# some_lock = seam.locks.list()[0]

# Inspect this device to see which capabilities it supports.
# print(some_lock.capabilities_supported)
# ['access_code', 'lock']

# This device supports the 'lock' capability, so you can use the Seam API to
# unlock the lock if it is locked or to lock it if it is unlcoked.
# if some_lock.properties["locked"]:
#     seam.locks.unlock_door(some_lock)
# else:
#     seam.locks.lock_door(some_lock)


def derive_available_code_from(tel=str) -> str:
    """
    consider phone number validation and that some devices won't accept a leading zero
    simple example to extract last four digits from provided telephone number
    """
    return tel[-4:]


# guest_access_code = derive_available_code_from(yessty_payload["guest_telephone"])

# create a time-bound access code that operates between a designated starts_at and ends_at time window,
# /access_codes/create

# seam.access_codes.create(
#     device_id=yessty_payload["listing_smart_lock_id"],
#     name="examplecode",
#     starts_at=yessty_payload["reservation_check_in"],
#     ends_at=yessty_payload["reservation_check_out"],
#     code=guest_access_code,
#     use_backup_access_code_pool=True,
# )

# my_device = seam.devices.list()[0]
# my_device.properties.supports_backup_access_code_pool

# list or get access codes
# access_code = seam.access_codes.get()

# print(
#     "Is backup access code available: "
#     + str(access_code.is_backup_access_code_available)
# )

# backup_code = seam.access_codes.pull_backup_access_code(access_code=DUMMY_ACCESS_CODE_ID)

# print(backup_code)

# def webhook_handler(request):
#     headers = request.headers
#     payload = request.body

#     try:
#         wh = Webhook(DUMMY_SECRET)
#         msg = wh.verify(payload, headers)
#     except WebhookVerificationError as e:
#         return HttpResponse(status=400)

#     # Do something with the message...

#     return HttpResponse(status=204)

# class SeamWebhookHandlers(View):
#     # /seam/access-code-webhook
#     def post(self, request, *args, **kwargs):
#         # code here
#         return HttpResponse(status=200)

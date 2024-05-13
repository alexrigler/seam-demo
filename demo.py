from datetime import datetime #remember to handle datetimes in real world
from seam import Seam


yessty_payload = {
    "guest_name": "Jane Doe",
    "guest_email": "jane@example.com",
    "guest_telephone": "+1 650-394-3042",
    "reservation_check_in": "01/08/24 16:00:00",
    "reservation_check_out": "01/12/24 12:00:00",
    "listing_name": "123 Main St",
    "listing_smart_lock_id": "abc-1234"
}


# Seam will automatically use the SEAM_API_KEY environment variable if you
# don't provide an api_key to `Seam()`
seam = Seam()

def derive_available_code_from(tel=str) -> str:
    """
    consider phone number validation and that some devices won't accept a leading zero
    simple example to extract last four digits from provided telephone number
    """
    return tel[-4:]

guest_access_code = derive_available_code_from(yessty_payload["guest_telephone"])

# create a time-bound access code that operates between a designated starts_at and ends_at time window,
# /access_codes/create

seam.access_codes.create(
    device_id=yessty_payload["listing_smart_lock_id"]
    name="examplecode"
    starts_at=yessty_payload["reservation_check_in"], 
    ends_at=yessty_payload["reservation_check_out"],
    code=guest_access_code,
    use_backup_access_code_pool = True
    )


# A backup access code pool is a collection of pre-programmed access codes stored on a device, ready for use. These codes are programmed in addition to the regular access codes on Seam, serving as a safety net for any issues with the primary codes.
# If there's ever a complication with a primary access code—be it due to intermittent connectivity, manual removal from a device, or provider outages—a backup code can be retrieved. Its end time can then be adjusted to align with the original code, facilitating seamless and uninterrupted access.
# To bulletproof your implementation of access codes, it's essential to maintain a pool of backup access codes for each device. Seam provides a robust implementation of this backup pool system, and this article will help you learn how to use our backup access pool system.


my_device = seam.devices.list()[0]
my_device.properties.supports_backup_access_code_pool


# list or get access codes

access_code = seam.access_codes.get("dc83d82d-55d2-4178-8c8c-10382311aed2")

pprint("Is backup access code available: " 
    + str(access_code.is_backup_access_code_available))

access_code_id = "dc83d82d-55d2-4178-8c8c-10382311aed2"

backup_code = seam.access_codes.pull_backup_access_code(
    access_code = access_code_id
)

pprint(backup_code)

# Warning: many_active_backup_codes

# Multiple back up codes have been pulled from the device. This usually indicates that Seam is having issues programming access codes onto the device. Check if the device is offline or if there are other issues.
# Warning: partial_backup_access_code_pool

# Seam is having trouble refilling the back up access code pool. This could result from device connection issues or from the device running out of space for new codes.
# Error: empty_backup_access_code_pool

# There are no more back up codes available in the pool. This can happen when you've just enabled the back up pool feature, or when all of the backup access codes have been used.


# When you request for a device to perform an action, the Seam API will immediately return an Action Attempt object. 
# In the background, the Seam API will perform the action.
# This Action Attempt allows you to keep track of the progress of your Action.

# If you require offline access codes https://docs.seam.co/latest/capability-guides/smart-locks/access-codes#offline-access-codes

# For locks that support setting codes with a schedule Seam will preload access codes 
# onto the device a full 72 hours before the starts_at timestamp of a Time Bound code.  

#  BACKUP CODES
# To confirm that Seam supports back up code pools for your device, 
# check the device's properties by inspecting the response from Get Device or List Devices. 
# Ensure that the device's properties.supports_backup_access_code_pool is true.


# is_backup_access_code_available





from django.http import HttpResponse
from svix.webhooks import Webhook, WebhookVerificationError

secret = "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw"

def webhook_handler(request):
    headers = request.headers
    payload = request.body

    try:
        wh = Webhook(secret)
        msg = wh.verify(payload, headers)
    except WebhookVerificationError as e:
        return HttpResponse(status=400)

    # Do something with the message...

    return HttpResponse(status=204)

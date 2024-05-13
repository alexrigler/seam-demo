# Show the exact API routes being used
# Show the important parameters being provided to the Seam API
# Show some of the side-effects of making API calls to Seam (e.g. Seam programming the
# code onto the device)
# Nice code sample formatting, including comments to help the customer understand the
# purpose of each item.

# Dummy Data
# Guest name: “Jane Doe”
# Guest email: “jane@example.com”
# Guest telephone number: 650-394-3042 ⇐ bonus: many guests prefer the last 4-digit of their phone to be their access code for a smart lock; 
# the Seam API has a request parameter to set an access code to whatever you’d like, assuming the device permits it
# Reservation check-in: 4pm, January 8th, 2024
# Reservation check-out: 12pm, January 12th, 2024
# Listing Name: “123 Main St”
# Listing Smart Lock ID: “abc-1234”

# bonus: many guests prefer the last 4-digit of their phone to be their access code for a smart lock; 
# the Seam API has a request parameter to set an access code to whatever you’d like, assuming the device permits it

# Endpoints
# /devices/list/
# /devices/get/ https://docs.seam.co/latest/api-clients/devices/get-device 
# /events/list/ https://docs.seam.co/latest/api-clients/events/list-events 


from seamapi import Seam
from django.http import HttpResponse
from django.views.generic import View

# export SEAM_API_KEY=*** environment variable picked up here

seam = Seam()

# Retrieve all authroized locks and select the first lock.
some_lock = seam.locks.list()[0]

# Inspect this device to see which capabilities it supports.
print(some_lock.capabilities_supported)
# ['access_code', 'lock']

# This device supports the 'lock' capability, so you can use the Seam API to
# unlock the lock if it is locked or to lock it if it is unlcoked.
if some_lock.properties["locked"]:
    seam.locks.unlock_door(some_lock)
else:
    seam.locks.lock_door(some_lock)    

    
    
    
class SeamWebhookHandlers(View):
    # /seam/access-code-webhook
    def post(self, request, *args, **kwargs):
        # code here
        return HttpResponse(status=200)
        

# Demo using the Seam API

1. Create a Seam account at https://console.seam.co See quickstart guide
2. You will start with a Sandbox workspace
3. Create a sandbox device. In this example we'll use Yale.



[Seam capability guide for smart locks](https://docs.seam.co/latest/capability-guides/smart-locks)

Understand the lifecycle of access codes. Side effects of Seam API
* [Create access codes](https://docs.seam.co/latest/capability-guides/smart-locks/access-codes/creating-access-codes)



## Task 1

Overview
Yessty is a property management software (“PMS”) that helps Airbnb hosts manage their listings. Yessty confirms incoming Airbnb reservations and automates sending guest check-in instructions such as house directions, wifi passwords,...etc. Yessty competes with other short-term rental PMSs such as Hostaway, Hospitable, and Guesty.

Recently, Hospitable, Guesty, and Hostaway all launched a direct integration with smart locks. They all use Seam and can now all issue unique smart lock access codes for each guest.

The PMS industry is very competitive and Yessty needs to respond quickly by also providing this smart lock integration feature into their PMS. To that end, they want to use Seam since it greatly simplifies the integration process with each brand of smart locks.

Bob, a long-time engineer at Yessty, has been chosen to implement Seam. But Bob is a little confused, overworked, and tired. So it looks like Bob will need a little help to understand how to implement Seam.

Bob (a Yessty engineer) has been tasked with implementing the programming of a smart lock access code for each Airbnb reservation. This access code is then communicated to the Airbnb guest for them to enter the house.

Importantly, this access code should only become active at the check-in time for the reservation and then become inactive at the check-out time. Bob also has to send this access code to the guest 48 hours before check-in time.

The best way to help Bob is to draw a simple request diagram that shows each request as well as code samples detailing each request in the language of your choice (python, javascript, ruby, php...etc). The parties in this request diagram should be the guest/Airbnb, Yessty’s server, Seam, and the smart lock. The code sample only needs to show requests made to Seam as well as the parameters.

In your request diagram, please show the following:
* The reservation information arriving from the guest/airbnb to the Yessty’s server
* Yessty’s server programming an access code via Seam onto the smart lock
* Yessty’s server sending this access code to the guest via email & sms 48 hours prior tothe check-in

In your code sample, please show the following:
* Importing and setting the Seam API key
* Issuing each request that match the request diagram
* You can submit everything in a single file with “//... later on” comments in between requests

Elements of a solid answer:
* Show the exact API routes being used
* Show the important parameters being provided to the Seam API
* Show some of the side-effects of making API calls to Seam (e.g. Seam programming the code onto the device)
* Nice code sample formatting, including comments to help the customer understand the purpose of each item.

## Task 2

Unfortunately, access codes can sometimes fail to program onto a smart lock. For example, the wifi network could be down. As a result, Seam is unable to communicate with the lock to program the access code.

An access code that failed to program can lead to a pretty unhappy Airbnb guest who, once at the front door, tries to enter the access code that Yessty sent them to no avail.

In order to avoid this situation, Seam not only provides webhook events indicating when Seam is unable to program an access code (access_code.failed_to_set_on_device) but also provides backup codes that are permanently on a lock and can be used as an emergency access solution.

Bob must implement this backup code logic in order to have a reliable access solution in case the primary access code fails to program. When a backup code is used, Bob must immediately email the guest to tell them to use the new backup code.

For this task, please update your prior request diagram to show the following:
* A webhook event coming from Seam 2 hours before the check-in time indicating the code has failed to program.
* Yessty server acknowledging the webhook and immediately issuing a request to Seam to request the backup code
* Yesstly server then sends the backup code to the guest to let them know to use that instead.

Set backup codes https://docs.seam.co/latest/capability-guides/smart-locks/access-codes/backup-access-codes

Events and webhooks
https://docs.seam.co/latest/api-clients/events
Svix docs https://docs.svix.com/

`access_code.failed_to_set_on_device event`
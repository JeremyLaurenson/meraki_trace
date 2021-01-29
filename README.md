# meraki_trace
Props to Stefano Giorcelli for the original, much more though out idea.

This is a PoC whereby this script polls "Meraki" for the local details of the client and extracts a MAC address.
It "prefers" Ethernet over Wifi
It then turns around at access a Meraki API to resolve which network/host this client is and opens a web browser to the Meraki dashboard for that particualr client.


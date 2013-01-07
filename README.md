## Installation

You can install **active-campaign-python** by downloading the source.

[Click here to download the source (.zip)](https://github.com/adulmec/active-campaign-python/zipball/master) which includes all dependencies.

`from includes.ActiveCampaign import ActiveCampaign`

Fill in your URL and API Key in the `includes/Config.py` file, and you are good to go!

## Example Usage

### includes/Config.py
`from includes.Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY`

### examples.py

<pre>
from includes.ActiveCampaign import ActiveCampaign
from includes.Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY

ac = ActiveCampaign(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY)
print ac.api('account/view')
</pre>

See our [examples file](https://github.com/adulmec/active-campaign-python/blob/master/examples.py) or the comments from files in **includes** folder  for more in-depth samples.

## Prerequisites

1. A valid ActiveCampaign **hosted** account (trial or paid).

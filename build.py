import requests

def get_build():
    """Just cleaned and made it understandable of what everyone use."""
    resp = requests.get("https://discord.com/login").text
    sentry = resp.split('/assets/sentry.')[1]
    splitted_sentry = sentry.split('"')[0]
    resp = requests.get("https://discord.com/assets/sentry.{}".format(splitted_sentry), headers={"accept-encoding": "identity"}).text
    return resp.split('("buildNumber",(e="')[1].split('",')[0]

print(get_build())

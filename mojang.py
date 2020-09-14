import base64
import json
import urllib.request

profile_api_url = 'http://local.elizium-group.ru/profile/getProfile.php?uuid='

# get player profile via Mojang's API
# the returned object is the first property ("textures") decoded
# may raise an error on failure
def get_player_profile(uuid):
    compact_uuid = uuid.replace('-', '')

    response_str = None

    with urllib.request.urlopen(profile_api_url + uuid) as response:
        response_str = response.read().decode()

    if response_str:
        response = json.loads(response_str)
        
        if 'name' in response:
            # get player name
            profile = { 'name': response['name'] }

            # get player skin URL
            try:
                dec = json.loads(base64.b64decode(response['properties'][0]['value']).decode())
                profile['skin'] = dec['textures']['SKIN']['url'][27:] # remove URL prefix: http://textures.minecraft.net/texture/
            except:
                profile['skin'] = False

            return profile
        else:
            print('unexpected Mojang API response for ' + profile_api_url + uuid + ':')
    else:
        print('empty Mojang API response for ' + profile_api_url + uuid)
    
    # failed
    return None
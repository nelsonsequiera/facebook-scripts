from apps.core.errors import AudienceException, ErrorDTO
from apps.core.errors import TimeoutException
from apps.core.models import PluginIdStore
from facebook_business.exceptions import FacebookRequestError


def test():
    action = 'create'
    level = 'campaign'
    hierarchy = level
    platform = 'facebook'
    info = None
    field = None
    try:
        raise TimeoutException(platform=platform, message="Timeout Exception", hierarchy=hierarchy)
    except Exception as error:
        print("* " * 25)
        print(error.platform)
        print(error.to_dto().to_json())
        print("* " * 25)
        print('Got Exception. Could not {action} {level}. Reason was: {reason}'.format(
            action=action,
            level=level,
            reason=error)
        )
        message = error
        print(message.to_dto().to_json())

    return message.to_dto()


resp = test()
print(resp)


asd = {
    'action': 'create',
    'errors': {},
    'extra': resp.to_json(),
    'level': 'campaign',
    'media_plan': 'a8cd68a7-4553-461a-9c45-06c944de8ec3',
    'pid': '53',
    'plugin_id': 9,
    'success': True,
    'system_id': '847bb626-d3b3-4cd6-88b2-9f8f1481465e'
}

result = PluginIdStore.objects.create(**asd)

import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)

DOMAIN = {
    'cooltweets': {
        'schema': {
            'text': {
                'type': 'string',
                'maxlength': 140,
            },
            'user': {
                'screen_name': {
                    'type': 'string'
                },
                'name': {
                    'type': 'string'
                }
            },
            'place': {
                'url': {
                    'type': 'string'
                },
                'name': {
                    'type': 'string'
                },
                'full_name': {
                    'type': 'string'
                }
            },
            'entities':{
              'hashtags': {
                  'type': 'string'
              }
            },
            'id': {
                'type': 'number',
                'unique': True
            },
            'screen_name': {
                'type': 'string'
            }
        }
    }
}

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
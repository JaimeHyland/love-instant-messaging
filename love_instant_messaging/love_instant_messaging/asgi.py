"""
ASGI config for love_instant_messaging project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter  # added for instant messaging
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'love_instant_messaging.settings')

django_asgi_app = get_asgi_application()  # modified for instant messaging

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app, 
    }
) # modifed for instant messaging

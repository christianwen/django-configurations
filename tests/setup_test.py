"""Used by tests to ensure logging is kept when calling setup() twice."""

try:
    from unittest import mock
except ImportError:
    from mock import mock

import configurations

print('setup_1')
configurations.setup()

with mock.patch('django.setup', side_effect=Exception('setup called twice')):
    print('setup_2')
    configurations.setup()

print('setup_done')

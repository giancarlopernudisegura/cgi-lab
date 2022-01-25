#!/usr/bin/env python3

import os
import json

print('Content-Type: text/html\n')
print()
env = dict(os.environ)
print(f'<p>User-Agent: {env["HTTP_USER_AGENT"]}</p>')

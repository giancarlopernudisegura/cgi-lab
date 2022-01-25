#!/usr/bin/env python3

import os
import json

print('Content-Type: application/json\n')
print(json.dumps(dict(os.environ)))

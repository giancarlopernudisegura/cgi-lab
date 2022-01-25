#!/usr/bin/env python

import os
import json

print('Content-Type: application/json\n')
print(json.dumps(dict(os.environ)))

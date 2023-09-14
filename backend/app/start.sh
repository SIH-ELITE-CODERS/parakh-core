#!/bin/bash

# curl --location 'http://primarydb:8091/pools/default/buckets/development' \
# --header 'Content-Type: application/x-www-form-urlencoded' \
# --header 'Authorization: Basic cm9vdDpyb290' \
# --data-urlencode 'name=development' \
# --data-urlencode 'ramQuota=512' \
# --data-urlencode 'bucketType=ephemeral'

# curl --location 'http://primarydb:8091/pools/default/buckets/development/scopes' \
# --header 'Content-Type: application/x-www-form-urlencoded' \
# --header 'Authorization: Basic cm9vdDpyb290' \
# --data-urlencode 'name=sih'

# curl --location 'http://primarydb:8091/pools/default/buckets/development/scopes/sih/collections' \
# --header 'Content-Type: application/x-www-form-urlencoded' \
# --header 'Authorization: Basic cm9vdDpyb290' \
# --data-urlencode 'name=users'

# curl --location 'http://primarydb:8093/query/service' \
# --header 'Content-Type: application/x-www-form-urlencoded' \
# --header 'Authorization: Basic cm9vdDpyb290' \
# --data-urlencode 'statement=CREATE PRIMARY INDEX idx_email ON users USING GSI'

uvicorn core.main:app --host 0.0.0.0 --port 80

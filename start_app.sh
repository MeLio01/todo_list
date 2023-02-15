#!/bin/bash

set -o errexit
set -o nounset

gunicorn -b :8000 manage:app
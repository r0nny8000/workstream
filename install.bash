#!/bin/bash

echo 'building and installing workstream'

poetry build
pip install dist/workstream-0.1.0.tar.gz
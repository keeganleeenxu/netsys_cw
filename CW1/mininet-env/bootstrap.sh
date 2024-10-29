#!/bin/bash

set -e

MININET_VERSION="tags/2.3.0"
# No upstream tags, so pinning to a specific commit on gar-experimental that
# supports python3 and appears stable since 2020.
POX_VERSION="5f82461e01f8822bd7336603b361bff4ffbd2380"

sudo apt-get update
sudo apt-get install -y python3 unzip net-tools arping
git clone https://github.com/mininet/mininet
(cd mininet && git checkout $MININET_VERSION)
sed -i '234s/git:/https:/' mininet/util/install.sh
mininet/util/install.sh -nfvp
(cd pox && git checkout $POX_VERSION)

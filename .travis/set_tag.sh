#!/usr/bin/env bash

if $TRAVIS_TAG; then
    $RAIDENVERSION=$TRAVIS_TAG
else
    DATE=$(date +%Y.%m.%d)
    $RAIDENVERSION="nightly-$DATE"
fi

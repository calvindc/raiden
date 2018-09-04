#!/usr/bin/env bash

if $TRAVIS_TAG; then
    $RAIDENVERSION=$result
else
    DATE=`date +%Y.%m.%d`
    $RAIDENVERSION="nightly-$DATE"
fi

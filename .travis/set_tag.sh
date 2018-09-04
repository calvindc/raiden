#!/usr/bin/env bash

if $TRAVIS_TAG; then
    $TRAVIS_TAG=$result
else
    DATE=`date +%Y.%m.%d`
    $TRAVIS_TAG="nightly-$DATE"
fi

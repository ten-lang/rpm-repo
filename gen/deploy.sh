#!/bin/sh
cd ..
cp gen/RPMS/*/*.rpm ./
createrepo -x "gen/*" -x "gen/*/*" -x "gen/*/*/*" .

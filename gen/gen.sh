#!/bin/sh
PRO=$1
URL=https://github.com/ten-lang/$PRO/
TAG=$(git ls-remote --tags $URL | awk '{ print $2 }' | sort -r | awk 'FNR == 1' | sed 's/.*\///')
VER=$(echo $TAG | sed 's/v//')
GEN=$(pwd)
LOG=$(cat rpm/$PRO/changelog.txt)
REL=$(cat rpm/$PRO/release.txt)

mkdir -p BUILD
mkdir -p BUILDROOT
mkdir -p SOURCE
mkdir -p RPMS
mkdir -p SRPMS
mkdir -p SPECS

SPEC=$(cat rpm/$PRO/template.spec)
SPEC=$(eval "echo \"$SPEC\"")
printf "%s" "$SPEC" > SPECS/$PRO-$VER-$REL.spec

rm -rf SOURCES/*
wget -O "SOURCES/$TAG.tar.gz" "$URL/archive/$TAG.tar.gz"
rpmbuild -bb -D "_topdir $(pwd)" --buildroot $(pwd)/BUILDROOT SPECS/$PRO-$VER-$REL.spec

rpm --addsign --define="_gpg_name ten-lang" RPMS/*/$PRO-$VER-$REL*.rpm

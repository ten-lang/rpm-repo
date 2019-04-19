#!/bin/sh
wget -O /etc/yum.repos.d/ten-lang.repo https://raw.githubusercontent.com/ten-lang/rpm-repo/master/ten-lang.repo
wget -O -  https://raw.githubusercontent.com/ten-lang/rpm-repo/master/ten-lang.pub | gpg --import
yum update

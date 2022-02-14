#!/bin/bash -x  
#
# SPDX-License-Identifier: GPL-3.0-or-later
# 
# PackageVerificationCode script to generate verification code
# https://spdx.github.io/spdx-spec/package-information/#79-package-verification-code-field

# Targetdir

tdir=$1
tempfile=$(mktemp tempf.XXX)
tempfile_1=$(mktemp tempf_1.XXX)

if [ -d "$tdir" ] ; then 
	sha1sum $tdir/* | egrep -v 'spdx|deb' | awk '{print $1}' | sort > $tempfile
	sed -z s/\\n//g $tempfile > $tempfile_1 
	sha1sum $tempfile_1 | awk '{print $1}' 
	rm -rf $tempfile
	rm -rf $tempfile_1
else
	echo "Provide target directory"
	exit
fi

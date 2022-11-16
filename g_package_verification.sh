#!/bin/bash  
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# FileCopyrightText: <text> 2022 Matthew Buchanan Astley (matthewbuchanan@astley.nl) </text>
#
# PackageVerificationCode script to generate verification code
# https://spdx.github.io/spdx-spec/package-information/#79-package-verification-code-field
# Targetdir

tdir=~/app/$1
tempfile=$(mktemp tempf.XXX)
tempfile_1=$(mktemp tempf_1.XXX)

if [ -d "$tdir" ] ; then 
	sha1sum $tdir/* 2>/dev/null | egrep -v 'spdx|deb' | awk '{print $1}' | sort > $tempfile
	sed -z s/\\n//g $tempfile > $tempfile_1 
	sha1sum $tempfile_1 | awk '{print $1}' 
	rm -rf $tempfile
	rm -rf $tempfile_1
else
	echo "Provide target directory"
	exit
fi

#!/bin/bash

#
# Remove any non-intel or virtualization PCI device ID
#

while read LINE; do
	if [ "${LINE:0:1}" == "#" ]; then
		echo "$LINE"
		X=0
	elif [ "${LINE:0:13}" == "pci:v00008086" ] || [ "${LINE:0:13}" == "pci:v00001AF4" ]; then
		echo "$LINE"
		X=1
	else
		if [ $X -eq 1 ]; then
			echo "$LINE"
			echo ""
			X=0
		fi
	fi
done < hwdb/20-pci-vendor-model.hwdb

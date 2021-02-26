#! /bin/sh

#####################################################
# Name: backup.sh
#
# Backs up the jugendstadtplan project folder,
# especially including the database and the uploaded
# images.
#
# Dependencies: tar, xz
#
# Usage: backup.sh -o /path/to/desired/backup
#
# License: AGPLv3
#
# Author: Till Mahlburg
######################################################

# Functions

usage () {
cat <<- EOF
usage: $(basename "$0") -h

<command description>

OPTIONS:
    -o <path to backup> sets the path the backup should be saved in
    -h shows this help
EOF
}

backup () {
	local path
	path="$1"
	tar -cf "${path%%/}/backup.tar.xz" .
}

# Main functionality. Evaluates the given arguments.

main () {
    while getopts "ho:" opt; do
        case $opt in
            h )     usage ;;
            o )	    backup "$2" ;;
            \? )    usage
                    exit 1 ;;
            esac
    done
    shift $((OPTIND - 1))
}
main "$@"

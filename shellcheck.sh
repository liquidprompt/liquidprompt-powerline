#!/bin/sh

# shellcheck shell=bash

# shellcheck disable=SC2093
exec shellcheck \
  --shell=bash \
  --exclude=SC2155 \
  --external-sources \
  "$0" # Include this script to get the below imports


. ./liquidprompt

. ./powerline.theme

# vim: ft=sh et sts=2 sw=2 tw=120

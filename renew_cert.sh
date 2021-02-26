#! /bin/sh

# Renews Let's-Encrypt-Certificate using certbot.
# Assumes nginx running as a systemd service.
# Requires root in most configurations

certbot renew --pre-hook "systemctl stop nginx" --post-hook "systemctl start nginx"

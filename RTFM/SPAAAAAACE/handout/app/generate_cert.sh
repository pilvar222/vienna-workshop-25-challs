#!/bin/bash

# Generate a private key
openssl genrsa -out cert.key 2048

# Generate a self-signed certificate
openssl req -new -x509 -key cert.key -out cert.crt -days 365 -subj "/C=US/ST=Space/L=Aperture/O=WheatleyLabs/OU=SpaceAdventure/CN=challenge"

echo "Self-signed certificate generated successfully!" 
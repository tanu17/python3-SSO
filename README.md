# python3-SSO

This is a minimal demo project for paypal sso using python3 and django based on the saml toolkit ( https://github.com/onelogin/python-saml )

To Dos Before using this plugin:
1. Obtain ssl certificate for https from your organization
2. Required details from organization for setup-
issuerid :https://<url of your app>
ACS URL :https://<url of your app>/saml/acs (or any url)
Attributes (to be sent back from Identity Provider): userid, firstname, lastname, email, country etc
Certificate : SSL certificate (not the public key, not private key but the certificate) you will receive a saml file (similar to SAMPLE_Dev-IDP-metadata.xml)
3.install django in a way to be able to run with https (you can either run django using runsslserver(django 1.9 +)module sslserver or using apache or nginx as reverse proxy) ref: https://github.com/teddziuba/django-sslserver
4.pip install python-saml (or using any other installation steps mentioned in https://github.com/onelogin/python-saml)
5. Make the following changes in settings.json:
x509cert :Copy the x509cert from the certificate file received from organization
privateKey : Copy the private key from the certificate file
idp : IDP root url
sp : change the entityId, assertionConsumerService urls as per ACS URL. Security settings in the file should remain unchanged especially "authnRequestsSigned": true
6. Django settings.py changes
Changes in the file BASE_DIR/demo/settings.py
DEBUG = True #change this in production
CSRF_TRUSTED_ORIGINS=["https://<idp root url>",'<idp root url>','https://<ACS URL>','<ACS URL>','<sp>']
3.ALLOWED_HOSTS=['"https://<idp root url>",'<idp root url>','https://<ACS URL>','<ACS URL>','<sp>']

How to run :
Keep valid certificate.cer and key.key Change the BASE_DIR/saml/settings.json as mentioned in above steps
Command python3 manage.py runsslserver 0.0.0.0:443 --certificate cert/certificate.cer --key cert/key.key

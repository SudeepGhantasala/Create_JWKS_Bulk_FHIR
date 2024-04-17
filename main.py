from jwcrypto import jwk as jwk_gen

key = jwk_gen.JWK.generate(kty='RSA', alg='RS384', size=2048, kid='1')
publickey = '{"keys": [' + key.export_public() + ']}'
privatekey = key.export_private()

# Write the JSON data to the file

publickeyfilename = ''
privatekeyfilename = ''

with open(publickeyfilename, 'w') as filetowriteto:
    # Write a string to the file
    filetowriteto.write(publickey)

with open(privatekeyfilename, 'w') as filetowritetotwo:
    # Write a string to the file
    filetowritetotwo.write(privatekey)

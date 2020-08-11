import requests
# from crypto.Cipher import AES

password = '625894'
offset = '0123456789ABCDEF'
token_16 = '38f80acd6e88e39d'


def get_key_by_web(pwd=password, token_b_16=token_16):
    aes_url = 'http://tool.chacuo.net/cryptaes'
    api_data = {'data': pwd, 'type': 'aes', 'arg': 'm=cbc_pad=pkcs5_block=128_p=' + token_b_16 + '_i=' + offset + '_o=0_s=gb2312_t=0'}
    ret = requests.post(data=api_data, url=aes_url)
    # print(ret.status_code)
    secret_pwd = ret.json()['data'][0]
    # print(secret_pwd)
    return secret_pwd


# print(get_key_by_web())


#
# class AESCipher:
#
#     def __init__(self, key):
#         self.key = key[0:16]
#         self.iv = "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"
#
#     def __pad(self, text):
#         text_length = len(text)
#         amount_to_pad = AES.block_size - (text_length % AES.block_size)
#         if amount_to_pad == 0:
#             amount_to_pad = AES.block_size
#         pad = chr(amount_to_pad)
#         return text + pad * amount_to_pad
#
#     def __unpad(self, text):
#         pad = ord(text[-1])
#         return text[:-pad]
#
#     def encrypt(self, raw):
#         raw = self.__pad(raw)
#         cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
#         return base64.b64encode(cipher.encrypt(raw))
#
#     def decrypt(self, enc):
#         enc = base64.b64decode(enc)
#         cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
#         return self.__unpad(cipher.decrypt(enc).decode("utf-8"))
#
#
# if __name__ == '__main__':
#     e = AESCipher('8ymWLWJzYA1MvLF8')
#     secret_data = "6860795567181583<REQDATA></REQDATA>242BB99CE386F2B1EA19CCCF606D20E2"
#     enc_str = e.encrypt(secret_data)
#     print('enc_str: ' + enc_str.decode())
#     dec_str = e.decrypt(enc_str)
#     print('dec str: ' + dec_str)

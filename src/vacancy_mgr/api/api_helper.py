"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils import timezone
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from lib.convert import *
from lib.functions import *
from company.models import Company


class ApiHelper:
    """APIヘルパークラス"""
    @staticmethod
    def get_key():
        """APIキーの取得"""
        company = Company.objects.get(pk=settings.COMPANY_ID)
        return ApiHelper.get_aes_encrypt(company.internal_api_key, company.api_key)

    @staticmethod
    def check_key(key: str):
        """APIキー確認"""
        ans = False
        company = Company.objects.get(pk=settings.COMPANY_ID)

        try:
            key = ApiHelper.get_aes_decrypt(key, company.api_key)
        except:
            key = None

        if company.internal_api_key == key:
            ans = True

        return ans

    @staticmethod
    def get_aes_encrypt(target, crypt_key):
        key = crypt_key.lower()[:16].encode("utf-8")
        iv = crypt_key.lower()[-16:].encode("utf-8")
        cipher = AES.new(key, AES.MODE_CBC, iv)
        data = pad(str(target).encode("utf-8"), AES.block_size)
        cipher_text = cipher.encrypt(data)
        return cipher_text.hex()

    @staticmethod
    def get_aes_decrypt(target, crypt_key):
        cipher_text = bytes.fromhex(target)
        key = crypt_key.lower()[:16].encode("utf-8")
        iv = crypt_key.lower()[-16:].encode("utf-8")
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size)
        return plain_text.decode()

    """
    暗号化アルゴリズムを3DESからAESに変更

    @staticmethod
    def get_3des_encrypt(target, crypt_key):
        key = crypt_key.lower()[:24].encode("utf-8")
        iv = crypt_key.lower()[-8:].encode("utf-8")
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        data = pad(str(target).encode("utf-8"), DES3.block_size)
        cipher_text = cipher.encrypt(data)
        return cipher_text.hex()

    @staticmethod
    def get_3des_decrypt(target, crypt_key):
        cipher_text = bytes.fromhex(target)
        key = crypt_key.lower()[:24].encode("utf-8")
        iv = crypt_key.lower()[-8:].encode("utf-8")
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        plain_text = unpad(cipher.decrypt(cipher_text), DES3.block_size)
        return plain_text.decode()
    
    """

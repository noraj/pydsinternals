#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*
import binascii

from dsinternals.common.data.hello.KeyCredential import KeyCredential
from dsinternals.common.data.DNWithBinary import DNWithBinary

import unittest


class TestCaseKeyCredential(unittest.TestCase):

    def test_key01(self):
        rawdnb = b"B:828:00020000200001293CDE5195FE34E2D6D7E385AE8E36EC0883CE457613458D679726E3DD8864C92000024042781613BB48B19CBEB46CD2EDB49C9FBADB5A6185DB01D1CCBBD32CF8EE591B0103525341310008000003000000000100000000000000000000010001CB56D3816B78DC0DB5BA3A766FFDA0E35902A8BD92EE38BCCA85A29838D4ADDB00BA2138D3BB89091CAC112D3DAE845E8A4DC4209DAA1357812996A2252C29B419DEC0C9EA38376F97AC1AB337868D42A534B135322045CAE9C5239E092FCA893173C64EAC11D470D0D88699D37CEE0D37C5B808328F9CB9DF432D9CCEAFABA97D276096522E17A60AEDEA41844D2AF6AF73E89326298F7A87F877856297500B97B1432F7A05BAA534734673B7B53F682D7E6C08D45BACE97BDB0392E44AA1BBD04DB646C53835A9C9BC5D9DE1A7EB5856079573B57E2E8CE652254765D8FD2ED9FD419D45529C00D81B7EDDD4BD5B8FAF2EA202ED8D9058591C016BB4F3E1E501000401010005001000064BA1D5AD9EE59242864067D70B9E9DC70200070100080008D5AF88AE717ED701080009D5AF88AE717ED701:CN=user2,CN=Users,DC=domain,DC=local"
        kc = KeyCredential.fromDNWithBinary(DNWithBinary.fromRawDNWithBinary(rawdnb))
        self.assertEqual(kc.verifyHash(), True)
        self.assertEqual(kc.Identifier, "KTzeUZX+NOLW1+OFro427AiDzkV2E0WNZ5cm492IZMk=")
        self.assertEqual(kc.KeyHash, binascii.unhexlify("4042781613bb48b19cbeb46cd2edb49c9fbadb5a6185db01d1ccbbd32cf8ee59"))

    def test_key02(self):
        rawdnb = b"B:828:000200002000010931771AA15D0D2C55F90085364F9105A8FF8EF5F7D29EAFB68D25FE9327BAA42000029B7190E48CCBF5985D4C9775B1CFB56BE4153CA99CE4DEE6AC4943EEEC5A86DD1B0103525341310008000003000000000100000000000000000000010001BC8830BAB8E09BF812656E00FA7EEB4D83CF710EB072C4F19F540537CD51756720537BFD157238E92567B68D68AD548758324FBA1FDEE0AA08D3ED9963D03EF9BB4BB8CB9158D7AA767F6BCF52912BDD7FA5C4D3EDBAB481885DC9F0F46C1AF79554128C103869DAFA0847229F59543A2F8AEAF538F30C5634C1B6C87F9F8CCD2E79241503C7754D23E66DA6BAF97CBD3BD4B7964D5FB7EAFEA70B8BB1AF9DB77319F6F9CF0EEBE16AF878A1038BF75CBC73B2E20D4A9F48D64236921D997924DD59E8951F9F6B3A813CEF78D8D386CD9FE1704E0A44F88F5E90265C07F0733143E173CBD4165E890F3B8AC533BF0A8BEBE66560BDB996C408472A33C9E2F87101000401010005001000061D1CC264E8B1894CB93691CFB32548CF0200070100080008ECFFF45A0F7FD701080009ECFFF45A0F7FD701:CN=user2,CN=Users,DC=domain,DC=local"
        kc = KeyCredential.fromDNWithBinary(DNWithBinary.fromRawDNWithBinary(rawdnb))
        self.assertEqual(kc.verifyHash(), True)
        self.assertEqual(kc.Identifier, "CTF3GqFdDSxV+QCFNk+RBaj/jvX30p6vto0l/pMnuqQ=")
        self.assertEqual(kc.KeyHash, binascii.unhexlify("9b7190e48ccbf5985d4c9775b1cfb56be4153ca99ce4dee6ac4943eeec5a86dd"))


if __name__ == '__main__':
    unittest.main()

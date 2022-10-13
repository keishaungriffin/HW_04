# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:32:11 2022

@author: keish
"""

import unittest

import unittest.mock as mock

from HW_04_Keishaun_Griffin_REST_based_APIs import GithubApi


class TestGithubAPI(unittest.TestCase):
    
    def testGithub(self):
        with mock.patch('HW_04_Keishaun_Griffin_REST_based_APIs.GithubAPI', create=True) as MockGithub:
            MockGithub.return_value = False
            self.assertEqual(MockGithub('?'), False)
    def testGithub2(self):
        with mock.patch('HW_04_Keishaun_Griffin_REST_based_APIs.GithubAPI', create=True) as MockGithub:
            MockGithub.return_value = True
            self.assertEqual(MockGithub('keishaungriffin'), True)
            
if __name__ == '__main__':
    unittest.main()

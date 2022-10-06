# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:32:11 2022

@author: keish
"""

import unittest

from HW_04_Keishaun_Griffin_REST_based_APIs import GithubApi


class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(GithubApi('?'), False)
    def testGithub2(self):
        self.assertEqual(GithubApi('keishaungriffin'), True)
       
if __name__ == '__main__':
    unittest.main()
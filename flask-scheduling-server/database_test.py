#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:37:56 2019

@author: joseph
"""

import unittest
#from app import app
from flaskApp import app
from app import db
#, db, bcrypt, UPLOAD_FOLDER
from models import Request
#import Scheduler
#import os
#import tempfile
#import pytest



class SomeTest(unittest.TestCase):

    
    def setUp(self):
        self.app = app.test_client()
    
    def tearDown(self):
            pass
        
    def test_getschedule(self):
        rv = self.app.get('/get-schedule', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
    
    def test_getrequests(self):
        rv = self.app.get('/get-requests', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
    
    
    def test_login(self):
        rv = self.app.post('/login', 
                           json={"user": "coord1","password": "12345"},
                           follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        #test fail
        rv = self.app.post('/login', 
                           json={"user": "coord1","password": "123456"},
                           follow_redirects=True)
        self.assertEqual(rv.status_code, 500)
        
    
    def test_add_request(self):
        rv = self.app.post('/add-request', 
                           json={"daySelect": "Monday",
                                "requester": "Natalie",
                                "startTime": "8am",
                                "endTime": "9am",
                                "reason": "lazy",
                                "status": False,
                                "weekly": False
                                 },
                           follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
    
    def test_get_color(self):
        rv = self.app.get('/get-course-colors', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
    
#    def test_gen_sched(self):
#        rv = self.app.get('/generate-schedule', follow_redirects=True)
#        self.assertEqual(rv.status_code, 200)
    
    def test_get_request(self):
        rv = self.app.get('/get-requests', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
    
    def test_satisfied(self):
        rv = self.app.post('/get-satisfied', 
                           json={"name": "David Yau"},
                           follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
    
    def test_del_request(self):
        rv = self.app.post('/del-request', 
                           json={"id": 10},
                           follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
    
    def test_approve_request(self):
        rv = self.app.post('/approve-request', 
                           json={"id": 9},
                           follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
    
    def test_404(self):
        rv = self.app.get('/other')
        self.assertEqual(rv.status, '404 NOT FOUND')

if __name__ == "__main__":
    unittest.main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:07:15 2019

@author: joseph
"""

from app import db
import sqlalchemy
class Account(db.Model):
    
    __tablename__ = 'Accounts'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    initials = db.Column(db.String)
    hash_pass = db.Column(sqlalchemy.types.LargeBinary)
    type = db.Column(db.String)

    __mapper_args__={
        'polymorphic_identity':'Accounts',
        'polymorphic_on':type
    }

    def __repr__(self):
        return "<Account(name='%s', initials='%s', hash_pass='%s')>" % ( self.name, self.initials, self.hash_pass)

    

class Professor(Account):
    __tablename__ = "Professors"
    id = db.Column(db.Integer,db.ForeignKey('Accounts.id'),primary_key=True)
    courses = db.relationship('Course',backref='Professors',lazy =True)

    courseclass_id= db.Column(db.Integer,db.ForeignKey("CourseClasses.id"),nullable=True)

    __mapper_args__={
        'polymorphic_identity':'Professors'
    }

    def __repr__(self):
        return "<Professor(name='%s', initials='%s', hash_pass='%s')>" % ( self.name, self.initials, self.hash_pass)


class CourseCoordinator(Account):
    __tablename__ = "CourseCoordinators"
    id = db.Column(db.Integer,db.ForeignKey('Accounts.id'),primary_key=True)

    __mapper_args__={
        'polymorphic_identity':'CourseCoordinators'
    }
    def __repr__(self):
        return "<CourseCoordinator(name='%s', initials='%s', hash_pass='%s')>" % ( self.name, self.initials, self.hash_pass)


class Course(db.Model):
    __tablename__ = "Courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
   
    professor_id = db.Column(db.Integer,db.ForeignKey("Professors.id"),nullable=True)
    courseclass_id= db.Column(db.Integer,db.ForeignKey("CourseClasses.id"),nullable=True)

    def __repr__(self):
        return "<Course(name='%s')>"%(self.name)

class Room(db.Model):
    __tablename__ = "Rooms"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer,nullable=False)
    roomType = db.Column(db.String,nullable=False)

    def __repr__(self):
        return "<Room(name='%s',size='%d',roomType='%s')>"%(self.name,self.size,self.roomType)

class StudentGroup(db.Model):
    __tablename__ = "StudentGroups"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer,nullable=False)
    
    #currently 1 to many relationships
    classes = db.relationship('CourseClass',backref='StudentGroups',lazy =True)
    
    #self.classes=classes??
    #db.Column(db.Integer,db.ForeignKey("CourseClasses.id"),nullable=False)

    def __repr__(self):
        return "<StudentGroup(name='%s',size='%s')>"%(self.name,self.size)

class CourseClass(db.Model):
    __tablename__ = "CourseClasses"
    id = db.Column(db.Integer, primary_key=True)
    courses = db.relationship('Course',backref='CourseClass',lazy =True)
    professorSize = db.Column(db.Integer,nullable=False)
    
    professors = db.relationship('Professor',backref='CourseClass',lazy =True)
    studentGroups_id = db.Column(db.Integer,db.ForeignKey("StudentGroups.id"),nullable=True)
    
    duration = db.Column(db.Integer,nullable=False)
    size = db.Column(db.Integer,nullable=False)
    classType = db.Column(db.String,nullable=False)
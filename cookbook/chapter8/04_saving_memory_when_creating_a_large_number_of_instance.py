#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:12:54 2018

@author: son
"""
## __dict__ vs __slots__ 
##single date : 428 bytes
##slots date : drop to 156 bytes
class Date:
#    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day, time):
        self.year = year
        self.month = month
        self.day = day
        self.time = time
    def __str__(self):
        return "year {} mon {} day {} time {}".format( self.year, self.month, self.day, self.time)
class Data:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return "year {} mon {} day {} time {}".format( self.year, self.month, self.day)
print(Date.__dict__)
print(Data.__slots__)

a = Date(1,1,1,1)
b = Date(2,2,2,2)
b.name = 'a'

print(a)
print(b)


    
##encapsulating names in a class

class A:
    def __init__(self):
        self._internal = 0
        self.public = 1
    def public_method(self):
        print(self.public)
        
    def _internal_method(self):
        print('not call')
        

class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        print(self.__private)
    
    def public_method(self):
        self.__private_method()
class C(B):
    def __init__(self):
        self.__private = 1
    def __private_method(self):
        print(self.__private)
    
    def public_method(self):
        self.__private_method()
        
print(dir(B()))
print()
print(dir(C()))
print()
print(dir(A()))

#creating managed attributes

class Person:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('excepted a string')
        self.__name = value
    @name.deleter
    def name(self):
        raise AttributeError("cant delete attribute")

son = Person('sjh')

print(son.name)
son.name = 'son'
print(son.name)
print(son.__dict__)
print()
print(dir(son))


#calling a method on a parent class

class SonJeongHo(Person):
    def __init__(self):
        super().__init__('sonjeongho')
        self.age = 32
class KimBeomSoo(Person):
    pass

class LeeSeongYoon(Person):
    @property
    def name(self):
        print("lee name")
        return super().name
    @name.setter
    def name(self, value):
        print('set name')
        super(LeeSeongYoon,LeeSeongYoon).name.__set__(self,value)
    @name.deleter
    def name(self):
        print('del')
        super(LeeSeongYoon,LeeSeongYoon).name.__delete__(self)
    
        

s = SonJeongHo()
k = KimBeomSoo('beomsoo')
l = LeeSeongYoon('Lee Seong Yoon')
print(s.name)
print(k.name)
print(l.name)
#creating a new kind of class or instance attribute


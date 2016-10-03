#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 23:56:33
# *************************************************************************
from maple import db


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.Text)
    name = db.Column(db.Text)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    content = db.Column(db.Text)

    def __init__(self, tag, name, title, author, content):
        self.name = name
        self.tag = tag
        self.title = title
        self.author = author
        self.content = content

    def __repr__(self):
        return '<Books %r>' % self.name

    @classmethod
    def get_book_list(cls, page=1, filter_dict=dict()):
        if not filter_dict:
            return cls.query.paginate(page, 18, True)
        return cls.query.filter_by(**filter_dict).paginate(page, 18, True)

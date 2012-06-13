#!/usr/bin/env python

import os
from liquidluck.options import g
from liquidluck.writers.base import BaseWriter, Pagination


class YearWriter(BaseWriter):
    _posts = {}

    def __init__(self):
        self._template = self.get('year_template', 'archive.html')

        for post in g.public_posts:
            if post.date.year not in self._posts:
                self._posts[post.date.year] = [post]
            else:
                self._posts[post.date.year].append(post)

        g.resource['year'] = self._posts

    def start(self):
        for year in self._posts:
            self._write_posts(year)

    def _write_posts(self, year):
        posts = self._posts[year]
        pagination = Pagination(posts, 1, self.perpage)
        pagination.title = year

        dest = os.path.join(g.output_directory, str(year), 'index.html')
        self.render({'pagination': pagination}, self._template, dest)

        if pagination.pages < 2:
            return

        for page in range(1, pagination.pages + 1):
            dest = os.path.join(
                g.output_directory, str(year), 'page/%s.html' % page
            )
            pagination = Pagination(posts, page, self.perpage)
            pagination.title = year
            self.render({'pagination': pagination}, self._template, dest)


class TagWriter(BaseWriter):
    _posts = {}

    def __init__(self):
        self._template = self.get('tag_template', 'archive.html')

        for post in g.public_posts:
            for tag in post.tags:
                if tag not in self._posts:
                    self._posts[tag] = [post]
                else:
                    self._posts[tag].append(post)

        g.resource['tag'] = self._posts

    def start(self):
        for tag in self._posts:
            self._write_posts(tag)

    def _write_posts(self, tag):
        posts = self._posts[tag]
        pagination = Pagination(posts, 1, self.perpage)
        pagination.title = tag

        dest = os.path.join(g.output_directory, 'tags', tag, 'index.html')
        self.render({'pagination': pagination}, self._template, dest)

        if pagination.pages < 2:
            return

        for page in range(1, pagination.pages + 1):
            dest = os.path.join(
                g.output_directory, 'tags', tag, 'page/%s.html' % page)
            pagination = Pagination(posts, page, self.perpage)
            pagination.title = tag
            self.render({'pagination': pagination}, self._template, dest)


class CategoryWriter(BaseWriter):
    _posts = {}

    def __init__(self):
        self._template = self.get('category_template', 'archive.html')

        for post in g.public_posts:
            if post.category:
                if post.category not in self._posts:
                    self._posts[post.category] = [post]
                else:
                    self._posts[post.category].append(post)

        g.resource['category'] = self._posts

    def start(self):
        for category in self._posts:
            self._write_posts(category)

    def _write_posts(self, category):
        posts = self._posts[category]
        pagination = Pagination(posts, 1, self.perpage)
        pagination.title = category

        dest = os.path.join(g.output_directory, category, 'index.html')
        self.render({'pagination': pagination}, self._template, dest)

        if pagination.pages < 2:
            return

        for page in range(1, pagination.pages + 1):
            dest = os.path.join(
                g.output_directory, category, 'page/%s.html' % page)
            pagination = Pagination(posts, page, self.perpage)
            pagination.title = category
            self.render({'pagination': pagination}, self._template, dest)

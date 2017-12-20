"""
ASIA - A tool for the semantic enrichment of data available in tabular formats
Copyright (C) 2017  Vincenzo Cutrona

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class AbstatSuggestion:
    def __init__(self, suggestion=None, dataset=None, frequency=None, namespace=None):
        self.suggestion = suggestion
        self.dataset = dataset
        self.frequency = frequency
        self.namespace = namespace

    def __str__(self):
        return '%s %s %s %f' % (self.suggestion, self.namespace, self.dataset, self.frequency)


class AbstatDataset:
    def __init__(self, uri):
        self.uri = uri

    def __str__(self):
        return '%s' % (self.uri)
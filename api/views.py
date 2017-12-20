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

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from abstat import AbstatWrapper
from serializers import AbstatSuggestionSerializer, AbstatDatasetSerializer


class MissingParameterException(APIException):
    status_code = 400
    default_detail = '"query" and/or "position" parameters are missing.'
    default_code = 'missing_parameter'

class NotValidPositionException(APIException):
    status_code = 400
    default_detail = 'Invalid "position". It should be one of "subj", "obj" or "pred".'
    default_code = 'not_valid_position'

class QueryTooShortException(APIException):
    status_code = 400
    default_detail = '"query" parameters must contain at least 2 characters.'
    default_code = 'query_too_short'


# Create your views here.
class AbstatSuggestionsList(APIView):
    serializer_class = AbstatSuggestionSerializer

    def get(self, request):
        aw = AbstatWrapper()
        q_string = request.query_params.get('query', None)
        q_position = request.query_params.get('position', None)
        rows = request.query_params.get('rows', 10)
        start = request.query_params.get('start', 0)

        if q_string is None or q_position is None:
            raise MissingParameterException
        if len(q_string) < 2:
            raise QueryTooShortException
        if q_position not in AbstatWrapper.POSITIONS:
            raise NotValidPositionException

        suggestions = aw.get_syntactic_suggestions(q_string, q_position, rows, start)

        serializer = AbstatSuggestionSerializer(suggestions, many=True)
        return Response(serializer.data)

class AbstatDatasetsList(APIView):
    serializer_class = AbstatDatasetSerializer

    def get(self, request):
        aw = AbstatWrapper()

        datasets = aw.get_datasets()

        serializer = AbstatDatasetSerializer(datasets, many=True)
        return Response(serializer.data)
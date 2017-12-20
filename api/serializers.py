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
from rest_framework import serializers


class AbstatSuggestionSerializer(serializers.Serializer):
    suggestion = serializers.CharField(max_length=100)
    dataset = serializers.CharField(max_length=100)
    frequency = serializers.IntegerField(default=0)
    namespace = serializers.CharField(max_length=100)

class AbstatDatasetSerializer(serializers.Serializer):
    uri = serializers.CharField(max_length=100)
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
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^suggestions/abstatSyntactic$', views.AbstatSuggestionsList.as_view()),
    url(r'^suggestions/abstatDatasets$', views.AbstatDatasetsList.as_view())
]
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
import requests
from asia.settings import ABSTAT_API_PREFIX
from models import AbstatSuggestion, AbstatDataset

class AbstatWrapper:

    POSITIONS = ['subj', 'obj', 'pred']

    def get_syntactic_suggestions(self, query, position, rows = 10, start = 0):

        assert position in self.POSITIONS, 'Invalid position. It should be one of "subj", "obj" or "pred".'

        uri = ABSTAT_API_PREFIX + 'SolrSuggestions'
        payload = {'qString': query, 'qPosition': position, 'rows': rows, 'start': start}

        r = requests.get(uri, params=payload)

        if r.status_code == 404:  # No suggestions found
            return []
        if r.status_code == 200:
            return [AbstatSuggestion(suggestion=x['suggestion'],
                                            dataset=x['dataset'],
                                            frequency=x['occurrence'])
                           for x in r.json()['suggestions']]
        # Server error
        return None

    def get_datasets(self):
        uri = ABSTAT_API_PREFIX + 'datasets'
        r = requests.get(uri)
        if r.status_code == 200:
            return [AbstatDataset(uri=x['URI'])
                    for x in r.json()['datasets']]
        return None

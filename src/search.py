from decimal import Decimal
import json
import re
from time import time

from falcon import HTTPBadRequest, Response, Request
from Levenshtein import jaro, jaro_winkler, ratio
from redis.commands.search.query import Query

from clients import REDIS

MOVIE = REDIS.ft('idx:movie')
PERSON = REDIS.ft('idx:person')
SERIES = REDIS.ft('idx:series')


class Search:
    def on_post(self, req: Request, res: Response):
        query = req.params.get("query", None)
        if query is None:
            raise HTTPBadRequest(description="missing search term")

        result = self.search(query)

        res.body = json.dumps(result, indent=4, sort_keys=True)

    @staticmethod
    def normalize_string(the_string: str) -> str:
        the_string = the_string.lower()
        the_string = re.sub('\W', '', the_string)

        return the_string

    @staticmethod
    def fuzzy_string(the_string: str) -> str:
        if ' ' in the_string:
            ret = ''
            for word in the_string.split(' '):
                if word in ('the', 'a', 'of'):
                    continue

                ret += f"%{word}%"
        else:
            ret = f"%{the_string}%"

        return ret

    def search(self, query_string) -> dict:
        ret = {
            'movies': [],
            'series': [],
            'persons': []
        }
        _fuzzy_query = self.fuzzy_string(query_string)
        _query_string = self.normalize_string(query_string)

        query = Query(_fuzzy_query)
        query._offset = 0
        query._num = 100

        movies = []
        movies_result = MOVIE.search(query=query)
        for movie in movies_result.docs:
            _title = self.normalize_string(movie['original_title'])
            _jw_score = jaro_winkler(_query_string, _title)
            _popularity_score = float(Decimal(_jw_score) * Decimal(movie['popularity']))
            setattr(movie, '_score', _jw_score)
            setattr(movie, '_popularity', _popularity_score)
            movies.append(movie.__dict__)

        movies.sort(key=lambda x: x['_score'], reverse=True)
        ret['movies'] = movies[0:10]

        series = []
        series_results = SERIES.search(query=query)
        for serie in series_results.docs:
            _title = self.normalize_string(serie['original_name'])
            _jw_score = jaro_winkler(_query_string, _title)
            _popularity_score = float(Decimal(_jw_score) * Decimal(serie['popularity']))
            setattr(serie, '_score', _jw_score)
            setattr(serie, '_popularity', _popularity_score)
            series.append(serie.__dict__)

        series.sort(key=lambda x: x['_score'], reverse=True)
        ret['series'] = series[0:10]

        persons = []
        persons_results = PERSON.search(query=query)
        for person in persons_results.docs:
            _name = self.normalize_string(person['name'])
            _jw_score = jaro_winkler(_query_string, _name)
            _popularity_score = float(Decimal(_jw_score) * Decimal(person['popularity']))
            setattr(person, '_score', _jw_score)
            setattr(person, '_popularity', _popularity_score)
            persons.append(person.__dict__)

        persons.sort(key=lambda x: x['_score'], reverse=True)
        ret['persons'] = persons[0:10]

        return ret

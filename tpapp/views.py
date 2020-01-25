# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from tpapp.serializers import TpAppSerializer
from tpapp.models import AppData


class ListCreateRecords(ListCreateAPIView):
    serializer_class = TpAppSerializer

    def get_queryset(self):
        # If no search string passed in url returns all posts in reverse chronological order by year only, not months
        if not self.request.query_params.get('search', None):
            return AppData.objects.order_by('year').reverse()

        # If string passed in url is <   search  >    : searches year field using search parameter
        query_param = self.request.query_params['search']
        queryset = AppData.objects.filter(Q(year=query_param))
        return queryset

        # If strings passed in url are <  start  > and <  end>   : filter records by range of years
        # year_start = self.request.query_params['start']
        #         # year_end = self.request.query_params['end']
        #         # queryset = AppData.objects.filter(year=year_start, year=year_end)
        #         # return queryset


class ListCreateRecordsMonth(ListCreateAPIView):
    serializer_class = TpAppSerializer

    def get_queryset(self):
        # If search string passed in url searches month field
        query_param = self.request.query_params['search']
        queryset = AppData.objects.filter(Q(month=query_param))
        return queryset


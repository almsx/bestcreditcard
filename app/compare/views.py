#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import requests
import delorean
from delorean import stops

from django.http import (HttpResponseRedirect, HttpResponse)
from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse

from forms import Formulary

class Index(View):
	def get(self, request, *args, **kwargs):
		return render(request, "index.html")

class Form(View):
	def get(self, request):
		return HttpResponseRedirect(reverse('index'))
	def post(self, request, *args, **kwargs):
		serializer = Formulary(data=request.POST)
		response = []
		if serializer.is_valid():
			url = # Get credit card info
			cc_detail = requests.get(url).json()

			balance = float(serializer.data.get('balance'))
			CAT = cc_detail.get('cat')
			CAT_per_month = CAT / 12

			d1 = datetime.datetime(2015,01,01)
			d2 = datetime.datetime(2015,02,10)

			for i,stop in enumerate(stops(freq=delorean.DAILY, count=31, timezone="America/Mexico_City", start=d1, stop=d2)):
				balance_tax = round(((float(balance))/31) * (CAT_per_month/100) , 2)
				response.append({
						'balance': balance,
						'day': i+1,
						'balance_tax': balance_tax
					})
				balance += balance_tax

			return render(request, "result.html", {"data":response,
				"cc_image":cc_detail.get('card_image'),
				"name":cc_detail.get('name'),
				"cat":cc_detail.get('cat'),
				"annuity":cc_detail.get('annuity'),
				"currency":cc_detail.get('currency'),
				})

		else:
			return HttpResponse(serializer.errors)
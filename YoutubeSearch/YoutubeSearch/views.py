from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductList(APIView):
	def get(self,request):
		page = request.GET.get('page')

		cat_filter=Product.objects.filter()
		serializer = ProductSerializer(product_list,many = True)

		return Response(serializer.data)
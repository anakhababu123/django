from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from api.models import Products,Reviews,Carts
from api.serializers import ProductSerializer,ProductModelSerializer,ReviewSerializers,CartSerializers
from rest_framework.decorators import action
from rest_framework import authentication,permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin


class ProductsView(ModelViewSet):
    serializer_class=ProductModelSerializer
    queryset=Products.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
#     def list(self,request,*args, **kwargs):
#         qs=Products.objects.all()
#         serializer=ProductModelSerializer(qs,many=True)
#         return Response(data=serializer.data)
    
#     def create(self,request,*args, **kwargs):
#         serializer=ProductModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             Products.objects.create(**serializer.validated_data)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.error)
        
#     def retrieve(self,request,*args, **kwargs):
#         id=kwargs.get("pk")
#         qs=Products.objects.get(id=id)
#         serializer=ProductModelSerializer(qs)
#         return Response(data=serializer.data)
    
#     def update(self,request,*args, **kwargs):
#         id=kwargs.get("pk")
#         obj=Products.objects.get(id=id)
#         serializer=ProductModelSerializer(data=request.data,instance=obj)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
   
#     def destroy(self,request,*args, **kwargs):
#         id=kwargs.get("pk")
#         Products.objects.get(id=id).delete()
#         return Response(data="deleted")

    @action(methods=["get"],detail=False)
    def categories(self,request,*args,**kwargs):
        qs=Products.objects.values_list('category',flat=True)
        print(qs)
        categories=Products.objects.values_list("category",flat=True).distinct()
        return Response(data=categories)

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args, **kwargs):
        user=request.user
        product=self.get_object()
        serializer=ReviewSerializers(data=request.data,context={"user":user,"product":product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["get"],detail=True)
    def reviews(self,request,*args,**kwargs):
        product=self.get_object()
        qs=Reviews.objects.filter(product=product)
        serializer=ReviewSerializers(qs,many=True)
        return Response(data=serializer.data)



    @action(methods=["post"],detail=True)
    def addto_cart(self,request,*args, **kwargs):
        product=self.get_object()
        user=request.user
        serializer=CartSerializers(data=request.data,context={"product":product,"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class CartsView(GenericViewSet,ListModelMixin):
    serializer_class=CartSerializers
    queryset=Carts.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)
    





    



    



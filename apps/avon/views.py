from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DeleteView,View,ListView
from .models import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import *
# Create your views here.



class IndexView(ListView):
	template_name='avon/index.html'

	def get_queryset(self):
		return Campaing.objects.all()


class ListCustomers(ListView):
	template_name='avon/customer_list.html'

	def get_queryset(self):
		return Customer.objects.all().order_by('-debt')

class DetailCustomer(View):
	template_name='avon/detail_customer.html'

	def get(self,request):
		context={'object_list':Customer.objects.all()}
		return render(request,self.template_name,context)

class DetailCustomerResult(TemplateView):

	def get(self,request,*args,**kwargs):
		data=dict()
		id_customer=request.GET['id']
		request.session['id_customer']=id_customer
		customer=Customer.objects.get(pk=id_customer)
		articles=Article.objects.filter(buyer=customer)
		total=0
		for a in articles:
			total+=a.price
		print('TOTAL: ${}<<<<<<<<<'.format(total))
		context={
			'object_list':articles,
			'debt':customer.debt,
			'total':total,
			'is_owed':(True if customer.debt > 0 else False),
		}
		print('IS_OWED::::{}'.format(context['is_owed']))
		data['html_result']=render_to_string('avon/partial_html_result.html',context)
		return JsonResponse(data)


def CustomerUpdate(request,id_customer):
	instance=Customer.objects.get(pk=id_customer)
	data=dict()
	if request.method=='POST':
		form=UpdateCustomer(request.POST,instance=instance)
		form.save()
		data['form_is_valid']=True
		customer=Customer.objects.get(pk=id_customer)
		articles=Article.objects.filter(buyer=customer)
		total=0
		for a in articles:
			total+=a.price
		context={
			'object_list':articles,
			'debt':customer.debt,
			'total':total,
			'is_owed':(True if customer.debt > 0 else False),
		}
		data['html_campaings_list']=render_to_string('avon/partial_html_result.html',context)
	else:
		form=UpdateCustomer(instance=instance)
		data['form_is_valid']=False
	context={'form':form}
	data['html_form']=render_to_string('avon/partial_customer_form.html',context,request=request)
	return JsonResponse(data)


def save_form(request,form,template_name,template_list,Object):
	data=dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid']=True
			campaings=Object.objects.all()
			data['html_campaings_list']=render_to_string('avon/{}.html'.format(template_list),{'object_list':campaings})
		else:
			data['form_is_valid']=False
	context={'form':form}
	data['html_form']=render_to_string('avon/{}.html'.format(template_name),context,request=request)
	return JsonResponse(data)

def save_article_form(request,form,template_name,template_list,Object):
	data=dict()
	if request.method == 'POST':
		if form.is_valid():
			article=form.save(commit=False)
			campaing=Campaing.objects.get(pk=request.session['id'])
			article.campaing=campaing
			article.save()
			##SAVE MANY TO MANY
			form.save_m2m()
			customers=list(str(value) for value in article.buyer.all())
			print('BUYER:::::::'+str(customers))
			addDebt(customers,article.price)
			data['form_is_valid']=True
			object_list=Object.objects.filter(campaing=campaing)
			data['html_campaings_list']=render_to_string('avon/{}.html'.format(template_list),{'object_list':object_list})
		else:
			data['form_is_valid']=False
	context={'form':form}
	data['html_form']=render_to_string('avon/{}.html'.format(template_name),context,request=request)
	return JsonResponse(data)


def addDebt(customers,price):
	for customer in customers:
		c=Customer.objects.get(name=customer)
		c.debt+=price
		c.save()

def delete_object(request,obj,Object,template_list,template_delete,op):
	data=dict()
	if request.method=='POST':
		obj.delete()
		data['form_is_valid']=True
		objects=Object.objects.all() if op == 1 else Object.objects.filter(campaing=Campaing.objects.get(pk=request.session['id']))
		data['html_campaings_list']=render_to_string('avon/{}.html'.format(template_list),{'object_list': objects})
	else:
		context={'object':obj}
		data['html_form']=render_to_string('avon/{}.html'.format(template_delete),context,request=request)
	return JsonResponse(data)

def campaing_delete(request,pk):
	campaing=get_object_or_404(Campaing,pk=pk)
	return delete_object(request,campaing,Campaing,'partial_list','partial_campaing_delete',1)



def campaing_create(request):
	if request.method =='POST':
		form=CampaingForm(request.POST)
	else:
		form=CampaingForm()
	return save_form(request,form,'partial_campaing_create','partial_list',Campaing)


def campaing_update(request,pk):
	campaing=Campaing.objects.get(pk=pk)
	if request.method=='POST':
		form=CampaingUpdateForm(request.POST,instance=campaing)
	else:
		form=CampaingUpdateForm(instance=campaing)
	return save_form(request,form,'partial_campaing_update','partial_list',Campaing)

#AJAX TEST
def ajax_list(request):
	return render(request,'avon/ajax_test.html')



def campaing_detail(request,pk):
	campaing=get_object_or_404(Campaing,pk=pk)
	request.session['id']=pk
	articles=Article.objects.filter(campaing=campaing)
	return render(request,'avon/campaing_detail.html',{"object_list":articles})

def article_create(request):
	if request.method=='POST':
		form=ArticleForm(request.POST)
	else:
		form=ArticleForm()
	return save_article_form(request,form,'partial_article_create','partial_article_list',Article)

def article_delete(request,id_art):
	article=get_object_or_404(Article,pk=id_art)
	return delete_object(request,article,Article,'partial_article_list','partial_article_delete',2)


def create_customer(request):
	data=dict()
	if request.method=='POST':
		form=CustomerForm(request.POST)
		form.save()
		data['form_is_valid']=True
		context={'object_list':Customer.objects.all()}
		print(context)
		data['options']=render_to_string('avon/partial_options.html',context)

	else:
		data['form_is_valid']=False
		form=CustomerForm()
	data['html_form']=render_to_string('avon/partial_customer_form_.html',{'form':form},request=request)
	return JsonResponse(data)

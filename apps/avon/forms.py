from django import forms
from .models import Campaing,Article,Customer
from django.conf import settings




class UpdateCustomer(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(UpdateCustomer,self).__init__(*args,**kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs['class']='form__field'

	class Meta:
		model=Customer
		exclude=['name']
		labels={'debt':'Cuenta'}


class CustomerForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(CustomerForm,self).__init__(*args,**kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs['class']='form__field'
			self.fields[i].widget.attrs['placeholder']=self.fields[i].label

	class Meta:
		fields='__all__'
		labels={'name':'Nombre','debt':'Deuda'}
		model=Customer


class DateInput(forms.DateInput):
	input_type='date'
	input_formats=settings.DATE_INPUT_FORMATS

class CampaingUpdateForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(CampaingUpdateForm,self).__init__(*args,**kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs['class']='form__field'
	class Meta:
		model=Campaing
		fields='__all__'

		labels={
			'name':'Nombre',
			'campaing_num':'Numero de camapaña',
			'deperture_date':'Fecha de salida',
			'arrival_date':'Fecha de llegada',
		}

class CampaingForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(CampaingForm,self).__init__(*args,**kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs['class']='form__field'
	class Meta:
		model=Campaing
		fields='__all__'

		widgets={
			'deperture_date':DateInput(),
			'arrival_date':DateInput(),
		}

		labels={
			'name':'Nombre',
			'campaing_num':'Numero de camapaña',
			'deperture_date':'Fecha de salida',
			'arrival_date':'Fecha de llegada',

		}

class ArticleForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(ArticleForm,self).__init__(*args,**kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs['class']= 'form__field' if not i == 'price' else 'form__field form__field--int'


	class Meta:
		model=Article
		exclude=['campaing']
		labels={
			'name':'Nombre',
			'price':'Precio',
			'category':'Categoría',
			'buyer':'Comprador',
		}

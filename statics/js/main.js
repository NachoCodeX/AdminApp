$(document).ready(()=>{

	let saveForm=(function () {
		let form=$(this);
		$.ajax({
			url:form.attr("action"),
			data:form.serialize(),
			type:form.attr('method'),
			dateType:'JSON',
			success:(data)=>{
				console.log(data);
				if(data.form_is_valid){
					$('.modal').fadeOut('1000');
					$('.modal__cover').fadeOut('1000');
					$('#list').html(data.html_list);
					if(data.options){
						$('.select').html(data.options);
					}
				}else{
					$('.modal').html(data.html_form);
				}
			}


		});
		return false;
	});


	let loadForm=(function () {
			let btn=$(this);
			$.ajax({
				url:btn.attr('data-url'),
				type:'GET',
				dataType:'JSON',
				beforeSend:()=> {
					$('.modal').fadeIn('1000');
					$('.modal__cover').fadeIn('1000');
					console.log(btn.attr('data-url'));

				},
				success:(data)=> {
					$('.modal').html(data.html_form);
					$('.button-x').click(()=>{
						$('.modal').fadeOut('1000');
						$('.modal__cover').fadeOut('1000');
					});
				}

			});

	});


	//CREATE
	$('#modal_content').click((e)=>{
		let aux=e.target.className;
		if (aux==='modal__cover'){
			$('.modal').fadeOut('1000');
			$('.modal__cover').fadeOut('1000');
		}
	});

	$('.js-ajax').click(loadForm);
	$('#modal_content').on('submit','.js-campaing-create-form',saveForm)
	//UPDATE
	$('#table').on('click','.js-update-campaing',loadForm);
	$('#modal_content').on('submit','.js-campaing-update-form',saveForm)
	//DELETE
	$('#table').on('click','.js-delete-campaing',loadForm);
	$('#modal_content').on('submit','.js-campaing-delete-form',saveForm)


	//DETAIL Customer


	$('.select').on('change', function(e){
		let id_customer=$(this).val();
		$.ajax({
			url:'/detail_customer/result/',
			type:'GET',
			data:{'id':id_customer},
			success:(data)=>{
				$('#list').html(data.html_result);
				$('.btn').html('<button type="button" id="button_debt" class="button" data-url="/update/customer/'+id_customer+"\""+'>EDITAR CUENTA</button>');
			}
		});
	});

	$('.btn').on('click','#button_debt',loadForm);
	$('.btn').on('click','#button_debt',saveForm);


});

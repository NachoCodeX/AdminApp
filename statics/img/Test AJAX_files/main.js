$(document).ready(()=>{

	let loadForm=(function () {
			let btn=$(this);
			$.ajax({
				url:'/ajax-list/',
				type:'GET',
				dataType:'json',
				beforeSend:()=> {
					$('.modal__delete').fadeIn('1000');
					$('.cover').fadeIn('1000');
					console.log(btn.attr('url'));

				},
				success:(data)=> {
					console.log("SUCCESS");
					$('.modal__delete').html(data.html_tem);
				}

			});
		
	});


	$('.list-js').click(loadForm);


});
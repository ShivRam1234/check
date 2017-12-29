$(function() {
	  $('.searchbox1').keyup(function(){
		$.ajax({
			type: "GET",
			url:"/search_status1/",
			data:{
				'search_text1': $('#search1').val(),
				'csrfmiddlewaretoken':$("input[name = csrfmiddlewaretoken]").val()
			},
			success: searchSuccess1,
			dataType: 'html'

		});



	});
	});

function searchSuccess1(data,textStatus,jqXHR)
{
	$('#search-results1').html(data);
}

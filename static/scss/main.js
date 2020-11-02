$(document).ready(function(){
  
     
    product();
  
   function product(){
       $(document).on('click', 'a', function() {
               var id=this.id;
            });
		$.ajax({
			url:"action.php?cid=id",
			method:"POST",
             data: {product:1},
			success:function(data)
			{
				$('#getProduct').html(data);
			}
		});
	}
    
    

    $("body").delegate(".category","click", function(event){
    event.preventDefault();
    var cid=$(this).attr("cid");
       $.ajax({
			url:"action.php",
			method:"POST",
             data: {get_cat:1,category:cid},
			success:function(data)
			{
				$('#getProduct').html(data);
			}
		});

    });
    
    $("body").delegate(".type","click", function(event){
    event.preventDefault();
    var tid=$(this).attr("tid");
       $.ajax({
			url:"action.php",
			method:"POST",
             data: {get_type:1,type:tid},
			success:function(data)
			{
				$('#getProduct').html(data);
			}
		});

    }); 
    
    });
  
    

    
                       

 


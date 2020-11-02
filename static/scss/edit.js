var name;
var pic;
var quantity;
var des;
var price;
    function init()
    {
        var myForm = document.getElementById("myForm");
        myname = document.getElementById("name");
        price = document.getElementById("price");
         pic = document.getElementById("image1");
        file= document.getElementById("image");
        quantity = document.getElementById("q");
        des = document.getElementById("diss");
        myForm.onsubmit = check;
		
    } 
  

	function check()
    { 
       
        if (pic.value == ""){
            Swal.fire("Please enter pic");  
                return false; }
        
     
         if (!(file.value == "")){  
                var extension = $('#image').val().split('.').pop().toLowerCase();  
                if(jQuery.inArray(extension, ['gif','png','jpg','jpeg']) == -1)  
                {  
                     Swal.fire('Invalid Image File');  
                     $('#image').val('');  
                     return false;  
                }else{
        //Image preview
        var reader = new FileReader();
    reader.onload = function()
    {
      var output = document.getElementById('image1');
      output.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
       
           } 
         }
		if (myname.value == ""){
            Swal.fire("Please enter name");  
                return false; }
        
		if (price.value == ""){
            Swal.fire("Please enter price");  
                return false; }
    
		
       
        
        if (des.value == ""){
            Swal.fire("Please enter descripti");  
                return false; }
                    
        if (quantity.value == ""){
            Swal.fire("Please enter quantity");  
                return false; }


		 
		
 }
   
	
	
    window.addEventListener("load", init, false);
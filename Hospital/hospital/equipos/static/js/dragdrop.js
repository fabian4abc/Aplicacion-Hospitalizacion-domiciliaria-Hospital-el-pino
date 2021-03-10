
  var elem_destino;
	

 function comenzar(){
 	var personal=document.querySelectorAll("#zonainicio a");
 	for(var i=0;i<personal.length;i++){

 		personal[i].addEventListener("dragstart",comenzando_arrastrar,false);
 	}

 	elem_destino = document.getElementById("zonadestino")

 	elem_destino.addEventListener("dragenter",function(e){e.preventDefault();},false);

 	elem_destino.addEventListener("dragover",function(e){e.preventDefault();},false);

 	elem_destino.addEventListener("drop",soltado,false);

}

function comenzando_arrastrar(e){

	var element =e.target;
	e.dataTransfer.setData("Text",element.getAttribute("id"));
}


function soltado(e){

	e.preventDefault();

	var id=e.dataTransfer.getData("Text");
	console.log(id)

	var name=document.getElementById(id);
	console.log(name)
	elem_destino.innerHTML ="<p>holaa</p> <br>";
}



window.addEventListener("load",comenzar,false);

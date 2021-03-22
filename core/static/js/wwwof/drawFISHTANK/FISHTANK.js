class fishtank{
	constructor() {
		this.figura=document.getElementById("figura");
		this.litrostxt=document.getElementById('litros');
		this.texto_lado1=document.getElementById("lado01");
		this.texto_lado2=document.getElementById("lado02");
		this.texto_lado3=document.getElementById("lado03");
		this.entrada_lado_1=document.getElementById("entrada_lado_1");
		this.entrada_lado_2=document.getElementById("entrada_lado_2");
		this.entrada_lado_3=document.getElementById("entrada_lado_3");
		this.vel =0.01
		this.lados = new createVector(this.texto_lado1,this.texto_lado2,this.texto_lado3)
		this.frameCount = 0;
		this.parrafo;
	}
rectangle(){
	this.figura.innerHTML='rectagle';
	document.getElementById('help').innerHTML = ""
	litros=(this.entrada_lado_1.value*this.entrada_lado_2.value*this.entrada_lado_3.value)/1000;
	this.litrostxt.innerHTML=litros+"  l";
	this.texto_lado1.innerHTML='large cm';
	this.texto_lado2.innerHTML='heigth cm';
	this.texto_lado3.innerHTML='width cm';
	this.frameCount = this.frameCount+ this.vel;
	rotateX(this.frameCount);
  	rotateY(this.frameCount);
	this.fishtank = box(this.entrada_lado_1.value ,this.entrada_lado_2.value ,this.entrada_lado_3.value ,0,0);
	}	
cubic(){
	this.figura.innerHTML='cubic'
	document.getElementById('help').innerHTML = ""
	litros=(parseFloat(this.entrada_lado_1.value)**3)/1000;
	this.litrostxt.innerHTML=litros+" l"
	this.texto_lado1.innerHTML='large cm '
	this.texto_lado2.innerHTML='--NOT NEEDED--'
	this.texto_lado3.innerHTML='--NOT NEEDED--'
	this.frameCount = this.frameCount+ this.vel;
	rotateX(this.frameCount);
	rotateY(this.frameCount);
	this.fishtank = box(this.l);
}

triangularpris(){
	litros=(((this.entrada_lado_1.value*this.entrada_lado_2.value)/2)*this.entrada_lado_3.value)/1000
	this.figura.innerHTML='trianglar prism'
	this.litrostxt.innerHTML=litros+"l"
	this.texto_lado1.innerHTML='large of base cm'
	this.texto_lado2.innerHTML='heigth of base cm'
	this.texto_lado3.innerHTML='heigth  cm '
	this.frameCount = this.frameCount+ this.vel;
	document.getElementById('help').innerHTML = 'help links <br><button value="trianglar prism"><a href="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Faulaprende.com%2Fwp-content%2Fuploads%2F2019%2F01%2Fprisma-triangular.jpg&f=1&nofb=1"> trianglar prism </a></button><br><button value="base"><a href="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmatematicabasica.net%2Fwp-content%2Fuploads%2F2019%2F02%2Farea-do-triangulo-3.png&f=1&nofb=1">base</a></button>';
	rotateX(this.frameCount);
  	rotateY(this.frameCount);	
	this.fishtank =  cylinder(this.b,this.h,3)
	//return this.fishtank
}
cilinder(){
	this.figura.innerHTML='cilinder';
	document.getElementById('help').innerHTML = ""
	//this.R=parseFloat(this.entrada_lado_1.value)
	//this.h=parseFloat(this.entrada_lado_2.value)
	litros=PI*(parseFloat(this.entrada_lado_1.value)**2)*parseFloat(this.entrada_lado_2.value)/1000	
	this.texto_lado1.innerHTML='radio cm'
	this.texto_lado2.innerHTML='heigth cm'
	this.texto_lado3.innerHTML='--NOT NEEDED--'
	this.litrostxt.innerHTML=litros+" l"
	this.frameCount = this.frameCount+ this.vel;
	rotateX(this.frameCount);
  	rotateY(this.frameCount);
	this.fishtank =  cylinder(this.R,this.h,24)
}


}
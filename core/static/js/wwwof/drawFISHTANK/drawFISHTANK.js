let dft ;
function setup() {
	canvas = createCanvas(750, 463, WEBGL) ;
	dft = new fishtank();
}
function draw() {
	background(150);
	x = (windowWidth - width) / 2 ;
	y = 300;
	canvas.position(x, y);
	Select = document.getElementById('select');
	seleccion = Select.options[Select.selectedIndex].value;
	if (seleccion == 'rectagle') {
		dft.rectangle()
	}
	else if (seleccion == 'cubic') {
		dft.cubic()
	}
	else if (seleccion == 'triangle'){
		dft.triangularpris()
	}
	else if (seleccion == 'cilinder') {
		dft.cilinder()
	}

}
//setInterval(draw,500)
public class Teste{

	public static void main(String[] args){
		Caneta c1 = new Caneta();
		c1.cor = "Azul";
		c1.ponta = 0.5f;
		c1.tampada = false;
		c1.status();
	}
}

class Caneta{

	// Atributos
	String modelo;
	String cor;
	float ponta;
	int carga;
	boolean tampada;
	void status(){
		System.out.println("Uma caneta " + this.cor);
		System.out.println("Com ponta " + this.ponta);
		System.out.println("Está tampada? " + this.tampada);
	}

	// Metodos
	void rabiscar(){
	
	}

	void tampar(){
	
	}

	void destampar(){
	
	}

}



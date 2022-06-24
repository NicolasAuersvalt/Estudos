// Classes

#include <iostream>

using namespace std;

class Pizza{

/* Precisamos definir o que é público ou privado */

public:
    int tomate = 5;
    int salame = 3;
    string nomes;

    void make();

private:

};

/* Deve-se construir o Método make() FORA da classe */

void make(){
    
}

int main(){

    /* Agora vamos usar a classe */


    // INSTANCIANDO UM NOVO OBJETO

    Pizza *bacon = new Pizza();

    /* Estou criando um novo objeto do tipo Pizza que é */ 

    /* Regra primitiva, vamos declarar com * antes SEMPRE */


    // CHAMANDO OBJETO DA CLASSE

    cout << bacon -> tomate;

    /* método é acionado com . em C */

    /* Já em C++, vamos usar -> */

    return 0;
}
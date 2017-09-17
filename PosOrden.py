from Nodo import *
from Pila import Pila

def leerCadena():
	cadena = raw_input('Ingrese la cadena de caracteres a operar:')
	#listaCaracteres = []
	listaCaracteres = cadena.split(' ')
	return listaCaracteres

def crearArbol(lista, pila):
        for i in range(0,len(lista)):
                if lista[i] in "+-*/=":
                        der = pila.sacarElemento()
                        izq = pila.sacarElemento()
                        nodoAux = Nodo(lista[i], izq, der)
                        pila.agregarElemento(nodoAux)
                else:
                        pila.agregarElemento(Nodo(lista[i], None, None))
        return pila.sacarElemento()

def imprimirArbolPostfijo(arbol):
        if arbol != None:
                imprimirArbolPostfijo(arbol.izq)
                imprimirArbolPostfijo(arbol.der)
                print arbol.valor               

def ingresarArbol():
        while True:
                opcion = raw_input('Desea ingresar una expresion matematica en posfijo: (Y/N)')
                if opcion == 'Y':
                        cadena = leerCadena()
                        pila = Pila()
                        nodo = crearArbol(cadena, pila)
                        print "Resultado operacion: " , evaluar(nodo)
                if opcion == 'N':
                        break
        imprimirDatos()
        return None

def main():
        ingresarArbol()
        return None

main()

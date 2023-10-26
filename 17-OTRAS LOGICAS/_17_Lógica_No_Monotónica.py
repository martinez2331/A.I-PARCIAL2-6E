#La l�gica no mon�tona es un enfoque en la l�gica y la inteligencia artificial que se utiliza para representar el razonamiento que no sigue 
#la l�gica cl�sica monot�nica. En la l�gica mon�tona, se asume que si una afirmaci�n es cierta, seguir� siendo cierta al agregar m�s informaci�n. 
#En cambio, en la l�gica no mon�tona, las afirmaciones pueden dejar de ser ciertas cuando se agrega nueva informaci�n.

#Un ejemplo com�n de l�gica no mon�tona es el "mundo del cierre" (closed world assumption), donde se asume que algo es falso a menos que se pueda
#demostrar que es cierto. Esto es �til en situaciones en las que no se tiene informaci�n completa y es necesario hacer suposiciones l�gicas basadas
#en la informaci�n disponible.

class BaseConocimiento:
    def __init__(self):
        self.hechos = set()

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def eliminar_hecho(self, hecho):
        self.hechos.discard(hecho)

    def verificar_hecho(self, hecho):
        return hecho in self.hechos

# Crear una base de conocimiento
base_de_conocimiento = BaseConocimiento()

# Agregar hechos iniciales
base_de_conocimiento.agregar_hecho("p�jarosvuelan")
base_de_conocimiento.agregar_hecho("ping�inosnovuelan")

# Verificar si los p�jaros vuelan (l�gica mon�tona)
if base_de_conocimiento.verificar_hecho("p�jaros_vuelan"):
    print("Los p�jaros vuelan.")
else:
    print("Los p�jaros no vuelan.")

# Agregar informaci�n adicional
base_de_conocimiento.agregar_hecho("ping�inos_pueden_nadar")

# Verificar si los p�jaros vuelan con la nueva informaci�n (l�gica no mon�tona)
if base_de_conocimiento.verificar_hecho("p�jaros_vuelan"):
    print("Los p�jaros vuelan.")
else:
    print("Los p�jaros no vuelan.")

# Verificar si los ping�inos vuelan con la nueva informaci�n (l�gica no mon�tona)
if base_de_conocimiento.verificar_hecho("ping�inos_no_vuelan"):
    print("Los ping�inos no vuelan.")
else:
    print("Los ping�inos pueden volar.")


#En este ejemplo, estamos utilizando una base de conocimiento simple para representar hechos y c�mo cambia la l�gica cuando se agrega nueva 
#informaci�n (l�gica no mon�tona). Los ping�inos originalmente se consideran como no voladores, pero despu�s de agregar informaci�n adicional,
#la l�gica cambia y se reconoce que los ping�inos no son necesariamente no voladores en este contexto.En este ejemplo, estamos utilizando una
#base de conocimiento simple para representar hechos y c�mo cambia la l�gica cuando se agrega nueva informaci�n (l�gica no mon�tona).
#Los ping�inos originalmente se consideran como no voladores, pero despu�s de agregar informaci�n adicional, la l�gica cambia y se reconoce que los
#ping�inos no son necesariamente no voladores en este contexto.

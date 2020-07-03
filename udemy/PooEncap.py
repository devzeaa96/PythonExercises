class encapsulamiento:
    __privado_atri = 'Atributo privado no se podra acceder desde afuera'

    def __privado_meth(self):
        print('Metodo que no podra acceder desde afuera')

#e = encapsulamiento()
#e.__privado_meth()

class encapsulamiento1:
    privado_atri = 'Atributo privado no se podra acceder desde afuera'

    def privado_meth(self):
        print('Metodo que no podra acceder desde afuera')

e = encapsulamiento1()
print(e.privado_atri)
e.privado_meth()


### Para encapsular dentro de la clase algun metodo o atributo solo debemos nombrarlos con __(dos guiones al piso) antes del nombre 
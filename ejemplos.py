
#Trabajador nombre, ape, hora, valor hora
#Mostarar informacion trabajador
#metodo mostrar cantidad de horas extras
#Metodo que retorne el monto a pagar por horas extras >40
#cada hora extra se paga por el 50% del valor de la hora normal
#metodo que retorne el monto a pagar por horas normales
#metodo que retorne el monto final que recibe el trabajo

class Trabjador:
    def crear(self , nom , ape , hora, valorHora):
        self.nom=nom
        self.ape=ape
        self.hora=hora
        self.valorHora=valorHora
  

    def mostrar(self):
        print("Nombre: ", self.nom, "Apellido: ", self.ape, "hora: " ,  self.valorHora , "hora: " ,  self.valorHora)

    def Mensaje(self):   
        if(self.edad>=18):
            return "iguales"
        else:
             return "no"      

    def montoPagar(self):
        Pago=self.valorHora*self.hora
        return Pago

    def horaExtras(self):
        if(self.hora>40):
            return   self.hora-40 
        else:
            return 0
              

    def horaExtrasPago(self):
            
        if(self.hora>40):
            return   self.valorHora*1.5
        else:
            return 0

    def montoFinal(self):
            
            return self.montoPagar()+self.horaExtrasPago()
                
        


unTrabjador=Trabjador()             
n=input("Digite un nombre: ")
a=input("Digite un apellido: ")
e=int(input("Ingrese hora :"))
f=int(input("Ingrese hora valor hora :"))
unTrabjador.crear(n,a,e,f)
unTrabjador.mostrar()
print(unTrabjador.horaExtras())
print(unTrabjador.montoPagar())
print (unTrabjador.horaExtrasPago())
print (unTrabjador.montoFinal())
t=input("") #Para que nose cierre
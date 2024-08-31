class Persona:
     def pensar(self, tema):
        print("Esta pensando " + tema)

     def correr(self):
        print("Esta corriendo")

     def aprender(self):
         print("Esta aprendiendo")

heidi = Persona()
heidi.pensar(tema= "en letras")

alejandro = Persona()
alejandro.correr()

adrian = Persona()
adrian.aprender()

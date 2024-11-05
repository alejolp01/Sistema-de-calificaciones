
class Calificacion:
    def __init__(self, Estudiante=None, Asignatura=None, Nota=None): # None porque no siempre se va a necesitar proporcionar todos los archivos
       self.Estudiante=Estudiante
       self.Asignatura=Asignatura
       self.Nota=Nota
       
    def __str__(self):
        return (f'Estudiante:{self.Estudiante}, Asignatura:{self.Asignatura}, Nota:{self.Nota}')



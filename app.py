class Calculadora(object):

  def __init__(self):
    print "estoy en init"
    flag = True
    funciones = {
      "showset": self.show_set,
      "sets":self.sets,
      "showsets": self.show_sets,
      "union": self.union,
      "intersection": self.inteserction,
      "set": self.set_var,
      "setunion":self.set_union,
      "setintersection":self.set_intersection
    }
    self.conjuntos = {}
    while flag:
      self.expresion = raw_input('-> ')
      try:
        if self.expresion=='sets':
          self.sets()
          continue
        if self.expresion=='showsets':
          self.show_sets()
          continue
        linea = self.expresion.split(' ')
        comando = linea[0]
        if linea.__len__() > 1:
          funciones[comando](self.expresion.replace(comando, ''))
      except:
        print "error al leer conjunto"
        pass
      
  def sets(self):
    for conjunto in self.conjuntos:
      print conjunto

  def show_set(self, cadena):
    conjunto = cadena.replace(' ', '')
    a = ''
    for elemento in self.conjuntos[conjunto]:
      a = a + elemento + ','
    b = a[:a.__len__() -1:]
    print '{' + b + '}'

  def show_sets(self):
    for conjunto in self.conjuntos:
      string = conjunto + ':={'
      for elemento in self.conjuntos[conjunto]:
        string = string + elemento +','
      string2 = string[:string.__len__() -1:] + '}'
      print string2

  def set_union(self, cadena):
    conjuntos = cadena.replace(' ', '').split(',')
    if conjuntos.__len__() != 3:
      print "error con parametros"
      return
    cadena2 = conjuntos[1] + ','+conjuntos[2]
    self.conjuntos[conjuntos[0]] = self.union(cadena2)

  def set_intersection(self,cadena):
    conjuntos = cadena.replace(' ', '').split(',')
    if conjuntos.__len__() != 3:
      print "error con parametros"
      return
    cadena2 = conjuntos[1] + ','+conjuntos[2]
    self.conjuntos[conjuntos[0]] = self.inteserction(cadena2)

  def union(self, cadena):
    print "union"
    print cadena
    conjuntos = cadena.replace(' ', '').split(',')
    union = ''
    arreglo_union = []
    for elemento in self.conjuntos[conjuntos[0]]:
      union = union + elemento + ','
      arreglo_union.append(elemento)
    for elemento in self.conjuntos[conjuntos[1]]:
      if not union.__contains__(elemento):
        union = union + elemento + ','
        arreglo_union.append(elemento)
    print '{' + union + '}'
    return arreglo_union

  def inteserction(self, cadena):
    print 'interseccion'
    conjuntos = cadena.replace(' ', '').split(',')
    tmp = []
    inter = ''
    if (conjuntos[0] in self.conjuntos and conjuntos[1] in self.conjuntos) == False:
      print "Alguno de los conjuntos no existe"
      return
    for elemento in self.conjuntos[conjuntos[0]]:
      tmp.append(elemento)
    interseccion = []
    for elemento in self.conjuntos[conjuntos[1]]:
      if tmp.__contains__(elemento):
        inter = inter + elemento + ','
        interseccion.append(elemento)
    print '{' + inter[:inter.__len__()-1:] + '}'
    return interseccion
    

  def set_var(self, cadena):
    let = cadena.replace(' ', '')
    arreglo = let.split(':=')
    if not arreglo[0]:
      print "especifique conjunto"
      return
    if arreglo.__len__() < 2:
      print "error en parametros"
      return
    conjunto = arreglo[0]
    valor = arreglo[1]
    if valor[0]!="{" or valor[-1:]!="}":
      print "error con llaves"
      return
    contador_llaves = 0
    for v in valor:
      if v=='{':
        contador_llaves = contador_llaves + 1
      if v=='}':
        contador_llaves = contador_llaves - 1
    if contador_llaves!=0:
      print "problema con las llaves"
      return
    self.conjuntos[conjunto] = []

    elementos = valor.replace('{','').replace('}','').split(',')
    for elemento in elementos:
      if not elemento:
        print "elemento invalido"
        return
    for elemento in elementos:
      self.conjuntos[conjunto].append(elemento)

if __name__ == '__main__':
  Calculadora()

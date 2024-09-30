from abc import ABC, abstractmethod

class Empleado_F2(ABC):
    def __init__(self, rfc, apellidos, nombres):
        self._rfc=rfc
        self._apellidos=apellidos
        self._nombres=nombres
    @abstractmethod
    def mostrar_atributos(self):
        pass
    
    def atributos(self):
        return self._rfc,self._apellidos, self._nombres
    
class EmpleadoVendedor_F2(Empleado_F2):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto_vendido=monto_vendido
        self.tasa_comision=tasa_comision

    def calcular_ingresos(self):
        return self.monto_vendido*self.tasa_comision
    def calcular_bonificacion(self):
        ingresos=self.calcular_ingresos()
        if self.monto_vendido<1000:
            return 0
        elif 1000<=self.monto_vendido<=5000:
            return 0.05*ingresos
        else:
            return 0.10*ingresos
    def calcular_descuento(self):
        ingresos=self.calcular_ingresos()
        if ingresos<1000:
            return 0.11*ingresos
        else:
            return 0.15*ingresos
    def calcular_sueldo_neto(self):
        ingresos=self.calcular_ingresos()
        bonificacion=self.calcular_bonificacion()
        descuento=self.calcular_descuento()
        return ingresos+bonificacion-descuento
    
    def mostrar_informacion(self):
        return (f"RFC: {self.rfc}, apellidos: {self.apellidos}, nombres: {self.nombres}, Monto Vendido: {self.monto_vendido}, Tasa de Comisión: {self.tasa_comision}")
class EmpleadoPermanente_F2(EmpleadoVendedor_F2):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, numero_seguro_social):
        super().__init__(rfc, apellidos, nombres)
        if sueldo_base < 150:
            raise ValueError("El sueldo base no puede ser menor a 150 pesos.")
        self.sueldo_base=sueldo_base
        self.numero_seguro_social = numero_seguro_social

    def ingresos(self):
        return self.sueldo_base
    def calcular_descuento(self):
        return 0.11*self.sueldo_base
    def calcular_sueldo_neto(self):
        ingresos=self.ingresos()
        descuento=self.calcular_descuento()
        return ingresos-descuento

    def mostrar_informacion(self):
        return (f"RFC: {self.rfc}, Apellidos: {self.apellidos}, Nombres: {self.nombres}, Sueldo Base: {self.sueldo_base}, NSS: {self.numero_seguro_social}")

class Artikulo:
    
    def __init__(self, Kodea, Izena, Prezioa):
        
        self.Kodea=Kodea
        self.Izena=Izena
        self.Prezioa=Prezioa
        
class Bideo_jokoak(Artikulo):
    
    def __init__(self,Generoa, Empresa, plataforma, mult_lokal, mult_online, PEGI, titulua):
        
        self.Generoa=Generoa
        self.Empresa=Empresa
        self.plataforma=plataforma
        self.mult_lokal=mult_lokal
        self.mult_online=mult_online
        self.PEGI=PEGI
        self.titulua=titulua
        
class Consola(Artikulo):
    
    def __init__(self,Plataforma, Empresa):
        
        self.Plataforma=Plataforma
        self.Empresa=Empresa
        
class Liburuak(Artikulo):
    
    def __init__(self,ISBN,Autor, Generoa,paginas, argitaletxea,argitaratu_eguna, editoriala, titulua):
        
        self.ISBN=ISBN
        self.Autor=Autor
        self.Generoa=Generoa     
        self.paginas=paginas
        self.argitaletxea=argitaletxea
        self.argitaratu_eguna=argitaratu_eguna
        self.editoriala=editoriala
        self.titulua=titulua
        

class Usuario:
       
    def __init__(self, NAN, Izena, Abizena,algo):
        
        self.NAN=NAN
        self.Izena=Izena
        self.Abizena=Abizena
        self.algo=algo
        
class Erosleak(Usuario):

    def __init__(self, erosle_kodea):
        
        self.erosle_kodea=erosle_kodea
        
class Langileak(Usuario):
    
    def __init__(self, kargua, langile_kodea):
        
        self.kargua=kargua
        self.langile_kodea=langile_kodea
print('kaixo')
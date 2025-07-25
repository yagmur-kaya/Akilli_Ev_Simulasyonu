class Cihaz:
    def __init__(self):
        self.durum="Kapalı"
    def ac(self):
        self.durum="Açık"
    def kapat(self):
        self.durum="Kapalı" 
    def durum_goruntule(self):
        return self.durum
                   
class klima(Cihaz):
    def __init__(self):
     super().__init__()
     self.derece=24
    def derece_ayarla(self,sayi):
        self.derece=sayi
        return f" Klimanız {self.derece} derece ile çalışıyor."
    def derece_goster(self):
        return  f" Klimanız {self.derece} derecedir."

class perde(Cihaz):
    def __init__(self):
     super().__init__()
    def yariya_indir(self):
       self.durum="Yarı Açık"
    def ac(self):
       return super().ac()
    def kapat(self):
       return super().kapat()
    def durum_goruntule(self):
       return f" Perdeniz {self.durum} durumdadır."
    
class firin(Cihaz):
 def __init__(self):
      super().__init__()  
   def sicaklik_ayarla(self,sayi):
      self.derece=sayi
      return f" Fırın {self.derece} derece ile çalışıyor."
   def sicaklik_goster(self,sayi):
      self.sicaklik=sayi
      return f" Fırının sıcaklığı {self.derece}  derecedir."
    
   def alt_ust(self):
      self.pisirme_mod="alt-üst"
      return f" Fırınınız {self.pisirme_mod} modunda çalışıyor."
   def fanli_(self):
      self.pisirme_mod="fanlı"
      return f" Fırınınız {self.pisirme_mod} modunda çalışıyor."
   def grill_(self):
      self.pisirme_mod="grill"
      return f" Fırınınız {self.pisirme_mod} modunda çalışıyor."
   def buz_cozme(self):
      self.pisirme_mod="buz çözme"  
      return f" Fırınınız {self.pisirme_mod} modunda çalışıyor."
   def pisir(self,süre):
      self.sure=süre
      return f" Fırın {self.derece} derece ile {self.pisirme_mod} modunda {self.sure} dakikadır çalışıyor."
klima_=klima()
print(klima_.derece_ayarla(22))
print(klima_.derece_goster()) 

perde_=perde()
perde_.yariya_indir()
perde_.durum_goruntule()
print(perde_.durum_goruntule())

firin_=firin()
firin_.ac()
firin_.sicaklik_ayarla(180)
firin_.fanli_()
firin_.sicaklik_goster(25)


print(firin_.sicaklik_ayarla(220))
print(firin_.sicaklik_goster(25))
print(firin_.grill_())
print(firin_.buz_cozme())
print(firin_.pisir(30))
       
        



        

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
    def derece_goster(self):
        return self.derece 

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
       return f" Perde durumu : {self.durum}"
    
class firin(Cihaz):
   def __init__(self):
      super().__init__()  
   def sicaklik_ayarla(self,sayi):
      self.derece=sayi
      return f" Fırın {self.derece} ile çalışıyor."
   def sicaklik_goster(self):
      return f" Sıcaklık: {self.derece} 'dir."
   #def pisirme_mod(self,mod):
      
   def alt_ust(self):
      self.pisirme_mod="alt-üst"
   def fanli_(self):
      self.pisirme_mod="fanlı"
   def grill_(self):
      self.pisirme_mod="grill"
   def buz_cozme(self):
      self.pisirme_mod="buz çözme"  
      return f" Fırınınız {self.pisirme_mod} 'unda çalışıyor."
   def pisir(self,süre):
      self.sure=süre
      return f" Fırın {self.derece} ile {self.pisirme_mod} modunda {self.sure} dakika çalışıyor."
firin_=firin()
firin_.ac()
firin_.sicaklik_ayarla(180)
firin_.fanli_()
print(firin_.pisir(30))
print(firin_.sicaklik_ayarla(220))
perde_=perde()
perde_.yariya_indir()
perde_.durum_goruntule()
print(perde_.durum_goruntule())
       
        



        
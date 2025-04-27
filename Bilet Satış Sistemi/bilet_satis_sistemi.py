import tkinter as tk
from tkinter import simpledialog, messagebox


# Kullanıcı Verileri
class Etkinlik:
    def __init__(self, ad, tarih, mekan, toplam_bilet):
        self.ad = ad
        self.tarih = tarih
        self.mekan = mekan
        self.toplam_bilet = toplam_bilet
        self.kalan_bilet = toplam_bilet
        self.bilet_alanlar = []

    def bilet_sat(self, kullanici_adi, adet):
        if self.kalan_bilet >= adet:
            self.kalan_bilet -= adet
            self.bilet_alanlar.append((kullanici_adi, adet))
            return True
        else:
            return False
        
# Uygulama Arayüzü

class BiletSatisUygulamasi:
    def __init__(self, root):
        self.etkinlikler = []

        self.root = root
        self.root.title("Bilet Satış Sistemi")
        self.root.geometry("500x500")

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack()

        tk.Button(self.frame, text="Etkinlik Ekle", width=30, command=self.etkinlik_ekle).pack(pady=5)
        tk.Button(self.frame, text="Bilet Satın Al", width=30, command=self.bilet_satin_al).pack(pady=5)
        tk.Button(self.frame, text="Etkinlikleri Göster", width=30, command=self.etkinlikleri_goster).pack(pady=5)
        tk.Button(self.frame, text="Bilet Alanları Göster", width=30, command=self.bilet_alanlari_goster).pack(pady=5)
        tk.Button(self.frame, text="Çıkış", width=30, command=root.quit).pack(pady=5)

    def etkinlik_ekle(self):
        ad = simpledialog.askstring("Etkinlik Adı", "Etkinlik adını girin:")
        tarih = simpledialog.askstring("Etkinlik Tarihi", "Tarih (GG/AA/YYYY):")
        mekan = simpledialog.askstring("Mekan", "Mekan adı:")
        toplam_bilet = simpledialog.askinteger("Toplam Bilet", "Toplam bilet sayısı:")
        if ad and tarih and mekan and toplam_bilet:
            yeni_etkinlik = Etkinlik(ad, tarih, mekan, toplam_bilet)
            self.etkinlikler.append(yeni_etkinlik)
            messagebox.showinfo("Başarılı", "Etkinlik eklendi!")

    def bilet_satin_al(self):
        if not self.etkinlikler:
            messagebox.showerror("Hata", "Önce etkinlik ekleyin!")
            return

        etkinlik_listesi = "\n".join([f"{i}: {e.ad} ({e.kalan_bilet} bilet kaldı)" for i, e in enumerate(self.etkinlikler)])
        secim = simpledialog.askinteger("Etkinlik Seç", f"Etkinlik numarasını girin:\n{etkinlik_listesi}")
        
        if secim is None or secim >= len(self.etkinlikler):
            messagebox.showerror("Hata", "Geçersiz seçim.")
            return

        kullanici_adi = simpledialog.askstring("Bilet Sahibi", "Bilet sahibinin adını girin:")
        adet = simpledialog.askinteger("Bilet Adedi", "Kaç bilet almak istiyorsunuz?")
        
        if kullanici_adi and adet:
            if self.etkinlikler[secim].bilet_sat(kullanici_adi, adet):
                messagebox.showinfo("Başarılı", f"{kullanici_adi} için {adet} bilet satın alındı!\nKalan bilet: {self.etkinlikler[secim].kalan_bilet}")
            else:
                messagebox.showerror("Hata", "Yeterli bilet yok!")

    def etkinlikleri_goster(self):
        if not self.etkinlikler:
            messagebox.showinfo("Etkinlikler", "Hiç etkinlik bulunmuyor.")
            return

        liste = ""
        for e in self.etkinlikler:
            liste += f"{e.ad} - {e.tarih} - {e.mekan} (Kalan Bilet: {e.kalan_bilet})\n"
        
        messagebox.showinfo("Etkinlikler", liste)

    def bilet_alanlari_goster(self):
        if not self.etkinlikler:
            messagebox.showinfo("Bilgi", "Hiç etkinlik yok.")
            return

        etkinlik_listesi = "\n".join([f"{i}: {e.ad}" for i, e in enumerate(self.etkinlikler)])
        secim = simpledialog.askinteger("Etkinlik Seç", f"Bilet sahiplerini görmek istediğiniz etkinlik:\n{etkinlik_listesi}")

        if secim is None or secim >= len(self.etkinlikler):
            messagebox.showerror("Hata", "Geçersiz seçim.")
            return

        etkinlik = self.etkinlikler[secim]
        if not etkinlik.bilet_alanlar:
            messagebox.showinfo("Bilgi", "Henüz bilet alan yok.")
            return

        sahipler = ""
        for kisi, adet in etkinlik.bilet_alanlar:
            sahipler += f"{kisi} ({adet} bilet)\n"
        
        messagebox.showinfo("Bilet Alanlar", sahipler)


# Çalıştır ve Kullan

if __name__ == "__main__":
    root = tk.Tk()
    app = BiletSatisUygulamasi(root)
    root.mainloop() 
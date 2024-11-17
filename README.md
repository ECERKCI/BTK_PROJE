HOUSİNG PRİCES PREDİCTİON
Bu proje, ev özelliklerine dayanarak tahmini ev fiyatlarını hesaplamak için bir makine öğrenmesi modelinin (RandomForestRegressor) oluşturulmasını ve bunun bir web uygulamasında kullanılmasını içeriyor. 
Kullanıcılar, evlerin çeşitli özelliklerini girerek tahmin edilen fiyatları görüntüleyebilirler.

Proje İçeriği
Bu repo aşağıdaki bileşenleri içerir:
housing_price_model.pkl: Modelin eğitildiği ve kaydedildiği dosya.
app.py: Streamlit ile oluşturulmuş web uygulaması kodu.
Jupyter Notebook: Modelin eğitilmesi, verilerin analiz edilmesi ve değerlendirilmesi için kullanılan kod.
feature_columns.pkl: Modelin eğitildiği özelliklerin isimlerini içeren dosya.
dataset.csv (Opsiyonel): Projede kullanılan ev fiyatları veri seti. Eğer veri seti GitHub'a yüklenmediyse, Kaggle linki üzerinden indirilebilir.

Kullanılan Teknolojiler
Python: Python dilinde geliştirilmiştir.
Streamlit: Web arayüzü için kullanılmıştır.
Scikit-learn: Makine öğrenmesi modeli ve model değerlendirmesi için kullanılmıştır.
Pandas, Numpy: Veri manipülasyonu ve analiz için kullanılmıştır.
Matplotlib, Seaborn: Veri görselleştirme için kullanılmıştır.

Gereksinimler
Projeyi çalıştırmak için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:
pip install streamlit scikit-learn pandas numpy matplotlib seaborn joblib

Veri Seti
Veri seti, evlerin özellikleri ve satış fiyatlarıyla ilgili bilgileri içerir. Bu projede kullanılan veri setini Kaggle üzerinden indirebilirsiniz. Veri seti, her evin özelliklerini (örneğin, yaşanabilir alan, arsa alanı, yıl gibi) ve bu özelliklere dayanarak tahmin edilen satış fiyatlarını içerir.

Projeyi Çalıştırmak
Modeli Eğitmek ve Kaydetmek:

Jupyter Notebook dosyasını çalıştırarak modelin eğitilmesini sağlayabilirsiniz. Bu dosya, verilerin işlenmesi, modelin eğitilmesi ve kaydedilmesi adımlarını içerir.
Model eğitildikten sonra housing_price_model.pkl dosyasını kaydeder.
Web Uygulamasını Çalıştırmak:
Web uygulamasını çalıştırmak için app.py dosyasını kullanabilirsiniz.

Uygulama, kullanıcıdan evin çeşitli özelliklerini alacak ve eğitilen model üzerinden tahmin edilen ev fiyatını gösterecektir.
Web uygulamasını başlatmak için aşağıdaki komutu kullanabilirsiniz:
streamlit run app.py

Bu komut, tarayıcınızda uygulamayı başlatacak ve sol panelden ev özelliklerini girerek tahmin edilen fiyatı görüntüleyebilirsiniz.

Modelin Eğitilmesi
Model, RandomForestRegressor kullanılarak eğitilmiştir. Eğitim sırasında, evlerin çeşitli özellikleri (örneğin, metrekare, arsa alanı, yapım yılı gibi) kullanılmıştır. Model, ev fiyatlarını doğru şekilde tahmin edebilmek için bu verilerle eğitilmiştir.

Modelin eğitim süreci ve veri manipülasyonu Jupyter Notebook dosyasına eklenmiştir. Bu dosya, veri setinin temizlenmesi, özelliklerin seçilmesi, modelin eğitilmesi ve değerlendirilmesi adımlarını içerir.

Kullanıcı Girdileri
Streamlit uygulaması, kullanıcıların aşağıdaki ev özelliklerini girmelerine olanak tanır:

GrLivArea (m²): Yaşanabilir alanın metrekare cinsinden değeri.
LotArea (m²): Arsa alanının metrekare cinsinden değeri.
OverallQual (Genel Kalite): Ev kalite derecesi (1-10 arasında).
YearBuilt (Yapım Yılı): Ev yapım yılı.
Girdiğiniz özelliklere dayanarak model, tahmin edilen ev fiyatını döndürecektir.

Modelin Kullanılması
Eğitilen model, housing_price_model.pkl dosyasına kaydedildikten sonra, web uygulaması bu modelin tahmin yeteneğini kullanarak yeni verilerle tahmin yapabilir.

Örnek Kullanım
Web uygulamasını başlatın (streamlit run app.py).
Kenar çubuğundan ev özelliklerini girin.
"Tahmini Ev Fiyatı" başlığında tahmin edilen ev fiyatını görün.

import statistics as st

lat_ms = [120, 130, 125, 128, 122, 600]
media = st.mean(lat_ms)
mediana = st.median(lat_ms)
modas = st.multimode(lat_ms)
dp_amostral = st.stdev(lat_ms) # amostral (n-1)
var_amostral = dp_amostral ** 2 # variância amostral

print("Média:", round(media,2))
print("Mediana:", mediana)
print("Moda(s):", modas)
print("Variância amostral:", round(var_amostral,2))
print("DP amostral:", round(dp_amostral, 2))
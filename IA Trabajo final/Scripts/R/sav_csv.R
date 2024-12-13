library(haven)
## Se cambia los .sav a .csv

# Leer divorcios de 2015 .sav
data <- read_sav("Descargas/bdd_divorcios_2015_spss/divorcios 2015.sav")

write.table(data, "Descargas/IA Trabajo final/Scripts/EDV 2015.csv", row.names = FALSE, quote = FALSE, sep = ";")

# Leer divorcios de 2014 .sav
data <- read_sav("Descargas/bdd_divorcios_2014_spss/Divorcios_2014.sav")

write.table(data, "Descargas/IA Trabajo final/Scripts/EDV 2014.csv", row.names = FALSE, quote = FALSE, sep = ";")


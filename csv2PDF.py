import fpdf
import os
import time

#PASOS PREVIOS
#CONVERTIR LA TABLA A CSV SEPARADO POR ;. sEPUEDE SEPARAR POR , Y LUEGO REEMPLAZAR , OR ;
#REEMPLAZAR LAS RUTAS DEL CSV DE \ A /
#AJUSTAR LAS SIGUIENTES RUTAS
#ruta del logo de la junta
junta="O:/sigmena/logos/junta/JCYL.jpg"
#abro el csv separado por ;
patharchivo="c:/lidar/csv.csv"
#definir la carpeta, que debe existir, donde queremos guardar los distintos pdfs.
ruta="c:/lidar/"

archivo = open(patharchivo, "r")

#inicio un contador para cada pagina
contador=0
 
#leo una linea
lines=archivo.readlines()


provincia="SALAMANCA"

#proceso cada linea, cojo los datos y los meto a un pdf.
for line in lines:
    contador=contador+1
    #defino cada elemento del csv por el orden que ocupa
    #elementos separados por ;
    datosseparados= line.split(";")
    
    n_mojon=datosseparados[1]
    monte=datosseparados[7]
    n_monte=datosseparados[8]
    municipio=datosseparados[9]
    pertenencia=datosseparados[11]
    lat=datosseparados[12]
    lon=datosseparados[13]
    foto=datosseparados[2]
    orto=datosseparados[4]
    x=datosseparados[-6]
    y=datosseparados[-5]
    h=datosseparados[-4]
    cat=datosseparados[-3]
    estado=datosseparados[-2]
    
    if contador>1:
        #creo un pdf vacio
        pdf=fpdf.FPDF("P","mm","A4")
        pdf.add_page()
        pdf.set_font('Arial','B',9)
        #meto los rectangulos
        pdf.set_xy(31,50)
        pdf.cell(116,8,"",border=1, align="L")
        pdf.set_xy(31,61)
        pdf.cell(116,17,"",border=1, align="L")
        pdf.set_xy(153,50)
        pdf.cell(31,28,"",border=1, align="L")
        pdf.set_xy(104,84)
        pdf.cell(80,21,"",border=1, align="L")
        pdf.set_xy(104,107)
        pdf.cell(80,33,"",border=1, align="L") 
        pdf.set_xy(104,151)
        pdf.cell(80,10,"",border=1, align="L")
        pdf.set_xy(103,83)
        pdf.cell(82,79,"",border=1, align="L") 
        
        #meto textos fijos
        
        pdf.set_xy(33,50)
        pdf.cell(10,10,"MONTE",border=0, align="L")
        pdf.set_xy(33,60)
        pdf.cell(10,10,"Nº C.U.P.",border=0, align="L")
        pdf.set_xy(75,60)
        pdf.cell(10,10,"Término Municipal",border=0, align="L")
        pdf.set_xy(33,71)
        pdf.cell(10,10,"Provincia",border=0, align="L")
        pdf.set_xy(75,71)
        pdf.cell(10,10,"Pertenencia",border=0, align="L")
        pdf.set_xy(160,53)
        pdf.cell(10,10,"Nº MOJON",border=0, align="L")
        pdf.set_xy(122,81)
        pdf.cell(10,10,"COORDENADAS GEOGRÁFICAS",border=0, align="L")        
        pdf.set_xy(122,104)
        pdf.cell(10,10,"COORDENADAS UTM (Huso 30)",border=0, align="L")  
        pdf.set_font('Arial','',10)
        pdf.set_xy(105,87)
        pdf.cell(10,10,"Longitud",border=0, align="L")
        pdf.set_xy(105,95)
        pdf.cell(10,10,"Latitud",border=0, align="L")        
        pdf.set_xy(105,117)
        pdf.cell(10,10,"X:",border=0, align="L")
        pdf.set_xy(105,124)
        pdf.cell(10,10,"Y:",border=0, align="L")
        pdf.set_xy(105,137)
        pdf.cell(10,10,"Categoría:",border=0, align="L")
        pdf.set_xy(105,144)
        pdf.cell(10,10,"Observaciones:",border=0, align="L")
        pdf.set_xy(146,137)
        pdf.cell(10,10,"Estado:",border=0, align="L")
        pdf.set_xy(118,130)
        pdf.cell(10,10,"Alt. Elipsoide:",border=0, align="L")
        pdf.set_xy(136,109)
        pdf.cell(10,10,"DATUM ETRS89",border=0, align="L")
        pdf.set_font('Arial','',4)
        pdf.set_xy(159,98)
        pdf.cell(10,10,"Grados Sexagesimales",border=0, align="L")
        pdf.set_xy(138,112)
        pdf.cell(10,10,"Elipsoide GRS80",border=0, align="L")
        pdf.set_xy(175,131)
        pdf.cell(10,10,"Metros",border=0, align="L")
        
        
        #meto laS imagenES que sta en ruta
        pdf.image(foto,34,80,62,77,'jpg')
        pdf.image(orto,34,163,150,115,'jpg')
        pdf.image(junta,34,25,32,0,'jpg')
        
        #meto LOS TEXTOS VARIABLES
        pdf.set_font('Arial','',8)
        pdf.set_xy(162,60)
        pdf.cell(10,10,n_mojon,border=0, align="C")
        pdf.set_xy(90,50)
        pdf.cell(10,10,monte,border=0, align="C")
        pdf.set_xy(57,60)
        pdf.cell(10,10,n_monte,border=0, align="C")
        pdf.set_font('Arial','',7)
        pdf.set_xy(120,60)
        pdf.cell(10,10,municipio,border=0, align="C")
        pdf.set_xy(60,71)
        pdf.cell(10,10,provincia,border=0, align="C")        
        pdf.set_xy(115,71)
        pdf.cell(10,10,pertenencia,border=0, align="C")
        pdf.set_xy(140,87)
        pdf.cell(10,10,str(lon)+" W",border=0, align="C")
        pdf.set_xy(140,95)
        pdf.cell(10,10,str(lat)+" N",border=0, align="C")
        pdf.set_xy(145,117)
        pdf.cell(10,10,x,border=0, align="C")
        pdf.set_xy(145,124)
        pdf.cell(10,10,y,border=0, align="C")
        pdf.set_xy(155,130)
        pdf.cell(10,10,h,border=0, align="C")
        pdf.set_xy(128,137)
        pdf.cell(10,10,cat,border=0, align="C")
        pdf.set_xy(172,137)
        pdf.cell(10,10,estado,border=0, align="C")

        
        
        #guardo todo en el pdf
        pdf.output(ruta+str(contador)+".pdf","F")
        print contador

    
    
#al final habra que juntar todas las paginas del pdf en orden

    



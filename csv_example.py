import csv

from matplotlib.pyplot import close 

with open('archive/NetflixOriginals.csv','r') as csvfile:
    csvreader=csv.DictReader(csvfile)

    #with open('new_names.csv','w') as new_file:
      #  csv_writer= csv.writer(new_file)
        

    for line in csvreader:
        print(line['IMDB Score'])

# next(csvreader) satrıların ait  olduğu  kolonları  göstermez yani  indexi 1  den  başlatır
        
        #for line  in  csvreader:
            #csv_writer.writerow(line)     #açtığımız  yeni csv  dosyasındaki yerleri yukarıda belirlediğimiz delimeterla  yazıcak  
            #print(line)
            #print(line[4])  # listedeki elemanların ait olduğu  indexleri  seçmek

         
#! /bin/sh
set -x

#Generating seismograms

for i in $(ls *.bin| sed 's/.bin/ /') # loop varrendo uma lista
 do 
dado=$i
psimage n1=375 n2=369 <$dado.bin> $dado.ps d1=0.008 d2=0.025 label1='Profundidade (km)' label2='Afastamento (km)'  width=4.0 labelsize=18 height=2. d1num=1 d2num=2
ps2eps -B -r 800 $dado.ps
epstopdf $dado.ps  $dado.pdf
pdfcrop $dado.pdf aux.pdf
mv aux.pdf $dado.pdf
mv  $dado.pdf pdf/
rm *.ps *.eps 
#exit 0
done
exit 0

#tiro                       bclip=0.317733 wclip=-0.31947           

# modelo Chamine V          bclip=4500 wclip=1500  lend=4500  lbeg=1500  xbox=1.0 d1num=1.0 d2num=2.0 ldnum=1000 
# modelo Chamine Q          bclip=120 wclip=20  lend=140  lbeg=20  xbox=1.0 d1num=1.0 d2num=2.0 ldnum=40
# modelo Chamine Acustico 1 bclip=0.346664 wclip=-0.293298  lend=0.4  lbeg=-0.3  xbox=1.0 d1num=1.0 d2num=2.0 ldnum=0.3
# modelo Chamine Acustico   bclip=1.45177 wclip=-1.12465  lend=1.5  lbeg=-1.2  xbox=1.0 d1num=1.0 d2num=2.0 ldnum=0.8

#bclip=0.0157952 wclip=-0.0239571  lend=0.03 lbeg=-0.03 xbox=1.0 d1num=1.0 d2num=2.0 ldnum=0.03

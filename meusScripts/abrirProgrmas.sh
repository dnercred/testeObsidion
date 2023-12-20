#!/usr/bin/env bash

# comando pra iniciar O sicronismo Entre o Celular e o PC 


lista=("ls-R" "btop" "htop")

# verificacao=$(adb devices -l | grep -iEo '[0-9]{3}.[0-9]{3}.[0-9]+.[0-9]+[:][0-9]{4}')


#Esperar 5 segundos
sleep 5s


select menu in ${lista[@]}; do  
  case $REPLY in 
  
     # adb tcpip 5555 : Comando pra Restart   na porta 5555
     1) { ls-R ; echo "dar COmando Ls-R";  break ;};;						   
      	 echo "Atenção O celular que Esta conectado Na IP 192.168.0.4:5555 samsung " ; 
      break  ;};; 
     2) { adb tcpip 5555 ; adb connect 192.168.0.3:5555; 
    	 echo "Da O camando Btop" ;
    	 
      break  ;};;
     3) { htop ;
            echo "AbrirTerminal linux"; };;   
  
  esac 

done  

# start Pra inicar o Celular Espelhado

scrcpy 2>"${buracoNegro}" >"${buracoNegro}"
exit 1




# obs Importante de saber QUal o celular primeiro que esta conectado pois Interfere
 # Na coneção o celular Na Ordem Do mesmo


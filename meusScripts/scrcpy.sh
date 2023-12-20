#!/usr/bin/env bash

# comando pra iniciar O sicronismo Entre o Celular e o PC 

sansungIp="192.168.0.4:5555"
philcoIp="192.168.0.3:5555"
buracoNegro="/dev/null"
PS3="Escolha o celular pra conectar "
lista=("Sansung" "Philco" "HTOP")

verificacao=$(adb devices -l | grep -iEo '[0-9]{3}.[0-9]{3}.[0-9]+.[0-9]+[:][0-9]{4}')

echo -e "\E[31;2m${verificacao}\E[m"

sleep 5s

[[ "${verificacao}" = "${sansungIp}" ]] && adb disconnect "${sansungIp}" || adb disconnect "${philcoIp}"

select menu in ${lista[@]}; do  
  case $REPLY in 
  
     # adb tcpip 5555 : Comando pra Restart   na porta 5555
     1) { adb tcpip 5555  ; adb connect 192.168.0.4:5555; 						   
      	 echo "Atenção O celular que Esta conectado Na IP 192.168.0.4:5555 samsung " ; 
      break  ;};; 
     2) { adb tcpip 5555 ; adb connect 192.168.0.3:5555; 
    	 echo "Atenção O celular que Esta conectado Na IP 192.168.0.4:5555 samsung " ;
    	 
      break  ;};;
   
  esac 

done  

# start Pra inicar o Celular Espelhado

scrcpy 2>"${buracoNegro}" >"${buracoNegro}"
exit 1




# obs Importante de saber QUal o celular primeiro que esta conectado pois Interfere
 # Na coneção o celular Na Ordem Do mesmo


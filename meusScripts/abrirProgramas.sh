#!/usr/bin/env bash


 


listaComandos=("ranger" "btop" "htop" "psensor")

# verificacao=$(adb devices -l | grep -iEo '[0-9]{3}.[0-9]{3}.[0-9]+.[0-9]+[:][0-9]{4}')


#Esperar 2segundos
sleep 2s


select menu in ${listaComandos[@]}; do  
  case $REPLY in 
  
     
     1) { ranger ; 
          echo "Abrir gerenciador De Arquivos ranger" ; };;						   
      	  
     
     2) { btop ;  
           echo "Da O camando Btop" ; };;
     3) { htop ;
            echo "AbrirTerminal linux"; };;   
     4) { psensor ;
            echo "VEr Temperatura do computador e Seus nucleos" ; };;     
  
  esac 
done  




exit 1




# obs Importante de saber QUal o celular primeiro que esta conectado pois Interfere
 # Na coneção o celular Na Ordem Do mesmo


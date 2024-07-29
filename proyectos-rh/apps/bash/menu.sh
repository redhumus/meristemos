#!/bin/bash
trap ''2
while true
do
  clear
  fortune
  neofetch
  echo "=======================" "======================"
  echo "|                   Menu TAWANTISUYO           |"
  echo "|=======================" "====================|"
  echo "|=======================" "====================|" 
  echo "|0 HTOP                                        |"  
  echo "|                        |                     |"    
  echo "|1 Otra de  Fortune!!!   | 5 /proc/cpuinfo     |" 
  echo "|2 Entrar a ReDHumus     | 6 Bpytop            |"
  echo "|3 Entra RH con tunel    | 7  CAL              |"
  echo "|4 Actualizar JOSM       | 8  GOTOP            |" 
  echo "|9 NeoFetch              | 10 Journalctl -xe   |"
  echo "|11 Directorios + G      | 12 Archivos + G     |" 
  echo "|13 5 archivos + G       |                     |" 
  echo "|##############################################|"
  echo -e "Escriba su selección \c"
  read answer
  case "$answer" in

    0) htop;;
    1) fortune
       uptime;;
  #  2) ssh -L 7465:localhost:7465 omnibus@78.47.189.21;;

#    2) sudo service jupyterlab restart
 #       sudo systemctl status service.jupyterlab;;
    # 3) cd /home/omnibus/Documentos/twister-core
    #   ./twisterd -daemon -rpcuser=kublaykan -rpcpassword=L3gGag96YeWiSYKKk6sjgco9RQzfqs32GUtZvPrgkLdjHjaXo9aJ -rpcallowip=127.0.0.1 ;;
#    3) 	rm /etc/tomcat9/bundle.pfx 
#	rm /etc/tomcat9/cert.pem 
#	rm /etc/tomcat9/chain.pem  
#	rm /etc/tomcat9/privkey.pem
#	cd /etc/letsencrypt/live/redhumus.org
#	openssl pkcs12 -export -out bundle.pfx -inkey privkey.pem -in cert.pem -certfile chain.pem -password pass:claudina2 
#	cp cert.pem /etc/tomcat9/cert.pem 
#	cp chain.pem  /etc/tomcat9/chain.pem 
#	cp privkey.pem  /etc/tomcat9/privkey.pem 
#	cp bundle.pfx  /etc/tomcat9/bundle.pfx 
#	cd /etc/tomcat9
#	chown tomcat:tomcat cert.pem chain.pem privkey.pem bundle.pfx
#	service tomcat9 restart
#	exit ;;
#     3) env JAVA_HOME=/usr/lib/jvm/java-11-openjdk freemind ;;


   # 4) cd /etc/systemd/system

    3) ssh -L 3000:localhost:3000 0mn1bu5@redhumus.org -p 22039;;
     2) ssh  0mn1bu5@redhumus.org -p 22039;;

    4)	sudo mv /home/omnibus/Descargas/josm-tested.jar /usr/share/java/josm/josm.jar  ;;

    5) cat /proc/cpuinfo ;;
 #   5) cd /home/omnibus/apps/PharoLauncher-linux-2.0-x64/pharolauncher
#       ./pharo-launcher ;; 
  #  6) cd /home/omnibus/Documentos/BrigadaDigital/openstreetmapco.io
  #     cd _posts
  #     git status;;
  6) bpytop ;;      

 7) cal ;;
   # 8) cd /var/lib/tomcat7/webapps/geoserver/bin 
   #     JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64 nohup ./startup.sh & ;;  
    8) gotop -s --celsius  ;;
    9) neofetch ;;
    10) sudo journalctl -xe;;
    11) sudo du -xh / |grep '^\S*\+G'|sort -rn;;
    12) sudo find / -printf '%s %p\n'| sort -nr | head -10;;
    13) sudo  find / -xdev -type f -size +100M -exec ls -la {} \; | sort -nk 5;;
q) exit ;;
 esac
 echo -e "Oprima Enter para continuar\c"
 read input
done

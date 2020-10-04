echo "Welcome to Mult setup... Initializing"
echo "  __  __           _   _   
 |  \/  |         | | | |  
 | \  / |  _   _  | | | |_ 
 | |\/| | | | | | | | | __|
 | |  | | | |_| | | | | |_ 
 |_|  |_|  \__,_| |_|  \__|
                           (0.1)
                           "

# To Install
DESTDIR = /usr/local/bin
sudo cp hash.py $(DESTDIR)/mult && sudo chmod +x $(DESTDIR)/mult && echo "Installation Successful!"

# To uninstall:
	# sudo rm -f $(DESTDIR)/mult
	# echo "Mult has been removed"
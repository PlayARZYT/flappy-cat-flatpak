# flappy-cat-flatpak
Flappy Cat but flatpak! Linux and Raspberry Pi Game port.
# Welcome! Thank you for installing our small raspberry pi game!
# -Manual Installation, Download game only on the website (website coming soon!)-
1. Open terminal and paste: git clone https://github.com/PlayARZYT/flappy-cat-flatpak.git
2. Then, paste in: cd flappy-cat-flatpak
3. Then, paste in to build: flatpak-builder --force-clean build-dir org.playarz.flappycat.yml
4. Then, paste in this command to install app: flatpak-builder --user --install --force-clean build-dir org.playarz.flappycat.yml
5. If you want it to appear in the system as an app, do:
--If never installed flatpak before, do: sudo update-desktop-database ~/.local/share/applications/
--if ever installed any flatpak, do: sudo reboot (both commands will make the app appear but the app icon is for now systematic - a gear icon or else.)
7. Lastly, paste in this command to run: flatpak run org.playarz.flappycat
# Enjoy!

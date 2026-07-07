# flappy-cat-flatpak
Flappy Cat but flatpak! Linux and Raspberry Pi Game port.
# Welcome! Thank you for installing our small raspberry pi game!
# !Make sure you have aarch64! to check, open Terminal and run: uname -m. Or else wont work! 
# -Manual Installation, Download game only on the website (website coming soon!)-
1. Open terminal and paste: git clone https://github.com/PlayARZYT/flappy-cat-flatpak.git
2. Then, paste in this command to check for flatpak: flatpak remote-add --if-not-exists flathub https://flathub.org
3. Then, install the .yml SDK if missing: flatpak install flathub org.freedesktop.Sdk/aarch64/23.08
  -- Then / Or, install User Scope: flatpak install --user flathub org.freedesktop.Sdk/aarch64/23.08
  -- And System Scope: sudo flatpak install flathub org.freedesktop.Sdk/aarch64/23.08
4. Then, verify SDK installation by running: flatpak list --runtime | grep 23.08
5. Then, paste in: cd flappy-cat-flatpak
6. Update and install builder: sudo apt update && sudo apt install -y flatpak-builder
7. Then, paste in to build: flatpak-builder --force-clean build-dir org.playarz.flappycat.yml
8. Then, paste in this command to install app: flatpak-builder --user --install --force-clean build-dir org.playarz.flappycat.yml
9. If you want it to appear in the system as an app, do:
  --If never installed flatpak before, do: sudo update-desktop-database ~/.local/share/applications/
  --if ever installed any flatpak, do: sudo reboot (both commands will make the app appear but the app icon is for now systematic - a gear icon or else.)
10. Lastly, paste in this command to run: flatpak run org.playarz.flappycat
# Enjoy!

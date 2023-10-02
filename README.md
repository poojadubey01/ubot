# Ubot Installation Guide 🤖

Follow these simple steps to install Ubot on various operating systems, including Termux on mobile, Windows, macOS, and Linux, and enjoy its amazing features! 🚀

## Prerequisites 📋

Before you begin, ensure that you have the following prerequisites:

- **Python**: You need Python installed on your system. If you don't have it, you can download it from [python.org](https://www.python.org/downloads/).

- **Git**: You also need Git installed to clone the Ubot repository. You can download it from [git-scm.com](https://git-scm.com/downloads).

## Installation 🚀

### Termux (Mobile):

1. Open the Termux app on your mobile device.

2. Run the following commands to install Ubot:

   ```shell
   pkg update && apk upgrade -y
   apt install termux-api
   apt install nodejs
   pkg install git
   pkg install python
   termux-setup-storage
   cd storage/downloads
   git clone https://github.com/poojadubey01/ubot
   cd ubot
   pip install -r requirements.py
   python ubot.py
   ```

### Windows, macOS, and Linux:

1. Open your command-line terminal or shell.

2. Clone the Ubot repository using Git:

   ```shell
   git clone https://github.com/poojadubey01/ubot
   ```

3. Navigate to the Ubot directory:

   ```shell
   cd ubot
   ```

4. Install the required Python packages using pip:

   ```shell
   pip install -r requirements.py
   ```

5. Start Ubot:

   ```shell
   python ubot.py
   ```

## Checking the Output 📂

After running Ubot, you can check the output file named `getbenefits.txt` in the same directory where you cloned the Ubot repository.

## Note 📝

This installation process is suitable for Termux (Mobile), Windows, macOS, and Linux. Enjoy using Ubot on your preferred operating system! 🤖✨

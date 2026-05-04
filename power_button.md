<h1>Power Button - Work instructions</h1>
<h3>How to reboot/shutdown your Raspberry Pi's with an arcade led button.</h3>

<img src="https://github.com/aktendo79/post_img/blob/main/photo_5983389584139685497_y.jpg" width="400">

<p>The button I used is a standard arcade led button with 5 faston, we will use 4 of that for this project.</p>

<img src="https://github.com/aktendo79/post_img/blob/main/photo_5983389584139685498_y.jpg" width="400">

<p>Connections:
  <ul>
    <li>faston on the left -> GND</li>
    <li>faston on the top -> GND (you can use a single connection linking the faston on the left with this one)</li>
    <li>faston on the front, upper one -> GPIO17</li>
    <li>faston on the right -> GPIO4</li>
  </ul>
</p>

<h2>1. Save the script</h2>

Put the script here for example:<br>
<pre>/home/alessia/power_button.py</pre>
Then make it executable:<br>
<pre>chmod +x /home/alessia/power_button.py</pre>

<h2>2. Create the service systemd</h2>

Open:<br>
<pre>sudo nano /etc/systemd/system/power-button.service</pre>
Paste:<br>
<pre>
[Unit]
Description=Shutdown Button Service (PPB)
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/alessia/power_button.py
Restart=always
User=alessia

[Install]
WantedBy=multi-user.target
</pre>

<h2>3. Activate the service</h2>
<pre>
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable shutdown-button.service
sudo systemctl start shutdown-button.service
</pre>

<h2>4. Test it</h2>

Check the status:<br>
<pre>sudo systemctl status shutdown-button.service</pre>

It must be:<br>
<pre>active (running)</pre>

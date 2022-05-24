# Contact list with Socket

We are from [fit@hcmus](https://www.fit.hcmus.edu.vn/vn/), and this is our practice project for Computer Networking course (CSC10008). 

Our app manages a digital contact list using Socket programming, with TCP at Transport Layer. This contact list is stored at server side, and the server provides services for clients that they can request for contact information.


## Try our app

Get the lastest version of our app by following these steps
```bash
curl -fsSL github.com/htrvu/contact-list-with-socket/releases/latest/download/DigitalContact.zip -O
unzip -q DigitalContact.zip -d DigitalContact
```

## Build the app from source codes

Firstly, you must have `pyinstaller` installed. Then, follow these steps:

### 1. Clone this repository
```bash
git clone https://github.com/htrvu/contact-list-with-socket.git DigitalContact
cd DigitalContact
```

### 2. Build the source codes
#### a. Client
```bash
cd ./source/client # path to client folder
pyinstaller main.spec
```

#### b. Server
```bash
cd ../server # path to server folder
pyinstaller main.spec
```

#### c. Remove unnecessary stuffs
```bash
cd .. # path to source folder
mv client/dist/DigitalContact.exe client/DigitalContact.exe
mv server/dist/DigitalContact-Server.exe server/DigitalContact-Server.exe
rm -r client/dist client/build server/dist server/build
```

[//]: <add some screenshots>
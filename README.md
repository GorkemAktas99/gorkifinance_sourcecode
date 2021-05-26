# What is This ?
It is the source code of the container that enables the visualization of crypto finance data that I have prepared using Docker and Python. 
If the system you are running has Docker installed, you can easily pull the image with gorkemaktas99/gorkifinance:latest

# How to Create a new Image from it?
- First of all, you need to download the source files located here. For this, you can follow any step that allows you to get a repository on github. 
- Then go to the directory containing these files on a machine with Docker installed. 
- Then make sure you are in this directory and enter the command line below. You can use the "pwd" command to find your place. 
- "sudo docker image build -t [The name you set for the image ] ."
- After the compilation process is finished, you can check whether it is with the command line below. 
- "sudo docker image ls"
- If you can see the tag you used while creating the image on the top line, it means that the image file has been created successfully. 

# How to Use ?
- First of all, open your terminal screen where you can access Docker. 
- Then enter the code below on the terminal screen. 
- "sudo docker container run --network=host gorkemaktas99/gorkifinance:latest"
- With this code, if the image file is not in your local storage, the image file will be extracted from DockerHub. 
- Then an info screen will appear, informing you of usage instructions. 
# How to Get Only Image for Docker
You can use the following code to get it as an image file without running it as a container on your system. 
- "sudo docker pull gorkemaktas99/gorkifinance:version1.0.0 "
Or get latest version
- "sudo docker pull gorkemaktas99/gorkifinance:latest"
# Important Note 
The library of mpld3 used for data visualization wants to access your localhost. That's why --network = is set as host. If you do not use it, only 7 days of data will be displayed on your terminal screen. You can examine the source files. You do not have to run any file you do not trust. You are responsible for unexpected events on your network or computer. 

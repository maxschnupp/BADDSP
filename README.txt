BUILDING:
sudo docker build -t baddsp ./

RUNNING/OPENNING: 
sudo docker run -it baddsp


To Train: 

* Start a GPU instance on GCS and attach a disk 

* Connect by SSH and mount https://cloud.google.com/compute/docs/disks/add-persistent-disk

* Change docker image installation registry to disk with a symlink https://forums.docker.com/t/how-do-i-change-the-docker-image-installation-directory/1169

* build sudo docker build -t baddsp ./

* run sudo docker run -it baddsp

* train python3 main.py --train <instrument-name>
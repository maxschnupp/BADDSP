### BUILDING:
sudo docker build -t baddsp ./

### RUNNING/OPENNING: 
sudo docker run -it baddsp


### TRAINING: 

* When restarting an instance you will have to reinstall docker before moving on to the symlink step

* Start a GPU instance on GCS and attach a disk 

* Connect by SSH and mount https://cloud.google.com/compute/docs/disks/add-persistent-disk

* Change docker image installation registry to disk with a symlink https://forums.docker.com/t/how-do-i-change-the-docker-image-installation-directory/1169

* upload `serviceKey.json` to `/app`

* build: `sudo docker build -t baddsp ./`

* run: `sudo docker run -it baddsp`

* train: `python3 main.py --train instrument-name`

### TRANSFER: 

* input files should be put in the audioIn folder after transfer they will be available in audioOut and also in the bucket

* single file: `python3 main.py --transfer source-file-name.wav output-file-name.wav label` the label will be prepended to the file name in the bucket

* all files `python3 main.py --transferAll label` will iterate through the entire directory and transfer timbre for all files
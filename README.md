###### This is a simple collection of python scripts for ROS
Version of ROS: ROS 2
Running on:  Ubuntu 18.04.5 LTS


###### ROS package "topics" contains:
- One topic publisher **publisher.py**
- Two subscribers subbing to different topics:
- - **smarphone1.py** listening to topic *publish1*
- - **smarphone2.py** listening to topic *publish2*
- Topic switcher **switcher.py**
- launch file **publishing.launch**


###### + simple script to switch topics manually:
- topicSwitcher.py

It's fairly easy to find example code for publishers and subscribers, but it is way harder to find real-time topic switchers. I would recommend using a launch file and setting a specific parameter for a topic in there.
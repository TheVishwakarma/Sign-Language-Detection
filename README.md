Steps to run this project on your local computer:

> Download the main project folder

> Cut and paste the folder in your PC (C drive)

> open pycharm IDE on your PC

> open the folder as project

> check your interpreter

> create a virtual environment for your project

> open new terminal in Pycharm (In the terminal window)
  Install the packages using command - pip install -r requirements.txt
   

> Run the script- collect_imgs.py (Make sure your camera is facing your hand for gestures in front of the lense)
	1. Collect the data (Frame popup window will appear make your hand gesture of A, B, C, D and so on)
		a) (For the Sign letter A) press Q and it will start clicking 100 images to collect the images for your dataset
		b) you have to press Q for 31 times for each letter everytime "Q" appears in the frame poopup window until letter
		 "Z" and few words listed as 'Thank you','Yes','No','Hello', 'I Love you'
	2. Run the script- create_dataset.py (it will create the dataset using all the images stored on your data folder
	in the project directory) wait for the process to finish.
	3. Run the script- train_classifier.py (this will train the model for your web application) wait for the process to finish.
	4. Run the script in terminal window- Sign_language_detection.py (this will open the web application on your local web browser)
	streamlit run your-path-to-main-folder\Sign_language_detection.py
	copy this command and paste into the local terminal window and hit enter
> ![image](https://github.com/TheVishwakarma/Sign-Language-Detection/assets/86587324/8b81b7bd-1999-40e2-aba9-653bf8f47a6f)

	5. goto the web browser and select the web cam from the App mode in the left sidebar and click on use webcam
![image](https://github.com/TheVishwakarma/Sign-Language-Detection/assets/86587324/48ed8b71-8ff4-4881-85eb-bf181369de4d)

Make Sign language hand gestures of letter and it will show the letter and words in the video output window.
![image](https://github.com/TheVishwakarma/Sign-Language-Detection/assets/86587324/55bcc567-a687-400b-85bc-55d1972f23c1)

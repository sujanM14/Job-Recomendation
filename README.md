   
<h1 align="center">ConnectionHire</h1>       

  

Job seekers and recruiters struggle to find the right match for open job positions, leading to a time-consuming and inefficient recruitment process. ConnectionHire offers a solution to this problem with its advanced technologies that provide personalized job and candidate recommendations based on qualifications and experience.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

      
<h1 align="center">Aim</h1>

The job search process can be daunting and time-consuming for both job seekers and recruiters. That's where this app comes in!

This app is designed to assist applicants in searching for potential jobs and to help recruiters find talented candidates. The app offers a user-friendly interface that allows applicants to easily browse and search for job opportunities based on their preferences and qualifications. Users can create a profile, upload their resumes, and set up job alerts to receive notifications about new job postings that match their criteria. The app also provides helpful tips and resources for applicants, such as resume writing guides and interview preparation tips.

Recruiters can use this app to post job openings, search for candidates based on their qualifications, and view applicant profiles and resumes. The app's advanced search features allow recruiters to narrow down their search to find the most qualified candidates quickly. The app also includes features for scheduling interviews and communicating with applicants directly through the app.

Overall, this app is an excellent tool for both job seekers and recruiters, making the job search and hiring process more efficient and effective.
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h1 align="center">Business Values</h1>

- ConnectionHire brings the job world to you
- Simple to use : Drag and Drop
- Saves time
- Tailor-made dashboard
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h1 align="center">Project Flow</h1>

<p align="center">
  <img src="https://user-images.githubusercontent.com/71117423/224474003-f2916799-12c9-4323-8908-70f88821ed91.png" />
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h1 align="center">Solution</h1>

# JOB SEEKERS

<p align="center">
  <img src="https://user-images.githubusercontent.com/71117423/220825934-01f5a912-6325-4d3a-9592-f9b71ccc77d7.png" />
</p>

To assist job seekers, the process begins with uploading their CV to ConnectionHire. The CV is then processed by Optical Character Recognition (OCR) technology and undergoes Natural Language Processing (NLP). The NLP process compares the uploaded CV with various job postings to determine the best match based on similarity. Finally, the system provides a list of recommended jobs that match the user's qualifications and experience.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

# RECRUITERS

<p align="center">
  <img src="https://user-images.githubusercontent.com/71117423/220825926-5525e522-7a4f-4e4f-823b-46a4bf82c94f.png" />
</p>

For recruiters, the process begins with inputting the job post into ConnectionHire. The job post undergoes NLP analysis alongside the CVs in the database. Using various comparison methods, ConnectionHire identifies the best-matching candidates for the job posting. The system then provides a list of recommended candidates to the recruiter based on their qualifications and experience.

# RESUME ANALYZER

To extract user information from a resume, various features are analyzed. Firstly, the resume score is calculated based on the completeness of the information provided, the relevance to the job, and the overall layout. Career recommendations are then suggested based on the user's experience and education, which can help them target the right job opportunities. Additionally, resume writing tips are provided to improve the resume's overall effectiveness. Courses recommendations are also suggested based on the user's education and job preferences, which can help them acquire new skills and knowledge. Finally, skills recommendations are suggested based on the user's work experience and industry trends, which can help them stay competitive in the job market.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h1 align="center">Installation</h1>

- ## Cloning the Repository :

  git clone 
  cd Job-Recomendation
  Creating Conda Environment :

  conda create -n envname python=3.8
  conda activate envname

  Installing Required Packages :
  pip install -r requirements.txt

  Streamlit
  streamlit run HOME.py

-----------------------------------------------------
<h1 align="center">Data Collection</h1>
<p align="center">
  <img src= "https://user-images.githubusercontent.com/71117423/220715830-f4b4a5b8-8b6c-4cfd-b4b2-342761a1cf4c.png">
</p>

With web scraping restricted on job search engines like Indeed, we turned to Apify to collect relevant job-related data. Utilizing Apify's advanced tools and automation capabilities, we were able to efficiently and accurately extract large volumes of data. This enabled us to provide up-to-date and precise job postings and candidate recommendations to job seekers and recruiters.

-----------------------------------------------------
<h1 align="center">MongoDB</h1>

We are retrieving data from a MongoDB database job recommendation, which is comprised of three distinct collections: Resume_Data, all_locations_Data, and preprocessed_jobs_Data whhere as there are two more collection inside the same database which are Resume_from_CANDIDATE and Resume_from_RESUME_ANALYZER in order to store resumes entered by users on the job recommendation and resume analyzer pages. These collections will serve as a repository for user-provided resumes, allowing for more personalized and accurate job recommendations and analysis.

-----------------------------------------------------
<h1 align="center">Optical Character Recognition</h1>
<p align="center">
  <img width="1000" src="https://user-images.githubusercontent.com/71117423/220715830-f4b4a5b8-8b6c-4cfd-b4b2-342761a1cf4c.png" />
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/71117423/220832148-85e134ff-ed29-44a8-922c-83c6fc847790.png" />
</p>

By utilizing Optical Character Recognition (OCR) technology, we were able to convert a PDF document containing textual data into a machine-encoded text format that can be further processed and analyzed in a Jupyter Notebook. OCR is an advanced technology that enables the automatic conversion of scanned documents and images into machine-encoded text that can be easily manipulated and analyzed. By leveraging OCR technology, we were able to extract valuable insights from the textual data, enabling us to gain a deeper understanding of the information contained within the document.
-----------------------------------------------------
<h1 align="center">Natural Language Processing</h1>
Data preprocessing is an essential step in building a Machine Learning model and depending on how well the data has been preprocessed; the results are seen.

In NLP, text preprocessing is the first step in the process of building a model.

Some text preprocessing steps used are:
<p align="center">
  <img src="https://user-images.githubusercontent.com/71117423/220833096-10719ee1-0e85-476d-9836-62456a61a22e.png" />
</p>

    Word tokenization:
    Stop words removal
    Lemmatization
    Bigram Collection Finder

-----------------------------------------------------
<h1 align="center">Optimizations</h1>

    Enhance the recommendation system to deliver precise and pertinent outcomes: Improve the recommendation system through advanced algorithms and data analysis techniques like using different deep learning Word Embeddigs.

    Establish a relationship with job posting firms to procure database/API access: Engage with job posting companies to gain access to their databases or APIs, expanding the range of job listings available on our platform and make it realtime.

    Encourage candidates to become part of the CV database: Increase the number and quality of CVs in our database by inviting the applicants.

-----------------------------------------------------
<h1 align="center">Conclusion</h1>
In summary, 
ConnectionHire utilizes advanced technologies such as OCR and NLP to provide job seekers and recruiters with personalized job and candidate recommendations. Additionally, the use of Apify allows for efficient and accurate data collection, leading to up-to-date and relevant job postings. ConnectionHire streamlines the recruitment process, saving time and resources for both job seekers and recruiters.# Job-Recomendation
# Job-Recommendation
# Job-Recomendation

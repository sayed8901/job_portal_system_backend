# BD Job Portal Project Backend

## Project Description

**Project Name**: BD Job Portal Project

## Overview

The **BD Job Portal** Project Backend provides a robust platform for managing job listings and applications. Built with **Django** and **Django REST Framework**, it allows for seamless interaction between `employer` (Employer) and `job seeker` (Job seeker).

Employers can create and manage job postings, while job seekers can browse, apply, and track their applications. The project also includes features like role-based access control, email notifications, and user dashboards, making it a comprehensive solution for **job portal management**.

Additionally, the use of **PostgreSQL** ensures reliable data handling and scalability, while maintaining flexibility for future enhancements.

---

<br>

## Technology Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: PostgreSQL (with supabase deployment)

---

<br>

## Project Features

### User Authentication

- User roles: Employers and Job Seekers.
- Users can register for an account and log in.
- Users can log out.

### Job Listings

- Employers can create job listings by providing details such as job title, description, requirements, and location.
- Job listings contain key information, such as the job title, company name, and date posted.

### Job Details

- Users can view detailed information about a job listing, including the job description, requirements, and application instructions.
- Job seekers can apply to a job by uploading their resume and providing other information (such as salary expectations).

### User Dashboard

- Employers have a dashboard to manage their posted job listings, view applications, and update job details.
- Job seekers have a dashboard to track their applications.

### Job Categories

- Jobs can be categorized based on industries, making it easier for users to find relevant listings.

### Email Notifications

- Send email notifications to users when they successfully apply for a job or when an employer receives a new application.

---

<br>

## Instructions to Run Locally

### Prerequisites

- Python 3.12.2
- Django 4.2.4
- Django REST Framework 3.15.2
- PostgreSQL

### Packages used:

```bash
asgiref==3.8.1
certifi==2024.8.30
charset-normalizer==3.3.2
dj-rest-auth==6.0.0
Django==4.2.4
django-allauth==0.63.3
django-cors-headers==4.4.0
django-environ==0.11.2
django-filter==24.3
djangorestframework==3.15.2
idna==3.10
Markdown==3.7
psycopg2-binary==2.9.9
requests==2.32.3
sqlparse==0.5.1
tzdata==2024.2
urllib3==2.2.3
whitenoise==6.7.0
```

---

<br>

### Installation Steps

1. Open `command prompt` in the folder directory where you want to create & run the project locally

2. Copy the `repository_url` to **Clone the repository**

   ```bash
   git clone https://github.com/sayed8901/job_portal_system_backend.git
   cd job_portal_system_backend
   ```

3. **Create a virtual environment**

   ```bash
   python -m venv job_portal_venv
   cd job_portal_venv
   Scripts\activate.bat
   cd ..
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   code .
   ```

<br>

5. **Environment Variables Configuration**

- `N.B.`: To run the application, you need to configure environment variables. Create a file named `.env` inside the root project directory of your project named `job_portal_system`.

<br>

6. **Then, add the `SECRET_KEY` in that `.env` file:**

- SECRET_KEY=(Your SECRET_KEY)

      --> N.B.: please see the `### Note for: Getting the SECRET_KEY` part for better understanding

- Copy the `secret key` from the temporarily created project's `temp_settings.py` file

<br>

7. **Add the supabase postgreeSQL database credentials** in `.env` file:

- DB_NAME=(Your database name)
- DB_USER=(Your database username)
- DB_PASSWORD=(Your database password)
- DB_HOST=(The host for your database)
- DB_PORT=(The port for your database)

      --> N.B.: please see the `### Note for: Database Setup` part for better understanding

<br>

8. **Also, Add the email sending accessibility credentials** in `.env` file:

- EMAIL: (Your email address for sending emails)
- EMAIL_PASSWORD: (Your email password or an app-specific password)

      --> N.B.: please see the `### Note for: Email Setup` part for better understanding

<br>

9. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

10. **Creating superuser**

```bash
python manage.py createsuperuser
```

11. **Run the development server**

```bash
python manage.py runserver
```

<br>

12. **Finally, Access the application**

- Local: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/login/

---

<br>

## 13. Extra Note for: Getting the `SECRET_KEY`

1. **to get the `SECRET_KEY`, Temporarily `Create a new project` named `temp_job_portal_system` anywhere `outside the current project directory` (may be in the `desktop`, `documents` or `downloads`, wherever you want, just outside the current project directory)**

   ```bash
   django-admin startproject temp_job_portal_system
   ```

   <br>

2. **After creating a project named `temp_job_portal_system`,**

- Manually go to that `temp_job_portal_system` project directory folder to get the `settings.py` file.
- Rename that `settings.py` file to `temp_settings.py`
- Copy that `temp_settings.py` file and paste it to a temporary directory like `desktop` or `documents` folder.

3. **Delete the project** named `temp_job_portal_system`

- As we have already copied the `temp_settings.py` file from the `temp_job_portal_system` project, now we can delete it.
- So now, Manually delete the `temp_job_portal_system` project directory

---

<br>

## 14. Extra Note for: Database Setup

1. **Setting up in supabase:**

- Go to `supabase.com` and log in with your `GitHub` account.
- Navigate to the dashboard and click on **New project**.
  - Select your organization (e.g., `sayed8901’s Org`).
  - Provide a relevant project name (e.g., `hr_corp-db`).
  - Set a strong database password (consider using a password generator) and make sure to copy it, as you will need it later.
  - Choose the **Region** as **South Asia (Singapore)** and click **Create new project**.

2. **Updating settings.py:**

- Make sure to replace the default SQLite database settings with PostgreSQL settings in your `settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
```

3. **Update the .env file:**

- In your .env file, replace/update the values for `DB_NAME`, `DB_USER`, `DB_HOST`, and `DB_PORT` based on your supabase database configuration.
- You should also set `DB_PASSWORD` with the password you generated earlier.

```python
DB_NAME=postgres
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```

**To find the required database connection details in supabase:**

- Go to the `supabase dashboard` and select your project.
- Choose the `database` option from the left sidebar.
- Alternatively, you can select the `connect` button from the top-right corner.
- Select the `Python` tab from the `Connection string`
- and go to `Connection parameters` for your database details.

---

<br>

## 15. Extra Note for: Email Setup

To set up email notifications for your Django application, follow these steps:

1. **Getting App Password**:

   - Log in to your `Google` account.
   - Click on your account profile image and select **Manage your Google Account**.
   - Navigate to the **Security** tab.
   - Enable **2-Step Verification** if it is not already enabled.
   - After enabling, scroll down and click on **App passwords**.
   - Provide an app name (e.g., `hrcorp`) and click **Create**. A `password` will be generated; copy this password;
   - paste this `password` onto the `EMAIL_PASSWORD` field in the `.env` file.

2. **Updating project settings.py**:

   - In your `settings.py` file, make sure to set up the email configuration as follows:

   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_USE_TLS = True
   EMAIL_PORT = 587
   EMAIL_HOST_USER = env("EMAIL")
   EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
   ```

---

<br>

## Getting Started

To unlock and access the full functionality of this site and to perform some role-specific activities, you will need to create an account first. Follow the instructions below to get started.

### Create an Account

- To register as an **Employer**: Visit `/employer/register`.
- To register as a **Job Seeker**: Visit `/job_seeker/register`.

#### Steps to Register:

1. Fill out the registration form with the relevant information and click the **POST** button.
2. A confirmation link will be automatically sent to your email. Please check your inbox.
3. Verify your account by clicking on the confirmation link provided in the email.
4. After verification, return to the project site and navigate to `/accounts/login` to log in with your credentials.

### Role-Based Activities

Once logged in, you can perform activities specific to your role. For a full list of available actions, you can check out the **`API Endpoints`** section below.

---

<br>

## API Endpoints

### User Management

- **Register Employer**:  
  `POST` - `/employer/register/`  
  Allows creating a new employer account.

- **Register Job Seeker**:  
  `POST` - `/job_seeker/register/`  
  Allows creating a new job seeker account.

- **Admin Login**:  
  `POST` - `/admin/login/`  
  Allows the admin to log in.

- **User Login**:  
  `POST` - `/accounts/login/`  
  Allows an employer or job seeker to log in.

- **User Logout**:  
  `GET` - `/accounts/logout/`  
  Logs out an employer or job seeker.

- **User Account Data by User ID**:  
  `GET` - `/accounts/user/?user_id=<id>`  
  Retrieves the account details of a user by their ID.

### Employer Management

- **List Employers**:  
  `GET` - `/employer/list/`  
  Returns a list of all employers.

- **Retrieve/Update/Delete Specific Employer**:  
  `GET` `PUT` `PATCH` `DELETE` - `/employer/list/<id>/`  
  Allows retrieving, updating, or deleting a specific employer.

- **Get Employer by User ID**:  
  `GET` - `/employer/by_user_id/?user_id=<id>`  
  Retrieves employer details using their user ID.

### Job Seeker Management

- **List Job Seekers**:  
  `GET` - `/job_seeker/list/`  
  Returns a list of all job seekers.

- **Retrieve/Update/Delete Specific Job Seeker**:  
  `GET` `PUT` `PATCH` `DELETE` - `/job_seeker/list/<id>/`  
  Allows retrieving, updating, or deleting a specific job seeker.

- **Get Job Seeker by User ID**:  
  `GET` - `/job_seeker/by_user_id/?user_id=<id>`  
  Retrieves job seeker details using their user ID.

### Category Management

- **List All Categories**:  
  `GET` - `/category/`  
  Returns a list of all job categories.

- **Retrieve/Update/Delete Specific Category**:  
  `GET` `PUT` `DELETE` - `/category/<id>/`  
  Allows retrieving, updating, or deleting a specific category (only accessible to employers).

### Job Post Management

- **List All Job Posts**:  
  `GET` - `/job_posts/all/`  
  Returns a list of all job posts.

- **Retrieve/Update/Delete Specific Job Post**:  
  `GET` `PUT` `DELETE` - `/job_posts/all/<id>/`  
  Allows retrieving, updating, or deleting a specific job post (only accessible to the employer who posted it).

- **Create a New Job Post**:  
  `POST` - `/job_posts/publish/?employer_id=<id>`  
  Allows an employer to create a new job post.

- **List Employer's All Advertisements**:  
  `GET` - `/job_posts/my_advertisements/?employer_id=<id>`  
  Returns a list of job posts by a specific employer.

- **List of All Job Posts by Category**:  
  `GET` - `/job_posts/job_posts_of_a_category/?slug=<category_slug>`  
  Returns job posts filtered by category.

### Job Application Management

- **List All Job Applications**:  
  `GET` - `/job_applications/all/`  
  Returns a list of all job applications.

- **Retrieve/Update/Delete Specific Job Application**:  
  `GET` `PUT` `DELETE` - `/job_applications/all/<id>/`  
  Allows retrieving, updating, or deleting a specific job application (only accessible to the applicant who submitted it).

- **Submit a Job Application**:  
  `POST` - `/job_applications/apply/?job_post_id=<id>&job_seeker_id=<id>`  
  Allows a job seeker to apply to a job post.

- **Check If a Job Seeker Already Applied**:  
  `GET` - `/job_applications/check_application/?job_post_id=<id>&job_seeker_id=<id>`  
  Checks if a specific job seeker has already applied for a job post.

- **List of Applications for an individual Job Seeker**:  
  `GET` - `/job_applications/my_applications/?job_seeker_id=<id>`  
  Returns a list of applications by a specific job seeker.

- **List of Applications for a single Job Post**:  
  `GET` - `/job_applications/applications_for_a_job_post/?job_post_id=<id>&employer_id=<id>`  
  Returns a list of applications for a specific job post (only accessible to the employer who posted it).

---

<br>

## Sample requests for model schemas:

### Publish new job post : POST

```bash
     {
        "employer": 2,
        "job_title": "Assistant Officer (IT)",
        "job_location": "Head Office",
        "employment_status": "permanent",
        "job_context": "Job Summary: This is an important entry-level position to contribute to MSS's growth and development by providing services with the existing IT team. This position is expected to perform and ensure smooth operation of day to day IT related services of the organization. The position is based in Dhaka and requires field visits on purpose.",
        "job_responsibilities": "* Install and configure computer hardware operating systems and applications as per requirement.\r\n* Frequent monitor and maintain computer systems and networks.\r\n* Setting up workstations with computers and necessary peripheral devices.\r\n* Develop and maintain local networks in ways that optimize performance.\r\n* Ensure security and privacy of networks and computer systems including anti-virus.\r\n* Sound knowledge in repairing and servicing of computers, laptops, laser printers, ink printers and other IT devices.\r\n* Develop, maintain and support all dynamic web portals/content management systems.\r\n* Perform, handle & take care of communication with staff through a series of actions either face-to-face, over the phone or virtual meeting tools to help set up systems or resolve issues.\r\n* Troubleshoot system and network problems; diagnose and solve hardware or software malfunctions.\r\n* Provide frequent support, including procedural documentation and relevant reports.\r\n* Set up new users' accounts and profiles and deal with access issues on necessary systems.\r\n* Test and evaluate new technology.\r\n* Generate weekly, monthly, quarterly or yearly reports as per the requirement of the management.\r\n* Effectively plan, organize, conduct, and coordinate necessary IT or system related training & workshops.\r\n* Record keeping and proper documentation as per organization practice.\r\n* Distribution and record keeping of various IT related products.\r\n* Maintain IT asset register, inventory and transfer process.\r\n* Undertake any other related duties and responsibilities that may be assigned from time to time.",
        "education": "BSC in Computer Science & Engineering/ Computer Science/ Telecommunication Engineering or any IT related subject from a reputed university with good academic records (No 3rd class/ division will be allowed). Professional courses in relevant subjects will get added advantage.",
        "experience": "* At most 2 years\r\n* The applicants should have experience in following business area(s):\r\nNGO\r\n* Freshers are also encouraged to apply.",
        "age": 32,
        "vacancy": 1,
        "salary": 22000,
        "other_benefits": "T/A, Mobile bill, Tour allowance, Medical allowance, Contributory Provident fund, Gratuity, Two festival bonuses in a year, yearly increment, special \"Staff Welfare Fund\" to cover health expenses for self and family. The death benefit from a Special \"Staff Welfare Fund\". Stipend facility for meritorious children.",
        "deadline": "2025-07-25",
        "application_instructions": "If you fulfil our requirements and think yourself confident as the best fit, you are requested to send your CV (including two professional references) along with a cover letter (CV & cover letter should be in one MS Word or PDF file) addressed to the Executive Director, MSS through e-mail to: hr@mssbd.org or Apply online on or before July 28, 2024.\r\n\r\nPlease mention the position applied for in the subject line of the e-mail. We treat all applications for employment on their merits. Any persuasion will disqualify the candidature. MSS reserves the right to cancel any application. Only short-listed candidates will be invited to the selection process.",
        "job_category": [
            1,
            3
        ]
    }
```

<br>

## Conclusion

In developing the **Job Portal Project** backend, the goal was to create an efficient and scalable platform for managing job advertisements and applications. By leveraging **Django** and **PostgreSQL**, I ensured a secure and robust system that allows **employers** and **job seekers** to interact seamlessly.

I believe the platform's features, including role-based access, job management, and application tracking, will significantly improve the hiring process for organizations and make job seeking more efficient.

I am excited to see the positive impact this system can bring, and if you have any questions or would like to contribute, feel free to reach out!

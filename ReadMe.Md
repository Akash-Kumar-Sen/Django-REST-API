# API Service for CRUD 
This is a basic CRUD-based API with Python-Django and Django REST Framework.
PS : CRUD Stands for create-read-update-delete

## Tech Stack
![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

## Features
Consider a store which has an inventory of boxes which are all cuboid(which have length breadth and height). Each Cuboid has been added by a store employee who is associated as the creator of the box even if it is updated by any user later on. 

1. Data Modelling

    Build minimal Models required for the such a store. You can use contrib modules for necessary models(for eg: users)

2. Add Api: 

    Adding a box with given dimensions(length breadth and height). 

    Adding user should be automatically associated with the box and shall not be overridden

    Permissions:

          User should be logged in and should be staff to add the box

3. Update Api:

    Update dimensions of a box with a given id:

    Permissions:

          Any Staff user should be able to update any box. but shall not be able to update the creator or creation date

4. List all Api

    List all boxes available:

    Data For each box Required:

            1. Length

            2. width

            3. Height

            4. Area

            5. Volume

            6. Created By :  (This Key shall only be available if requesting user is staff)

            7. Last Updated :  (This Key shall only be available if requesting user is staff)

    Permissions:

            Any user shall be able to see boxes in the store

    Filters:

            1. Boxes with length_more_than or length_less_than

            2. Boxes with breadth_more_than or breadth_less_than

            3. Boxes with height_more_than or height_less_than

            4. Boxes with area_more_than or area_less_than

            5. Boxes with volume_more_than or volume_less_than

            6. Boxes created by a specific user by username

            7. Boxes created before or after a given date

5. List my boxes:

    List all boxes available created by me:

    Data For each box Required:

            1. Length

            2. width

            3. Height

            4. Area

            5. Volume

            6. Created By

            7. Last Updated

    Permissions:

            Only Staff user shall be able to see his/her created boxes in the store

    Filters:

            1. Boxes with length_more_than or length_less_than

            2. Boxes with breadth_more_than or breadth_less_than

            3. Boxes with height_more_than or height_less_than

            4. Boxes with area_more_than or area_less_than

            5. Boxes with volume_more_than or volume_less_than


6. Delete Api:

    Delete a box with a given id: 

    Permissions:

         Only the creater of the box shall be able to delete the box.


Conditions fulfilled on each add/update/delete:

Average area of all added boxes should not exceed A1

Average volume of all boxes added by the current user shall not exceed V1

Total Boxes added in a week cannot be more than L1

Total Boxes added in a week by a user cannot be more than L2

Values A1, V1, L1 and L2 shall be configured externally. You can choose 100, 1000, 100, and 50 as their respective default values.


## Installation

#### 1. Install Python
Install ```python-3.7.2``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Setup virtual environment
Reference : https://docs.python.org/3/library/venv.html
```bash
# Install virtual environment
sudo pip install virtualenv

# Make a directory
mkdir envs

# Create virtual environment
virtualenv ./envs/

# Activate virtual environment
source envs/bin/activate
```

#### 3. Clone git repository
```bash
git clone "https://github.com/Akash-Kumar-Sen/Django-REST-API.git"
```

#### 4. Install requirements
```bash
cd EdexCare/
pip install -r requirements.txt
```

#### 5. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver

# your server is up on port 8000
```
Try opening [http://localhost:8000](http://localhost:8000) in the browser.
Now you are good to go.

## Output Image
![](https://github.com/Akash-Kumar-Sen/Django-Assignment/blob/main/output-expected.png)

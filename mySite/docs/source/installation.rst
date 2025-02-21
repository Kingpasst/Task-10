Installation
===========

Prerequisites
------------
* Python 3.8+


Setup
-----
1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/Kingpasst/Task-10.git

2. Create virtual environment:

   .. code-block:: bash

      python -m venv venv
      venv\Scripts\activate

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Configure environment variables:

   .. code-block:: bash

      cp .env.example .env

5. Run migrations:

   .. code-block:: bash

      python manage.py migrate
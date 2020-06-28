### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/shandryll/PPSD_AntiCoronaVirus.git
  $ cd PPSD_AntiCoronaVirus
  ```

2. Create a docker container:
  ```
  $ docker-compose build
  ```

3. Install database and initial data:
  ```
  $ python db/tables.py
  ```

4. Start docker container:
  ```
  $ docker-compose up -d
  ```
  
5. Navigate to:
  ```
  http://localhost:5000
  ```
  
6. Leave docker container:
  ```
  $ docker-compose down
  ```

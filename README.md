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
  
3. Start docker container:
  ```
  $ docker-compose up -d
  ```
  
4. Enter in docker container:
  ```
  $ docker exec -it anticoronavirus /bin/bash
  ```
  
5. Run the development server:
  ```
  $ python app.py
  ```
  
6. Navigate to:
  ```
  http://localhost:5000
  ```
  
7. Leave docker container:
  ```
  $ docker-compose down
  ```

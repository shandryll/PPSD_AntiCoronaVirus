### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/shandryll/PPSD_AntiCoronaVirus.git
  $ cd PPSD_AntiCoronaVirus
  ```

2. Create an Docker image:
  ```
  $ docker build -t anticoronavirus .
  ```

3. Create a Docker container:
  ```
  $ docker run anticoronavirus
  ```
  
4. Start docker-compose:
  ```
  $ docker-compose build
  ```
  
5. Run container:
  ```
  $ docker-compose up -d
  ```
  
6. Run the development server:
  ```
  $ python app.py
  ```

7. Navigate to:
  ```
  http://localhost:5000
  ```

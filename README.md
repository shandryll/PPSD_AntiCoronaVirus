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
  
4. Verify if exists a container:
  ```
  $ docker ps
  ```
  
5. Run the development server:
  ```
  $ python app.py
  ```

6. Navigate to [http://localhost:5000]

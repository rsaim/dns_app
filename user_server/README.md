Docker image: https://hub.docker.com/repository/docker/rsaim/user-server

```bash
$ docker build -t rsaim/user-server:latest .
[+] Building 0.6s (11/11) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                           0.0s
 => => transferring dockerfile: 380B                                                                                                                                                           0.0s
 => [internal] load .dockerignore                                                                                                                                                              0.0s
 => => transferring context: 2B                                                                                                                                                                0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                                                                                                  0.4s
 => [1/6] FROM docker.io/library/python:3.9@sha256:f83d4b1356ee28b54c28ffe10dfcddb020e33b38e6fa109dba369b7286d2819b                                                                            0.0s
 => => resolve docker.io/library/python:3.9@sha256:f83d4b1356ee28b54c28ffe10dfcddb020e33b38e6fa109dba369b7286d2819b                                                                            0.0s
 => [internal] load build context                                                                                                                                                              0.0s
 => => transferring context: 1.80kB                                                                                                                                                            0.0s
 => CACHED [2/6] RUN apt-get update   && apt-get clean   && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*                                                                                      0.0s
 => CACHED [3/6] RUN groupadd -g 799 nyu &&     useradd -r -u 999 -g nyu nyu                                                                                                                   0.0s
 => CACHED [4/6] WORKDIR /app                                                                                                                                                                  0.0s
 => CACHED [5/6] RUN pip install Flask                                                                                                                                                         0.0s
 => [6/6] COPY --chown=nyu:nyu . .                                                                                                                                                             0.0s
 => exporting to image                                                                                                                                                                         0.0s
 => => exporting layers                                                                                                                                                                        0.0s
 => => writing image sha256:94f7d62f014b8932ef3de80a09352a26d47a897b6c81fdfe3babe1bfc4088f69                                                                                                   0.0s
 => => naming to docker.io/rsaim/user-server:latest                                                                                                                                            0.0s	
```



```bash
$ docker run -p 8080:8080 rsaim/user-server

 * Serving Flask app 'user_server' (lazy loading)
 * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
 * Debug mode: on
    [07:02:34 PM]  * Running on all addresses.
    WARNING: This is a development server. Do not use it in a production deployment.
    [07:02:34 PM]  * Running on http://172.17.0.4:8080/ (Press CTRL+C to quit)
    [07:02:34 PM]  * Restarting with stat
    [07:02:34 PM]  * Debugger is active!
    [07:02:34 PM]  * Debugger PIN: 100-525-529
    [07:02:47 PM] 172.17.0.1 - - [13/Oct/2021 19:02:47] "GET / HTTP/1.1" 200 -
    [07:02:47 PM] 172.17.0.1 - - [13/Oct/2021 19:02:47] "GET /favicon.ico HTTP/1.1" 404 -
    ^C
```



```bash
$ docker push rsaim/user-server
Using default tag: latest
The push refers to repository [docker.io/rsaim/user-server]
64558df34c29: Pushed
1ca8ebb2878d: Pushed
cd93ac2f9c3a: Pushed
5da471c81d43: Pushed
34b2899cd9e6: Pushed
febe96d6107f: Mounted from library/python
7b656b8058c4: Mounted from library/python
02a38a00d553: Mounted from library/python
7fcd2600f5ad: Mounted from library/python
8f56c3340629: Mounted from library/python
ba6e5ff31f23: Mounted from library/python
9f9f651e9303: Mounted from library/python
0b3c02b5d746: Mounted from library/python
62a747bf1719: Mounted from library/python
latest: digest: sha256:df981ce1b96c4daeab248a119ea3ee9609021cc3324f15d1dcc9ba8baef987e5 size: 3259
```




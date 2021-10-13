Docker Image: https://hub.docker.com/r/rsaim/fibonacci-server

```bash
$ docker build -t rsaim/fibonacci-server:latest .
[+] Building 3.4s (13/13) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                           0.0s
 => => transferring dockerfile: 410B                                                                                                                                                           0.0s
 => [internal] load .dockerignore                                                                                                                                                              0.0s
 => => transferring context: 2B                                                                                                                                                                0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                                                                                                  0.9s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                  0.0s
 => [1/7] FROM docker.io/library/python:3.9@sha256:f83d4b1356ee28b54c28ffe10dfcddb020e33b38e6fa109dba369b7286d2819b                                                                            0.0s
 => => resolve docker.io/library/python:3.9@sha256:f83d4b1356ee28b54c28ffe10dfcddb020e33b38e6fa109dba369b7286d2819b                                                                            0.0s
 => [internal] load build context                                                                                                                                                              0.0s
 => => transferring context: 444B                                                                                                                                                              0.0s
 => CACHED [2/7] RUN apt-get update   && apt-get clean   && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*                                                                                      0.0s
 => CACHED [3/7] RUN groupadd -g 799 nyu &&     useradd -r -u 999 -g nyu nyu                                                                                                                   0.0s
 => CACHED [4/7] WORKDIR /app                                                                                                                                                                  0.0s
 => CACHED [5/7] RUN pip install Flask                                                                                                                                                         0.0s
 => [6/7] RUN pip install requests                                                                                                                                                             2.2s
 => [7/7] COPY --chown=nyu:nyu . .                                                                                                                                                             0.0s
 => exporting to image                                                                                                                                                                         0.1s
 => => exporting layers                                                                                                                                                                        0.1s
 => => writing image sha256:c611685a47ee53c47161627c9384eeabb65a48ab8faf666de2b23d1c6d38df21                                                                                                   0.0s
 => => naming to docker.io/rsaim/fibonacci-server:latest                                                                                                                                       0.0s
 
 Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```



```bash
$ docker run -p 9090:9090 rsaim/fibonacci-server

 * Serving Flask app 'fibonacci_server' (lazy loading)
 * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
 * Debug mode: on
    [fibonacci server: 06:56:45 PM]  * Running on all addresses.
    WARNING: This is a development server. Do not use it in a production deployment.
    [fibonacci server: 06:56:45 PM]  * Running on http://172.17.0.3:9090/ (Press CTRL+C to quit)
    [fibonacci server: 06:56:45 PM]  * Restarting with stat
    [fibonacci server: 06:56:45 PM]  * Debugger is active!
    [fibonacci server: 06:56:45 PM]  * Debugger PIN: 124-349-638
    [fibonacci server: 06:57:03 PM] 172.17.0.1 - - [13/Oct/2021 18:57:03] "GET / HTTP/1.1" 200 -
    [fibonacci server: 06:57:03 PM] 172.17.0.1 - - [13/Oct/2021 18:57:03] "GET /favicon.ico HTTP/1.1" 404 -
    [fibonacci server: 06:57:16 PM] /fibonacci got n=2
    [fibonacci server: 06:57:16 PM] 172.17.0.1 - - [13/Oct/2021 18:57:16] "GET /fibonacci?number=2 HTTP/1.1" 200 -
    load: 1.76  cmd: com.docker.cli 3897 running 0.03u 0.01s
    ^C
```



```bash
$ docker push rsaim/fibonacci-server
Using default tag: latest
The push refers to repository [docker.io/rsaim/fibonacci-server]
22fb333b2e85: Pushed
bf7285c59f79: Pushed
1ca8ebb2878d: Mounted from rsaim/user-server
cd93ac2f9c3a: Mounted from rsaim/user-server
5da471c81d43: Mounted from rsaim/user-server
34b2899cd9e6: Mounted from rsaim/user-server
febe96d6107f: Mounted from rsaim/user-server
7b656b8058c4: Mounted from rsaim/user-server
02a38a00d553: Mounted from rsaim/user-server
7fcd2600f5ad: Mounted from rsaim/user-server
8f56c3340629: Mounted from rsaim/user-server
ba6e5ff31f23: Mounted from rsaim/user-server
9f9f651e9303: Mounted from rsaim/user-server
0b3c02b5d746: Mounted from rsaim/user-server
62a747bf1719: Mounted from rsaim/user-server
latest: digest: sha256:bdbfd5669f632ff730c0fc1e6675711397774cf29f81579102ab209eae884e84 size: 3470
```




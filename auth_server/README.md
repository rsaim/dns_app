$ docker build -t rsaim/auth-server:latest .
[+] Building 0.4s (11/11) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                           0.0s
 => => transferring dockerfile: 37B                                                                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                                                              0.0s
 => => transferring context: 2B                                                                                                                                                                0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                                                                                                  0.3s
 => [1/6] FROM docker.io/library/python:3.9@sha256:206efc55ae5a8cc3ab413105da3617d78fa15bf512acc437a4dce94e4430ddcc                                                                            0.0s
 => [internal] load build context                                                                                                                                                              0.0s
 => => transferring context: 66B                                                                                                                                                               0.0s
 => CACHED [2/6] RUN apt-get update   && apt-get clean   && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*                                                                                      0.0s
 => CACHED [3/6] RUN groupadd -g 799 nyu &&     useradd -r -u 999 -g nyu nyu                                                                                                                   0.0s
 => CACHED [4/6] WORKDIR /app                                                                                                                                                                  0.0s
 => CACHED [5/6] RUN pip install Flask                                                                                                                                                         0.0s
 => CACHED [6/6] COPY --chown=nyu:nyu . .                                                                                                                                                      0.0s
 => exporting to image                                                                                                                                                                         0.0s
 => => exporting layers                                                                                                                                                                        0.0s
 => => writing image sha256:eda320be191e0b3ae7077baf217a0c3217f781f6a27d912d648aecf5407ec9bb                                                                                                   0.0s
 => => naming to docker.io/rsaim/auth-server:latest                                                                                                                                            0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them

###############

$ docker build -t rsaim/auth-server:latest .
[+] Building 0.4s (11/11) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                           0.0s
 => => transferring dockerfile: 37B                                                                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                                                              0.0s
 => => transferring context: 2B                                                                                                                                                                0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                                                                                                  0.3s
 => [1/6] FROM docker.io/library/python:3.9@sha256:206efc55ae5a8cc3ab413105da3617d78fa15bf512acc437a4dce94e4430ddcc                                                                            0.0s
 => [internal] load build context                                                                                                                                                              0.0s
 => => transferring context: 66B                                                                                                                                                               0.0s
 => CACHED [2/6] RUN apt-get update   && apt-get clean   && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*                                                                                      0.0s
 => CACHED [3/6] RUN groupadd -g 799 nyu &&     useradd -r -u 999 -g nyu nyu                                                                                                                   0.0s
 => CACHED [4/6] WORKDIR /app                                                                                                                                                                  0.0s
 => CACHED [5/6] RUN pip install Flask                                                                                                                                                         0.0s
 => CACHED [6/6] COPY --chown=nyu:nyu . .                                                                                                                                                      0.0s
 => exporting to image                                                                                                                                                                         0.0s
 => => exporting layers                                                                                                                                                                        0.0s
 => => writing image sha256:eda320be191e0b3ae7077baf217a0c3217f781f6a27d912d648aecf5407ec9bb                                                                                                   0.0s
 => => naming to docker.io/rsaim/auth-server:latest                                                                                                                                            0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them


###############

$ docker push rsaim/auth-server
Using default tag: latest
The push refers to repository [docker.io/rsaim/auth-server]
f1b71091f793: Pushed
1ca8ebb2878d: Mounted from rsaim/fibonacci-server
cd93ac2f9c3a: Mounted from rsaim/fibonacci-server
5da471c81d43: Mounted from rsaim/fibonacci-server
34b2899cd9e6: Mounted from rsaim/fibonacci-server
febe96d6107f: Mounted from rsaim/fibonacci-server
7b656b8058c4: Mounted from rsaim/fibonacci-server
02a38a00d553: Mounted from rsaim/fibonacci-server
7fcd2600f5ad: Mounted from rsaim/fibonacci-server
8f56c3340629: Mounted from rsaim/fibonacci-server
ba6e5ff31f23: Mounted from rsaim/fibonacci-server
9f9f651e9303: Mounted from rsaim/fibonacci-server
0b3c02b5d746: Mounted from rsaim/fibonacci-server
62a747bf1719: Mounted from rsaim/fibonacci-server
latest: digest: sha256:94567dd85fd8f0bc77c36f9906bc5887449d325ab5f38e406723162b484c54b9 size: 3259
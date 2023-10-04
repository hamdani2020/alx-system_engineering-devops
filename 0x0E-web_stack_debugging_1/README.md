# 0x0E. Web stack debugging #1
**DevOPs** | **SysAdmin** | **Scripting** | **Debugging**

![Image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/271/B4eeypV.jpg)

## Requirements
- Allowed editors: ``vi``, ``vim``, ``emacs``
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- ``README.md`` file at the root of the folder of the project is mandatory
- All your Bash script files must be executable
- Your Bash script must pass ``Shellcheck`` without any error
- Your bash scripts must run without any error
- The first line of all Bash scripts should be exactly ``#!/usr/bin/env bash``
- The second line of all Bash scripts should be a comment explainging what is the script doing.
- You are not allowd to use ``wget``

## Task 0
I'm finding out what's keeping my ubuntu container's Nginx installation from listening on poprt ``80``. I'm writing a Bash script with minimum number of commands to automate the fix and fix the bug.

**Requirements:**
- Nginx must be running, and listening on port ``80`` of all the server's active IPv4 IPs
- Write a Bash script that configues a server to the abose requirementss

```
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&>1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
```

## Task 1
Using what I did for task #0, I make my fix short and sweet

**Requirements**
- Your Bash script must 5 lines or less
- There must be a new line at the end of the file
- You must respect usual Bash script requirements
- You cannot use ``;``
- You cannot use ``&&``
- You cannot use ``wget``
- You cannot execute your previous answer file (Do no include the name previous script in this one)
- ``service`` (init) must say that ``nginx`` is not running for real

```
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
root@966c5664b21f:/# service nginx status
 * nginx is not running
root@966c5664b21f:/#
```

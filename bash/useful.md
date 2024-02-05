```shell
sudo apt update && sudo apt upgrade # resynchronize the package index files from their sources and install the newest versions of all packages currently installed

chmod u+x {file_name} # permission to execute (grant only the owner)

chmod +x {file_name} # permission to execute (grant all - owner, group, others)

chown -R {user_name}:{user_name} . # changes permissions

find . -name {file_name} # finds a dir by name

dpkg -i *.deb # installs .deb files

tar -vzxf *tar.gz # extract tar.gz files

ls -p | grep -v / # shows only files

# source: https://twitter.com/joaopedro_cc/status/1208961660452556800
history | awk '{print $2}' | sort | uniq -c | sort -rn | head -10 # last commands most used

# source: https://gist.github.com/ajcrites/e5b3508ff5a1a239014d5dccec16a8d4
history | cut -c8- | \grep -Eo '^[^[:space:]]+| \| [^[:space:]]+' | sed 's/ \| //' | sort | uniq -c | sort -n # command to (sort of) get all of the commands from your history by count

dpkg --get-selections | grep -v deinstall | nl # get a list of packages installed locally with number lines (nl)

dpkg -l # same list with description. add "| nl" to see number lines (nl)

<ctrl> + u # clears the line. Useful when password is typed wrong

less -N {file_name} # displays file contents output one page at a time with number lines (-N). An alternative to cat

docker ps -a # list both running and stopped containers

docker stop {container} # stop one container

docker stop `docker ps -q` # stop all the containers

docker rm {container} # delete one container

docker rm -f {container} # delete one container without stopping it

docker stop `docker ps -q`; docker rm `docker ps -aq` # delete all the containers

lsof -i :{port} # knows which process is using some port

kill -9 {PID} # if you want to terminate the process listed before

busybox httpd -p 8080 -h {path/to/file_name} # simple web server with BusyBox HTTP Daemon. Available at http://localhost:8080

tail -n 100 {file_name} # last 100 lines of a file

# convert all files in a directory from .mkv to .mp4
# source: https://www.putorius.net/convert-mkv-to-mp4-linux.html
for i in *.mkv; do
    ffmpeg -i "$i" -codec copy "${i%.*}.mp4"
done
```
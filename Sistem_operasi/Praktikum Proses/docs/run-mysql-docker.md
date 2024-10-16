# 1
docker pull mysql:5.7
# 2
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=your_password -p 3306:3306 -d mysql:5.7

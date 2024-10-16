docker build -t order-service-img .

<!-- order-service-img = python3.19 + kode_order_kita -->

docker run -d -p 7080:8000 --memory="1g" --cpus="1.5" --name order-service-1 order-service-img
docker run -d -p 7081:8000 --memory="1g" --cpus="1.5" --name order-service-2 order-service-img
docker run -d -p 7082:8000 --memory="1g" --cpus="1.5" --name order-service-3 order-service-img
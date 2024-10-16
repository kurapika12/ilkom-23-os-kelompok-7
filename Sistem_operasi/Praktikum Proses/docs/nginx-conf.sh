upstream order_service {
    server 127.0.0.1:7080
    server 127.0.0.1:7081
    server 127.0.0.1:7082
}

server {
    listen 80;
    location / {
        proxy_pass http://order_service;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; 
        proxy_set_header X-Forwarded-Proto $scheme; 
    }
}
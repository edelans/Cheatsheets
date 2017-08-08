#Django Config

server {
      server_name domain.com;


      access_log on;

      location / {
              proxy_pass http://127.0.0.1:8001;
              proxy_set_header X-Forwarded-Host $server_name;
              proxy_set_header X-Real-IP $remote_addr;
              add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
      }
  }


#Nodejs Config

server{

  server_name subdomain.domain.com;
  access_log /var/log/nginx/me.log;
  location / {


      proxy_pass http://127.0.0.1:8002;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection "upgrade";
      proxy_set_header Host $host;

      #IMPORTANT
      #Must allow access to this origin resource http://subdomain.domain.com;
      #if is not set , you will get CORS message and the websockets will be blocked
      proxy_set_header Access-Control-Allow-Origin http://subdomain.domain.com;
      proxy_set_header 'Access-Control-Allow-Headers' 'X-Requested-With,Accept,Content-Type, Origin';
      proxy_set_header X-NginX-Proxy true;


      proxy_redirect off;
  }
}

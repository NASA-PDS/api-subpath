FROM nginx:1.21.6-alpine
ENV CERT_CN=localhost
ENV PROXY_REDIRECT=default
RUN : &&\
    /sbin/apk update --quiet &&\
    /sbin/apk add --no-progress --quiet openssl &&\
    /bin/rm -rf /var/cache/apk/* &&\
    :
COPY nginx.conf /etc/nginx/
COPY default.conf.template /etc/nginx/templates/
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
EXPOSE 443

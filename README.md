# CheckMyIP
A Simple HTTP Based Public IP Address Lookup Service

Idea taken from [TelnetMyIP.com](https://github.com/PackeTsar/checkmyip)
to suit my self-hosted needs:
- Run behind an HTTP proxy (HTTP support only)
- Run inside a docker

-----------------------------------------
### USAGE
#### Running your CheckMyIP instance
Clone this repo on your docker host and run:
```bash
docker build . -t checkmyip
docker run --restart=always -d -p 8080:80 checkmyip 
```
Then point your reverse proxy to port 8080.

#### Getting your IP
- CURL: `curl <your reverse proxy>`

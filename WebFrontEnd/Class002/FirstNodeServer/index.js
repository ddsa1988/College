import http from "http";

// http.createServer(function (req, res) {
//     res.writeHead(200, { "content-type": "text/plain" });
//     res.end("Hello...");
// }).listen(8080);

http.createServer(function (req, res) {
    res.writeHead(200, { "content-type": "text/json" });
    res.end(
        JSON.stringify({ id: "1", firstName: "Diego", lastName: "Alexander" })
    );
}).listen(8080);

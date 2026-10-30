## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 3,428 | 3,436 | 3,417 | 0.2% | 390 MB | 116.4 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 3,389 | 3,403 | 3,378 | 0.3% | 137 MB | 41.3 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.7 | 3,387 | 3,397 | 3,380 | 0.2% | 396 MB | 119.7 KB |  |
| fusion-aot-11 | 16.7.3 | 3,346 | 3,368 | 3,317 | 0.5% | 126 MB | 38.6 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,283 | 3,297 | 3,266 | 0.4% | 2,294 MB | 715.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 2,781 | 2,789 | 2,744 | 0.6% | 394 MB | 145.2 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,774 | 2,778 | 2,762 | 0.3% | 384 MB | 141.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 2,742 | 2,757 | 2,733 | 0.3% | 140 MB | 52.2 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,733 | 2,739 | 2,715 | 0.3% | 150 MB | 56.0 KB |  |
| hive-router | v0.3.6 | 2,046 | 2,055 | 2,039 | 0.3% | 91 MB | 45.6 KB |  |
| grafbase | 0.53.5 | 1,453 | 1,458 | 1,449 | 0.2% | 100 MB | 70.4 KB |  |
| cosmo | 0.363.0 | 1,441 | 1,443 | 1,439 | 0.1% | 149 MB | 105.7 KB |  |
| caliban | 3.2.0 | 1,372 | 1,373 | 1,366 | 0.2% | 4,928 MB | 3,677.8 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 521 | 522 | 521 | 0.1% | 2,750 MB | 5,405.1 KB |  |
| apollo-router | v2.19.0 | 481 | 485 | 481 | 0.4% | 177 MB | 377.2 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 419 | 419 | 418 | 0.1% | 210 MB | 513.5 KB |  |
| apollo-gateway | 2.14.4 | 266 | 267 | 265 | 0.3% | 2,162 MB | 8,324.0 KB |  |
| hive-gateway | 2.15.3 | 264 | 265 | 264 | 0.2% | 3,618 MB | 14,031.7 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1243962     ✗ 0     
     data_received..................: 36 GB   300 MB/s
     data_sent......................: 498 MB  4.1 MB/s
     http_req_blocked...............: avg=3.22µs  min=931ns   med=2.26µs  max=8.35ms   p(90)=3.68µs  p(95)=4.46µs   p(99.9)=29.06µs
     http_req_connecting............: avg=551ns   min=0s      med=0s      max=8.3ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.25ms min=8.17ms  med=13.83ms max=276.4ms  p(90)=17.74ms p(95)=19.09ms  p(99.9)=26.83ms
       { expected_response:true }...: avg=14.25ms min=8.17ms  med=13.83ms max=276.4ms  p(90)=17.74ms p(95)=19.09ms  p(99.9)=26.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 414754
     http_req_receiving.............: avg=73.66µs min=24.63µs med=45.27µs max=23.51ms  p(90)=97.59µs p(95)=184.68µs p(99.9)=2.25ms 
     http_req_sending...............: avg=34.05µs min=4.33µs  med=8.48µs  max=150.44ms p(90)=17.72µs p(95)=100.23µs p(99.9)=2.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.15ms min=8.11ms  med=13.73ms max=273.56ms p(90)=17.62ms p(95)=18.96ms  p(99.9)=26.52ms
     http_reqs......................: 414754  3428.901475/s
     iteration_duration.............: avg=14.46ms min=8.34ms  med=14.03ms max=302.72ms p(90)=17.93ms p(95)=19.29ms  p(99.9)=27.05ms
     iterations.....................: 414654  3428.074744/s
     success_rate...................: 100.00% ✓ 414654      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1229751     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 493 MB  4.1 MB/s
     http_req_blocked...............: avg=2.45µs  min=802ns   med=1.85µs  max=3.96ms   p(90)=3.06µs  p(95)=3.78µs   p(99.9)=24.66µs
     http_req_connecting............: avg=230ns   min=0s      med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.43ms min=8.24ms  med=14ms    max=277.13ms p(90)=17.82ms p(95)=19.2ms   p(99.9)=27.42ms
       { expected_response:true }...: avg=14.43ms min=8.24ms  med=14ms    max=277.13ms p(90)=17.82ms p(95)=19.2ms   p(99.9)=27.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 410017
     http_req_receiving.............: avg=67.21µs min=24.02µs med=42.25µs max=104.9ms  p(90)=90.37µs p(95)=168.62µs p(99.9)=1.77ms 
     http_req_sending...............: avg=31.6µs  min=4.43µs  med=7.95µs  max=162.69ms p(90)=17.03µs p(95)=91.73µs  p(99.9)=1.77ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.33ms min=8.17ms  med=13.91ms max=271.74ms p(90)=17.71ms p(95)=19.08ms  p(99.9)=27.17ms
     http_reqs......................: 410017  3389.572984/s
     iteration_duration.............: avg=14.62ms min=8.43ms  med=14.19ms max=287.22ms p(90)=18.01ms p(95)=19.39ms  p(99.9)=27.68ms
     iterations.....................: 409917  3388.746293/s
     success_rate...................: 100.00% ✓ 409917      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1229067     ✗ 0     
     data_received..................: 36 GB   296 MB/s
     data_sent......................: 492 MB  4.1 MB/s
     http_req_blocked...............: avg=2.7µs   min=802ns   med=2.13µs  max=3.99ms   p(90)=3.48µs  p(95)=4.24µs   p(99.9)=28.35µs
     http_req_connecting............: avg=219ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.43ms min=8.16ms  med=14ms    max=269.45ms p(90)=17.98ms p(95)=19.39ms  p(99.9)=27.4ms 
       { expected_response:true }...: avg=14.43ms min=8.16ms  med=14ms    max=269.45ms p(90)=17.98ms p(95)=19.39ms  p(99.9)=27.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 409789
     http_req_receiving.............: avg=73.21µs min=24.83µs med=45.16µs max=162.15ms p(90)=94.37µs p(95)=177.69µs p(99.9)=2.09ms 
     http_req_sending...............: avg=32.42µs min=4.41µs  med=8.3µs   max=195.89ms p(90)=16.76µs p(95)=95.31µs  p(99.9)=1.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.33ms min=8.1ms   med=13.9ms  max=269.23ms p(90)=17.87ms p(95)=19.26ms  p(99.9)=27.16ms
     http_reqs......................: 409789  3387.856034/s
     iteration_duration.............: avg=14.63ms min=8.43ms  med=14.19ms max=292.7ms  p(90)=18.18ms p(95)=19.58ms  p(99.9)=27.62ms
     iterations.....................: 409689  3387.029303/s
     success_rate...................: 100.00% ✓ 409689      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1214043     ✗ 0     
     data_received..................: 35 GB   293 MB/s
     data_sent......................: 486 MB  4.0 MB/s
     http_req_blocked...............: avg=2.82µs  min=852ns   med=2.23µs  max=9.26ms   p(90)=3.53µs  p(95)=4.24µs   p(99.9)=30.41µs
     http_req_connecting............: avg=233ns   min=0s      med=0s      max=4.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.62ms min=8.3ms   med=14.17ms max=272.48ms p(90)=18.11ms p(95)=19.54ms  p(99.9)=27.9ms 
       { expected_response:true }...: avg=14.62ms min=8.3ms   med=14.17ms max=272.48ms p(90)=18.11ms p(95)=19.54ms  p(99.9)=27.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 404781
     http_req_receiving.............: avg=72.56µs min=24.31µs med=45.37µs max=167.95ms p(90)=93.74µs p(95)=185.94µs p(99.9)=1.98ms 
     http_req_sending...............: avg=31.9µs  min=4.32µs  med=8.41µs  max=94.51ms  p(90)=16.86µs p(95)=98.68µs  p(99.9)=1.65ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.51ms min=8.17ms  med=14.07ms max=272.33ms p(90)=18.01ms p(95)=19.42ms  p(99.9)=27.67ms
     http_reqs......................: 404781  3346.299877/s
     iteration_duration.............: avg=14.81ms min=8.51ms  med=14.36ms max=289.89ms p(90)=18.31ms p(95)=19.73ms  p(99.9)=28.11ms
     iterations.....................: 404681  3345.473183/s
     success_rate...................: 100.00% ✓ 404681      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-10-25-0247)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1191336     ✗ 0     
     data_received..................: 35 GB   287 MB/s
     data_sent......................: 477 MB  3.9 MB/s
     http_req_blocked...............: avg=2.47µs  min=792ns   med=1.91µs  max=3.89ms   p(90)=3.18µs  p(95)=3.93µs   p(99.9)=24.71µs
     http_req_connecting............: avg=226ns   min=0s      med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.9ms  min=8.55ms  med=14.57ms max=287.98ms p(90)=17.97ms p(95)=19.17ms  p(99.9)=26.87ms
       { expected_response:true }...: avg=14.9ms  min=8.55ms  med=14.57ms max=287.98ms p(90)=17.97ms p(95)=19.17ms  p(99.9)=26.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 397212
     http_req_receiving.............: avg=80.9µs  min=23.27µs med=43.96µs max=250.55ms p(90)=89.75µs p(95)=165.75µs p(99.9)=1.53ms 
     http_req_sending...............: avg=30.07µs min=4.23µs  med=8.18µs  max=25.05ms  p(90)=16.47µs p(95)=92.77µs  p(99.9)=1.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.79ms min=8.47ms  med=14.47ms max=99.72ms  p(90)=17.86ms p(95)=19.06ms  p(99.9)=26.7ms 
     http_reqs......................: 397212  3283.884476/s
     iteration_duration.............: avg=15.1ms  min=8.75ms  med=14.76ms max=300.69ms p(90)=18.15ms p(95)=19.36ms  p(99.9)=27.08ms
     iterations.....................: 397112  3283.057742/s
     success_rate...................: 100.00% ✓ 397112      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1012563     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 406 MB  3.3 MB/s
     http_req_blocked...............: avg=2.89µs  min=811ns   med=2.21µs  max=3.79ms   p(90)=3.69µs  p(95)=4.51µs   p(99.9)=30.43µs
     http_req_connecting............: avg=288ns   min=0s      med=0s      max=3.75ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.55ms min=11.8ms  med=17.11ms max=288.59ms p(90)=20.66ms p(95)=21.93ms  p(99.9)=29.12ms
       { expected_response:true }...: avg=17.55ms min=11.8ms  med=17.11ms max=288.59ms p(90)=20.66ms p(95)=21.93ms  p(99.9)=29.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 337621
     http_req_receiving.............: avg=69.34µs min=23.27µs med=45.16µs max=31.03ms  p(90)=97.08µs p(95)=162.39µs p(99.9)=1.55ms 
     http_req_sending...............: avg=29.72µs min=4.19µs  med=8.51µs  max=196.69ms p(90)=17.97µs p(95)=90.09µs  p(99.9)=1.56ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.46ms min=11.72ms med=17.02ms max=288.33ms p(90)=20.55ms p(95)=21.81ms  p(99.9)=28.94ms
     http_reqs......................: 337621  2781.151821/s
     iteration_duration.............: avg=17.76ms min=11.97ms med=17.31ms max=298.16ms p(90)=20.86ms p(95)=22.12ms  p(99.9)=29.36ms
     iterations.....................: 337521  2780.328072/s
     success_rate...................: 100.00% ✓ 337521      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1010238     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 405 MB  3.3 MB/s
     http_req_blocked...............: avg=2.87µs  min=762ns   med=1.83µs  max=8.18ms   p(90)=3.12µs  p(95)=3.83µs   p(99.9)=23.93µs
     http_req_connecting............: avg=655ns   min=0s      med=0s      max=8.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.6ms  min=11.72ms med=17.18ms max=290.64ms p(90)=20.66ms p(95)=21.91ms  p(99.9)=28.77ms
       { expected_response:true }...: avg=17.6ms  min=11.72ms med=17.18ms max=290.64ms p(90)=20.66ms p(95)=21.91ms  p(99.9)=28.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 336846
     http_req_receiving.............: avg=66.39µs min=23.24µs med=43.94µs max=171.9ms  p(90)=89.84µs p(95)=140.51µs p(99.9)=1.44ms 
     http_req_sending...............: avg=29.37µs min=4.14µs  med=7.86µs  max=217.65ms p(90)=16.16µs p(95)=79µs     p(99.9)=1.55ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.51ms min=11.67ms med=17.09ms max=282.06ms p(90)=20.55ms p(95)=21.8ms   p(99.9)=28.56ms
     http_reqs......................: 336846  2774.708255/s
     iteration_duration.............: avg=17.8ms  min=11.91ms med=17.38ms max=301.28ms p(90)=20.85ms p(95)=22.1ms   p(99.9)=28.97ms
     iterations.....................: 336746  2773.884523/s
     success_rate...................: 100.00% ✓ 336746      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 998514      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=2.98µs  min=952ns   med=2.33µs  max=4.17ms   p(90)=3.83µs  p(95)=4.67µs  p(99.9)=32.19µs
     http_req_connecting............: avg=277ns   min=0s      med=0s      max=4.13ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.8ms  min=11.92ms med=17.35ms max=293.2ms  p(90)=20.88ms p(95)=22.18ms p(99.9)=30.05ms
       { expected_response:true }...: avg=17.8ms  min=11.92ms med=17.35ms max=293.2ms  p(90)=20.88ms p(95)=22.18ms p(99.9)=30.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332938
     http_req_receiving.............: avg=70.69µs min=24.11µs med=46.02µs max=150.86ms p(90)=95.39µs p(95)=163.6µs p(99.9)=1.41ms 
     http_req_sending...............: avg=32.05µs min=4.57µs  med=8.97µs  max=189.55ms p(90)=18.31µs p(95)=93.7µs  p(99.9)=1.55ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.7ms  min=11.83ms med=17.26ms max=273.74ms p(90)=20.77ms p(95)=22.05ms p(99.9)=29.8ms 
     http_reqs......................: 332938  2742.110993/s
     iteration_duration.............: avg=18.01ms min=12.22ms med=17.56ms max=301.94ms p(90)=21.08ms p(95)=22.38ms p(99.9)=30.34ms
     iterations.....................: 332838  2741.287383/s
     success_rate...................: 100.00% ✓ 332838      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 995295      ✗ 0     
     data_received..................: 29 GB   239 MB/s
     data_sent......................: 399 MB  3.3 MB/s
     http_req_blocked...............: avg=2.45µs  min=761ns   med=1.81µs  max=4.07ms   p(90)=3.15µs  p(95)=3.9µs    p(99.9)=24.62µs
     http_req_connecting............: avg=273ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.87ms min=11.99ms med=17.45ms max=307.97ms p(90)=20.93ms p(95)=22.19ms  p(99.9)=29.46ms
       { expected_response:true }...: avg=17.87ms min=11.99ms med=17.45ms max=307.97ms p(90)=20.93ms p(95)=22.19ms  p(99.9)=29.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 331865
     http_req_receiving.............: avg=63.28µs min=22.43µs med=42.77µs max=19.88ms  p(90)=88.36µs p(95)=135.49µs p(99.9)=1.29ms 
     http_req_sending...............: avg=27.26µs min=4.21µs  med=7.79µs  max=213.02ms p(90)=16.47µs p(95)=77.86µs  p(99.9)=1.29ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.78ms min=11.94ms med=17.37ms max=307.5ms  p(90)=20.83ms p(95)=22.08ms  p(99.9)=29.19ms
     http_reqs......................: 331865  2733.290672/s
     iteration_duration.............: avg=18.07ms min=12.14ms med=17.65ms max=315.77ms p(90)=21.13ms p(95)=22.39ms  p(99.9)=29.67ms
     iterations.....................: 331765  2732.467057/s
     success_rate...................: 100.00% ✓ 331765      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 747867      ✗ 0     
     data_received..................: 22 GB   179 MB/s
     data_sent......................: 300 MB  2.5 MB/s
     http_req_blocked...............: avg=2.99µs  min=842ns   med=2.15µs  max=4.73ms   p(90)=3.89µs  p(95)=4.61µs   p(99.9)=32.39µs 
     http_req_connecting............: avg=444ns   min=0s      med=0s      max=4.68ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.84ms min=17.15ms med=23.51ms max=295.53ms p(90)=26.87ms p(95)=27.94ms  p(99.9)=33.28ms 
       { expected_response:true }...: avg=23.84ms min=17.15ms med=23.51ms max=295.53ms p(90)=26.87ms p(95)=27.94ms  p(99.9)=33.28ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 249389
     http_req_receiving.............: avg=64.73µs min=24µs    med=48.35µs max=100.51ms p(90)=92.49µs p(95)=116.23µs p(99.9)=870.61µs
     http_req_sending...............: avg=23.92µs min=4.32µs  med=8.91µs  max=137.5ms  p(90)=17.26µs p(95)=23.29µs  p(99.9)=912.98µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.75ms min=17.08ms med=23.42ms max=294.97ms p(90)=26.78ms p(95)=27.84ms  p(99.9)=33.11ms 
     http_reqs......................: 249389  2046.201588/s
     iteration_duration.............: avg=24.05ms min=17.35ms med=23.71ms max=304.34ms p(90)=27.08ms p(95)=28.14ms  p(99.9)=33.51ms 
     iterations.....................: 249289  2045.381102/s
     success_rate...................: 100.00% ✓ 249289      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: grafbase (HotChocolate subgraphs) (0.53.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 531471      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=4.32µs  min=851ns   med=2.21µs  max=8.76ms   p(90)=4.46µs   p(95)=5.36µs   p(99.9)=40.36µs
     http_req_connecting............: avg=1.53µs  min=0s      med=0s      max=8.71ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.61ms min=17.52ms med=33.27ms max=298.27ms p(90)=39.24ms  p(95)=40.99ms  p(99.9)=49.12ms
       { expected_response:true }...: avg=33.61ms min=17.52ms med=33.27ms max=298.27ms p(90)=39.24ms  p(95)=40.99ms  p(99.9)=49.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 177257
     http_req_receiving.............: avg=78.67µs min=26.9µs  med=55.17µs max=8.11ms   p(90)=118.18µs p(95)=158.76µs p(99.9)=1.29ms 
     http_req_sending...............: avg=33.42µs min=4.67µs  med=9.43µs  max=235.98ms p(90)=21.91µs  p(95)=36.13µs  p(99.9)=1.36ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.49ms min=17.38ms med=33.17ms max=296.93ms p(90)=39.13ms  p(95)=40.87ms  p(99.9)=48.73ms
     http_reqs......................: 177257  1453.731801/s
     iteration_duration.............: avg=33.85ms min=20.48ms med=33.5ms  max=313.39ms p(90)=39.46ms  p(95)=41.2ms   p(99.9)=49.41ms
     iterations.....................: 177157  1452.911674/s
     success_rate...................: 100.00% ✓ 177157      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.363.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 526965      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=3.03µs  min=912ns   med=2.16µs  max=4.18ms   p(90)=3.75µs  p(95)=4.44µs   p(99.9)=28.53µs 
     http_req_connecting............: avg=549ns   min=0s      med=0s      max=4.13ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.94ms min=17.95ms med=33.37ms max=290.49ms p(90)=40.44ms p(95)=42.7ms   p(99.9)=55.09ms 
       { expected_response:true }...: avg=33.94ms min=17.95ms med=33.37ms max=290.49ms p(90)=40.44ms p(95)=42.7ms   p(99.9)=55.09ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 175755
     http_req_receiving.............: avg=72.05µs min=25.63µs med=59.04µs max=207.62ms p(90)=97.21µs p(95)=113.63µs p(99.9)=734.81µs
     http_req_sending...............: avg=23.54µs min=4.54µs  med=9.99µs  max=226.63ms p(90)=16.99µs p(95)=20.62µs  p(99.9)=736.96µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.85ms min=17.83ms med=33.28ms max=289.97ms p(90)=40.34ms p(95)=42.61ms  p(99.9)=54.91ms 
     http_reqs......................: 175755  1441.158214/s
     iteration_duration.............: avg=34.15ms min=20.61ms med=33.56ms max=306.58ms p(90)=40.63ms p(95)=42.89ms  p(99.9)=55.33ms 
     iterations.....................: 175655  1440.338232/s
     success_rate...................: 100.00% ✓ 175655      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 501921      ✗ 0     
     data_received..................: 15 GB   120 MB/s
     data_sent......................: 201 MB  1.6 MB/s
     http_req_blocked...............: avg=2.91µs  min=892ns   med=2.26µs  max=2.84ms   p(90)=3.88µs  p(95)=4.59µs   p(99.9)=28.1µs  
     http_req_connecting............: avg=325ns   min=0s      med=0s      max=2.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.63ms min=18.52ms med=35.11ms max=308.13ms p(90)=42.16ms p(95)=44.47ms  p(99.9)=61.34ms 
       { expected_response:true }...: avg=35.63ms min=18.52ms med=35.11ms max=308.13ms p(90)=42.16ms p(95)=44.47ms  p(99.9)=61.34ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 167407
     http_req_receiving.............: avg=69.21µs min=27.04µs med=57.67µs max=212.72ms p(90)=93.08µs p(95)=108.06µs p(99.9)=717.07µs
     http_req_sending...............: avg=21.89µs min=4.73µs  med=10.86µs max=113.12ms p(90)=17.77µs p(95)=21.14µs  p(99.9)=699.06µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.54ms min=18.39ms med=35.02ms max=301.36ms p(90)=42.07ms p(95)=44.38ms  p(99.9)=60.99ms 
     http_reqs......................: 167407  1372.456557/s
     iteration_duration.............: avg=35.85ms min=21.63ms med=35.31ms max=314.34ms p(90)=42.36ms p(95)=44.68ms  p(99.9)=61.84ms 
     iterations.....................: 167307  1371.636725/s
     success_rate...................: 100.00% ✓ 167307      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 190869     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   626 kB/s
     http_req_blocked...............: avg=4.34µs  min=1.05µs  med=2.72µs  max=5.15ms   p(90)=4.17µs   p(95)=4.74µs   p(99.9)=54.91µs 
     http_req_connecting............: avg=1.31µs  min=0s      med=0s      max=4.68ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.95ms min=20.89ms med=91.59ms max=315.06ms p(90)=114.49ms p(95)=122.97ms p(99.9)=220.7ms 
       { expected_response:true }...: avg=93.95ms min=20.89ms med=91.59ms max=315.06ms p(90)=114.49ms p(95)=122.97ms p(99.9)=220.7ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 63723
     http_req_receiving.............: avg=79.4µs  min=27.84µs med=72.76µs max=22.37ms  p(90)=106.17µs p(95)=117.97µs p(99.9)=560.79µs
     http_req_sending...............: avg=19.36µs min=4.94µs  med=13.66µs max=142.84ms p(90)=19.31µs  p(95)=21.2µs   p(99.9)=524.27µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.85ms min=20.79ms med=91.51ms max=314.56ms p(90)=114.39ms p(95)=122.86ms p(99.9)=220.62ms
     http_reqs......................: 63723   521.283676/s
     iteration_duration.............: avg=94.3ms  min=34.39ms med=91.85ms max=342.05ms p(90)=114.73ms p(95)=123.24ms p(99.9)=221.6ms 
     iterations.....................: 63623   520.46563/s
     success_rate...................: 100.00% ✓ 63623      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 176439     ✗ 0    
     data_received..................: 5.2 GB  42 MB/s
     data_sent......................: 71 MB   579 kB/s
     http_req_blocked...............: avg=4.71µs   min=1.33µs  med=3.34µs   max=2.88ms   p(90)=4.84µs   p(95)=5.44µs   p(99.9)=56.21µs 
     http_req_connecting............: avg=1.13µs   min=0s      med=0s       max=2.85ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.64ms min=20.02ms med=99.79ms  max=322.21ms p(90)=128.94ms p(95)=138.08ms p(99.9)=180.72ms
       { expected_response:true }...: avg=101.64ms min=20.02ms med=99.79ms  max=322.21ms p(90)=128.94ms p(95)=138.08ms p(99.9)=180.72ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58913
     http_req_receiving.............: avg=80.34µs  min=28.82µs med=72.83µs  max=82.33ms  p(90)=104.54µs p(95)=115.97µs p(99.9)=515.74µs
     http_req_sending...............: avg=24.67µs  min=5.22µs  med=14.85µs  max=166.19ms p(90)=20.47µs  p(95)=22.49µs  p(99.9)=637.18µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.54ms min=19.9ms  med=99.7ms   max=321.3ms  p(90)=128.83ms p(95)=137.95ms p(99.9)=180.62ms
     http_reqs......................: 58913   481.996899/s
     iteration_duration.............: avg=102.03ms min=32.1ms  med=100.08ms max=331.78ms p(90)=129.19ms p(95)=138.36ms p(99.9)=182.16ms
     iterations.....................: 58813   481.178748/s
     success_rate...................: 100.00% ✓ 58813      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-v3 (HotChocolate subgraphs) (v3.0.0-preview.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 153537     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   503 kB/s
     http_req_blocked...............: avg=4.85µs   min=1.08µs  med=2.85µs   max=3.78ms   p(90)=4.3µs    p(95)=4.84µs   p(99.9)=127.37µs
     http_req_connecting............: avg=1.81µs   min=0s      med=0s       max=3.74ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=116.83ms min=20.77ms med=115.24ms max=343.96ms p(90)=144.66ms p(95)=154.09ms p(99.9)=197.45ms
       { expected_response:true }...: avg=116.83ms min=20.77ms med=115.24ms max=343.96ms p(90)=144.66ms p(95)=154.09ms p(99.9)=197.45ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51279
     http_req_receiving.............: avg=85.92µs  min=28.62µs med=76.33µs  max=166.01ms p(90)=107.71µs p(95)=119.49µs p(99.9)=473.22µs
     http_req_sending...............: avg=25.25µs  min=5µs     med=14.53µs  max=136.31ms p(90)=19.71µs  p(95)=21.7µs   p(99.9)=569.89µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.72ms min=20.62ms med=115.14ms max=331.52ms p(90)=144.55ms p(95)=153.98ms p(99.9)=196.65ms
     http_reqs......................: 51279   419.171388/s
     iteration_duration.............: avg=117.27ms min=37.25ms med=115.52ms max=365.46ms p(90)=144.91ms p(95)=154.34ms p(99.9)=199.58ms
     iterations.....................: 51179   418.353955/s
     success_rate...................: 100.00% ✓ 51179      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-gateway (HotChocolate subgraphs) (2.14.4)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 97548      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   320 kB/s
     http_req_blocked...............: avg=6.04µs   min=1.16µs  med=2.89µs   max=3.61ms   p(90)=4.21µs   p(95)=4.72µs   p(99.9)=1.51ms  
     http_req_connecting............: avg=2.88µs   min=0s      med=0s       max=3.57ms   p(90)=0s       p(95)=0s       p(99.9)=1.46ms  
     http_req_duration..............: avg=183.88ms min=22.46ms med=184.35ms max=409.05ms p(90)=195.8ms  p(95)=200.83ms p(99.9)=274.55ms
       { expected_response:true }...: avg=183.88ms min=22.46ms med=184.35ms max=409.05ms p(90)=195.8ms  p(95)=200.83ms p(99.9)=274.55ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32616
     http_req_receiving.............: avg=88.9µs   min=30.64µs med=80.92µs  max=70.35ms  p(90)=110.61µs p(95)=121.29µs p(99.9)=536.02µs
     http_req_sending...............: avg=23.09µs  min=5.26µs  med=15.43µs  max=65.67ms  p(90)=19.67µs  p(95)=21.42µs  p(99.9)=424.71µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.76ms min=22.32ms med=184.25ms max=405.19ms p(90)=195.69ms p(95)=200.73ms p(99.9)=272.25ms
     http_reqs......................: 32616   266.104409/s
     iteration_duration.............: avg=184.64ms min=40.9ms  med=184.74ms max=416.52ms p(90)=196.08ms p(95)=201.15ms p(99.9)=279.39ms
     iterations.....................: 32516   265.288539/s
     success_rate...................: 100.00% ✓ 32516      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 96696      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=6.02µs   min=1.21µs  med=3.18µs   max=3.51ms   p(90)=4.56µs   p(95)=5.15µs   p(99.9)=1.26ms  
     http_req_connecting............: avg=2.65µs   min=0s      med=0s       max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=185.42ms min=17.46ms med=172.18ms max=773.09ms p(90)=214.45ms p(95)=234.31ms p(99.9)=698.68ms
       { expected_response:true }...: avg=185.42ms min=17.46ms med=172.18ms max=773.09ms p(90)=214.45ms p(95)=234.31ms p(99.9)=698.68ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32332
     http_req_receiving.............: avg=97.02µs  min=29.01µs med=86.81µs  max=135.33ms p(90)=116.21µs p(95)=127.57µs p(99.9)=603.21µs
     http_req_sending...............: avg=31.41µs  min=5.24µs  med=16.94µs  max=167.61ms p(90)=21.32µs  p(95)=23.06µs  p(99.9)=442.97µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.29ms min=17.33ms med=172.07ms max=772.96ms p(90)=214.32ms p(95)=234.15ms p(99.9)=698.56ms
     http_reqs......................: 32332   264.6593/s
     iteration_duration.............: avg=186.23ms min=36.94ms med=172.56ms max=773.33ms p(90)=214.82ms p(95)=235.17ms p(99.9)=699.07ms
     iterations.....................: 32232   263.840732/s
     success_rate...................: 100.00% ✓ 32232      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB


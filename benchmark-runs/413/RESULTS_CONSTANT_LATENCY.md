## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 2,470 | 2,566 | 2,462 | 1.5% |  |
| fusion-nightly-net-11 | 16.7.0-p.31 | 2,306 | 2,382 | 2,285 | 1.4% |  |
| fusion-nightly-net-10 | 16.7.0-p.31 | 2,261 | 2,323 | 2,252 | 1.1% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.31 | 1,949 | 2,005 | 1,930 | 1.2% |  |
| fusion-net-10 | 16.6.9 | 1,881 | 1,931 | 1,872 | 1.1% |  |
| hive-router | v0.3.5 | 1,862 | 1,925 | 1,851 | 1.3% |  |
| cosmo | 0.359.0 | 1,356 | 1,407 | 1,350 | 1.5% |  |
| caliban | 3.2.0 | 1,321 | 1,385 | 1,318 | 1.9% |  |
| grafbase | 0.53.5 | 1,297 | 1,329 | 1,282 | 1.3% |  |
| hive-gateway-router-runtime | 2.15.2 | 488 | 509 | 484 | 1.6% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 401 | 416 | 398 | 1.6% |  |
| apollo-router | v2.18.0 | 400 | 415 | 394 | 2.0% |  |
| apollo-gateway | 2.14.4 | 265 | 268 | 261 | 0.9% |  |
| hive-gateway | 2.15.2 | 259 | 265 | 258 | 1.0% |  |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 899739      ✗ 0     
     data_received..................: 26 GB   216 MB/s
     data_sent......................: 361 MB  3.0 MB/s
     http_req_blocked...............: avg=2.88µs  min=862ns   med=2.01µs  max=9.5ms    p(90)=3.62µs  p(95)=4.58µs   p(99.9)=35.08µs
     http_req_connecting............: avg=328ns   min=0s      med=0s      max=5.79ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.78ms min=12.46ms med=19.06ms max=274.67ms p(90)=23.71ms p(95)=25.86ms  p(99.9)=44.55ms
       { expected_response:true }...: avg=19.78ms min=12.46ms med=19.06ms max=274.67ms p(90)=23.71ms p(95)=25.86ms  p(99.9)=44.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 300013
     http_req_receiving.............: avg=83.92µs min=24.87µs med=45.98µs max=137.84ms p(90)=96.88µs p(95)=159.49µs p(99.9)=4.63ms 
     http_req_sending...............: avg=41.31µs min=4.58µs  med=8.59µs  max=69.64ms  p(90)=18.97µs p(95)=89.7µs   p(99.9)=3.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.66ms min=12.17ms med=18.97ms max=273.48ms p(90)=23.57ms p(95)=25.64ms  p(99.9)=43.74ms
     http_reqs......................: 300013  2470.955001/s
     iteration_duration.............: avg=19.99ms min=12.58ms med=19.27ms max=300.14ms p(90)=23.92ms p(95)=26.07ms  p(99.9)=44.97ms
     iterations.....................: 299913  2470.131385/s
     success_rate...................: 100.00% ✓ 299913      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.31)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 840285      ✗ 0     
     data_received..................: 25 GB   202 MB/s
     data_sent......................: 337 MB  2.8 MB/s
     http_req_blocked...............: avg=2.78µs   min=812ns   med=1.9µs   max=11.04ms  p(90)=3.47µs  p(95)=4.38µs  p(99.9)=27.17µs
     http_req_connecting............: avg=296ns    min=0s      med=0s      max=4.4ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=21.2ms   min=12.82ms med=20.46ms max=306.58ms p(90)=25.78ms p(95)=27.99ms p(99.9)=48.06ms
       { expected_response:true }...: avg=21.2ms   min=12.82ms med=20.46ms max=306.58ms p(90)=25.78ms p(95)=27.99ms p(99.9)=48.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280195
     http_req_receiving.............: avg=431.62µs min=51.68µs med=83.92µs max=152.23ms p(90)=1.21ms  p(95)=2.15ms  p(99.9)=14.53ms
     http_req_sending...............: avg=39.84µs  min=4.31µs  med=7.84µs  max=172.76ms p(90)=17.78µs p(95)=84.67µs p(99.9)=2.99ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=20.73ms  min=12.74ms med=20.03ms max=305.3ms  p(90)=25.1ms  p(95)=27.21ms p(99.9)=46.46ms
     http_reqs......................: 280195  2306.829374/s
     iteration_duration.............: avg=21.41ms  min=13.02ms med=20.66ms max=316.15ms p(90)=25.99ms p(95)=28.21ms p(99.9)=48.52ms
     iterations.....................: 280095  2306.00608/s
     success_rate...................: 100.00% ✓ 280095      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.31)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 823875      ✗ 0     
     data_received..................: 24 GB   198 MB/s
     data_sent......................: 330 MB  2.7 MB/s
     http_req_blocked...............: avg=2.46µs   min=792ns   med=1.9µs   max=10.67ms  p(90)=3.18µs  p(95)=3.92µs  p(99.9)=25.99µs
     http_req_connecting............: avg=146ns    min=0s      med=0s      max=1.95ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=21.62ms  min=13.21ms med=20.9ms  max=307.83ms p(90)=26.59ms p(95)=28.73ms p(99.9)=46.69ms
       { expected_response:true }...: avg=21.62ms  min=13.21ms med=20.9ms  max=307.83ms p(90)=26.59ms p(95)=28.73ms p(99.9)=46.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 274725
     http_req_receiving.............: avg=509.52µs min=49.04µs med=88.36µs max=210.57ms p(90)=1.47ms  p(95)=2.32ms  p(99.9)=14.86ms
     http_req_sending...............: avg=36.87µs  min=4.65µs  med=7.99µs  max=138.41ms p(90)=16.42µs p(95)=81.37µs p(99.9)=2.9ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=21.08ms  min=13.11ms med=20.38ms max=307.54ms p(90)=25.83ms p(95)=27.93ms p(99.9)=44.6ms 
     http_reqs......................: 274725  2261.800955/s
     iteration_duration.............: avg=21.83ms  min=13.38ms med=21.1ms  max=315.85ms p(90)=26.79ms p(95)=28.94ms p(99.9)=47.29ms
     iterations.....................: 274625  2260.977658/s
     success_rate...................: 100.00% ✓ 274625      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.31)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 712866      ✗ 0     
     data_received..................: 21 GB   171 MB/s
     data_sent......................: 286 MB  2.3 MB/s
     http_req_blocked...............: avg=2.88µs   min=832ns   med=2µs     max=7.35ms   p(90)=3.88µs  p(95)=4.68µs  p(99.9)=31.58µs
     http_req_connecting............: avg=354ns    min=0s      med=0s      max=7.32ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.02ms  min=17.25ms med=24.4ms  max=308.94ms p(90)=29.24ms p(95)=31.04ms p(99.9)=50.18ms
       { expected_response:true }...: avg=25.02ms  min=17.25ms med=24.4ms  max=308.94ms p(90)=29.24ms p(95)=31.04ms p(99.9)=50.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 237722
     http_req_receiving.............: avg=364.97µs min=49.97µs med=90.41µs max=215.52ms p(90)=1.01ms  p(95)=1.72ms  p(99.9)=10ms   
     http_req_sending...............: avg=36.23µs  min=4.51µs  med=8.29µs  max=250.66ms p(90)=19.16µs p(95)=56.92µs p(99.9)=2.32ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.62ms  min=17.04ms med=24.03ms max=307.48ms p(90)=28.72ms p(95)=30.46ms p(99.9)=48.57ms
     http_reqs......................: 237722  1949.396145/s
     iteration_duration.............: avg=25.23ms  min=17.5ms  med=24.61ms max=322.58ms p(90)=29.44ms p(95)=31.25ms p(99.9)=50.7ms 
     iterations.....................: 237622  1948.576113/s
     success_rate...................: 100.00% ✓ 237622      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-10 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 687984      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 276 MB  2.3 MB/s
     http_req_blocked...............: avg=3.35µs   min=972ns   med=2.53µs   max=10.25ms  p(90)=4.23µs  p(95)=4.99µs  p(99.9)=34.87µs
     http_req_connecting............: avg=381ns    min=0s      med=0s       max=3.58ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.93ms  min=17.35ms med=25.28ms  max=304.61ms p(90)=30.42ms p(95)=32.42ms p(99.9)=51.2ms 
       { expected_response:true }...: avg=25.93ms  min=17.35ms med=25.28ms  max=304.61ms p(90)=30.42ms p(95)=32.42ms p(99.9)=51.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 229428
     http_req_receiving.............: avg=484.92µs min=49.96µs med=110.71µs max=261.96ms p(90)=1.32ms  p(95)=1.94ms  p(99.9)=12.68ms
     http_req_sending...............: avg=35.01µs  min=4.72µs  med=9.69µs   max=35.5ms   p(90)=19.52µs p(95)=61.49µs p(99.9)=2.02ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.41ms  min=17.24ms med=24.8ms   max=304.08ms p(90)=29.74ms p(95)=31.63ms p(99.9)=49.05ms
     http_reqs......................: 229428  1881.667415/s
     iteration_duration.............: avg=26.15ms  min=17.6ms  med=25.5ms   max=325.21ms p(90)=30.63ms p(95)=32.63ms p(99.9)=51.85ms
     iterations.....................: 229328  1880.847259/s
     success_rate...................: 100.00% ✓ 229328      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 681015      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 273 MB  2.2 MB/s
     http_req_blocked...............: avg=3.58µs  min=1.03µs  med=2.74µs  max=4.35ms   p(90)=4.42µs  p(95)=5.17µs   p(99.9)=36.48µs
     http_req_connecting............: avg=457ns   min=0s      med=0s      max=4.31ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.19ms min=18.04ms med=25.73ms max=298.82ms p(90)=29.9ms  p(95)=31.37ms  p(99.9)=48.55ms
       { expected_response:true }...: avg=26.19ms min=18.04ms med=25.73ms max=298.82ms p(90)=29.9ms  p(95)=31.37ms  p(99.9)=48.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 227105
     http_req_receiving.............: avg=80.59µs min=25.74µs med=54.8µs  max=90.08ms  p(90)=99.82µs p(95)=130.24µs p(99.9)=2.4ms  
     http_req_sending...............: avg=33.92µs min=4.73µs  med=10.55µs max=124.81ms p(90)=18.52µs p(95)=27.28µs  p(99.9)=1.57ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.08ms min=17.95ms med=25.63ms max=289.18ms p(90)=29.79ms p(95)=31.22ms  p(99.9)=47.53ms
     http_reqs......................: 227105  1862.423459/s
     iteration_duration.............: avg=26.42ms min=18.39ms med=25.94ms max=308.21ms p(90)=30.12ms p(95)=31.58ms  p(99.9)=49.01ms
     iterations.....................: 227005  1861.603388/s
     success_rate...................: 100.00% ✓ 227005      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.359.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 496212      ✗ 0     
     data_received..................: 15 GB   119 MB/s
     data_sent......................: 199 MB  1.6 MB/s
     http_req_blocked...............: avg=4.01µs  min=1.14µs  med=3.04µs  max=4.3ms    p(90)=4.87µs   p(95)=5.68µs   p(99.9)=35.69µs
     http_req_connecting............: avg=623ns   min=0s      med=0s      max=4.24ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.03ms min=18.74ms med=35.41ms max=320.85ms p(90)=43.1ms   p(95)=45.61ms  p(99.9)=60.73ms
       { expected_response:true }...: avg=36.03ms min=18.74ms med=35.41ms max=320.85ms p(90)=43.1ms   p(95)=45.61ms  p(99.9)=60.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 165504
     http_req_receiving.............: avg=82.79µs min=26.27µs med=65.03µs max=25.86ms  p(90)=109.49µs p(95)=131.88µs p(99.9)=1.24ms 
     http_req_sending...............: avg=30.43µs min=5.23µs  med=12.61µs max=204.91ms p(90)=20.77µs  p(95)=26.01µs  p(99.9)=1.18ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=35.92ms min=18.61ms med=35.31ms max=320.6ms  p(90)=42.98ms  p(95)=45.48ms  p(99.9)=60.18ms
     http_reqs......................: 165504  1356.103236/s
     iteration_duration.............: avg=36.26ms min=21.29ms med=35.64ms max=331.02ms p(90)=43.32ms  p(95)=45.83ms  p(99.9)=61.08ms
     iterations.....................: 165404  1355.283858/s
     success_rate...................: 100.00% ✓ 165404      ✗ 0     
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

     checks.........................: 100.00% ✓ 483471      ✗ 0     
     data_received..................: 14 GB   116 MB/s
     data_sent......................: 194 MB  1.6 MB/s
     http_req_blocked...............: avg=4.82µs  min=981ns   med=2.89µs  max=8.82ms   p(90)=4.89µs   p(95)=5.71µs   p(99.9)=39.65µs
     http_req_connecting............: avg=1.55µs  min=0s      med=0s      max=8.79ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.98ms min=18.9ms  med=36.41ms max=302.14ms p(90)=43.85ms  p(95)=46.34ms  p(99.9)=61.36ms
       { expected_response:true }...: avg=36.98ms min=18.9ms  med=36.41ms max=302.14ms p(90)=43.85ms  p(95)=46.34ms  p(99.9)=61.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 161257
     http_req_receiving.............: avg=80.55µs min=26.46µs med=61.45µs max=238.7ms  p(90)=103.34µs p(95)=124.48µs p(99.9)=1.57ms 
     http_req_sending...............: avg=29.47µs min=4.79µs  med=12.32µs max=231.19ms p(90)=20.7µs   p(95)=25.44µs  p(99.9)=1.28ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36.87ms min=18.77ms med=36.31ms max=300.88ms p(90)=43.73ms  p(95)=46.22ms  p(99.9)=60.93ms
     http_reqs......................: 161257  1321.274118/s
     iteration_duration.............: avg=37.22ms min=21.53ms med=36.63ms max=314.87ms p(90)=44.07ms  p(95)=46.56ms  p(99.9)=61.83ms
     iterations.....................: 161157  1320.454759/s
     success_rate...................: 100.00% ✓ 161157      ✗ 0     
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

     checks.........................: 100.00% ✓ 474543      ✗ 0     
     data_received..................: 14 GB   114 MB/s
     data_sent......................: 190 MB  1.6 MB/s
     http_req_blocked...............: avg=4.23µs  min=1.04µs  med=3µs     max=4.46ms   p(90)=5.38µs  p(95)=6.39µs   p(99.9)=45.23µs
     http_req_connecting............: avg=659ns   min=0s      med=0s      max=4.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=37.65ms min=18.19ms med=37.4ms  max=311.94ms p(90)=44.48ms p(95)=46.54ms  p(99.9)=63.4ms 
       { expected_response:true }...: avg=37.65ms min=18.19ms med=37.4ms  max=311.94ms p(90)=44.48ms p(95)=46.54ms  p(99.9)=63.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 158281
     http_req_receiving.............: avg=91.79µs min=26.5µs  med=58.37µs max=148.26ms p(90)=125.5µs p(95)=178.01µs p(99.9)=2.47ms 
     http_req_sending...............: avg=36.79µs min=4.85µs  med=11.24µs max=159.73ms p(90)=24.56µs p(95)=82.77µs  p(99.9)=2.08ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.53ms min=18.1ms  med=37.28ms max=311.42ms p(90)=44.36ms p(95)=46.4ms   p(99.9)=62.77ms
     http_reqs......................: 158281  1297.534255/s
     iteration_duration.............: avg=37.92ms min=20.65ms med=37.65ms max=327.08ms p(90)=44.71ms p(95)=46.78ms  p(99.9)=63.9ms 
     iterations.....................: 158181  1296.714488/s
     success_rate...................: 100.00% ✓ 158181      ✗ 0     
     vus............................: 1       min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 178806     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 72 MB   586 kB/s
     http_req_blocked...............: avg=5.47µs   min=1.37µs  med=3.59µs  max=4.14ms   p(90)=5.25µs   p(95)=5.97µs   p(99.9)=51.19µs 
     http_req_connecting............: avg=1.59µs   min=0s      med=0s      max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=100.28ms min=21.32ms med=98.07ms max=333.53ms p(90)=121.64ms p(95)=130.53ms p(99.9)=238.02ms
       { expected_response:true }...: avg=100.28ms min=21.32ms med=98.07ms max=333.53ms p(90)=121.64ms p(95)=130.53ms p(99.9)=238.02ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 59702
     http_req_receiving.............: avg=95.63µs  min=30.32µs med=81.78µs max=193.04ms p(90)=115.78µs p(95)=129.09µs p(99.9)=606.72µs
     http_req_sending...............: avg=25.14µs  min=5.87µs  med=16.02µs max=78.54ms  p(90)=21.91µs  p(95)=24.05µs  p(99.9)=622.43µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.16ms min=21.18ms med=97.95ms max=332.82ms p(90)=121.53ms p(95)=130.4ms  p(99.9)=237.42ms
     http_reqs......................: 59702   488.00966/s
     iteration_duration.............: avg=100.69ms min=34.05ms med=98.35ms max=349.06ms p(90)=121.89ms p(95)=130.83ms p(99.9)=241.27ms
     iterations.....................: 59602   487.192251/s
     success_rate...................: 100.00% ✓ 59602      ✗ 0    
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

     checks.........................: 100.00% ✓ 147018     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   482 kB/s
     http_req_blocked...............: avg=5.96µs   min=1.22µs  med=3.65µs   max=4.27ms   p(90)=5.31µs   p(95)=5.97µs   p(99.9)=465.19µs
     http_req_connecting............: avg=1.99µs   min=0s      med=0s       max=4.22ms   p(90)=0s       p(95)=0s       p(99.9)=409.25µs
     http_req_duration..............: avg=121.98ms min=21.7ms  med=120.27ms max=355.7ms  p(90)=150.69ms p(95)=160.54ms p(99.9)=207.43ms
       { expected_response:true }...: avg=121.98ms min=21.7ms  med=120.27ms max=355.7ms  p(90)=150.69ms p(95)=160.54ms p(99.9)=207.43ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49106
     http_req_receiving.............: avg=89.77µs  min=28.44µs med=84.44µs  max=63.8ms   p(90)=116.52µs p(95)=129.85µs p(99.9)=499.89µs
     http_req_sending...............: avg=26.8µs   min=5.58µs  med=17.52µs  max=114.03ms p(90)=23.23µs  p(95)=25.39µs  p(99.9)=609.55µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.87ms min=21.53ms med=120.16ms max=355.33ms p(90)=150.57ms p(95)=160.42ms p(99.9)=206.94ms
     http_reqs......................: 49106   401.24877/s
     iteration_duration.............: avg=122.47ms min=41.37ms med=120.59ms max=366.98ms p(90)=150.99ms p(95)=160.85ms p(99.9)=210.51ms
     iterations.....................: 49006   400.431663/s
     success_rate...................: 100.00% ✓ 49006      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.18.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 146655     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   481 kB/s
     http_req_blocked...............: avg=5.24µs   min=1.05µs  med=2.98µs   max=3.76ms   p(90)=4.5µs    p(95)=5.09µs   p(99.9)=676.83µs
     http_req_connecting............: avg=2.04µs   min=0s      med=0s       max=3.72ms   p(90)=0s       p(95)=0s       p(99.9)=655.03µs
     http_req_duration..............: avg=122.29ms min=20.35ms med=120.34ms max=327.14ms p(90)=153.14ms p(95)=163.83ms p(99.9)=207.83ms
       { expected_response:true }...: avg=122.29ms min=20.35ms med=120.34ms max=327.14ms p(90)=153.14ms p(95)=163.83ms p(99.9)=207.83ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48985
     http_req_receiving.............: avg=85.19µs  min=28.75µs med=79.35µs  max=57.5ms   p(90)=111.8µs  p(95)=123.65µs p(99.9)=500.24µs
     http_req_sending...............: avg=24.82µs  min=5.03µs  med=15.92µs  max=69.69ms  p(90)=21.51µs  p(95)=23.41µs  p(99.9)=482.1µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=122.18ms min=20.16ms med=120.23ms max=326.72ms p(90)=153.04ms p(95)=163.71ms p(99.9)=207.72ms
     http_reqs......................: 48985   400.429434/s
     iteration_duration.............: avg=122.77ms min=40.42ms med=120.66ms max=335.98ms p(90)=153.43ms p(95)=164.12ms p(99.9)=210.06ms
     iterations.....................: 48885   399.611981/s
     success_rate...................: 100.00% ✓ 48885      ✗ 0    
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

     checks.........................: 100.00% ✓ 97485      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   319 kB/s
     http_req_blocked...............: avg=6.58µs   min=1.48µs  med=3.65µs   max=3.56ms   p(90)=5.22µs   p(95)=5.85µs   p(99.9)=1.26ms  
     http_req_connecting............: avg=2.64µs   min=0s      med=0s       max=3.52ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=183.94ms min=23.34ms med=184.45ms max=412.44ms p(90)=197.4ms  p(95)=202.26ms p(99.9)=267.89ms
       { expected_response:true }...: avg=183.94ms min=23.34ms med=184.45ms max=412.44ms p(90)=197.4ms  p(95)=202.26ms p(99.9)=267.89ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32595
     http_req_receiving.............: avg=96.21µs  min=34.61µs med=87.35µs  max=70.61ms  p(90)=118.58µs p(95)=130.75µs p(99.9)=616.03µs
     http_req_sending...............: avg=41.41µs  min=6.93µs  med=18.4µs   max=181.98ms p(90)=23.49µs  p(95)=25.48µs  p(99.9)=514.9µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.8ms  min=23.21ms med=184.33ms max=411.86ms p(90)=197.28ms p(95)=202.14ms p(99.9)=267.73ms
     http_reqs......................: 32595   265.756136/s
     iteration_duration.............: avg=184.74ms min=55.48ms med=184.82ms max=420.04ms p(90)=197.68ms p(95)=202.56ms p(99.9)=270.29ms
     iterations.....................: 32495   264.940808/s
     success_rate...................: 100.00% ✓ 32495      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 94515      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   311 kB/s
     http_req_blocked...............: avg=7.19µs   min=1.62µs  med=3.98µs   max=3.8ms    p(90)=5.67µs   p(95)=6.35µs   p(99.9)=1.41ms  
     http_req_connecting............: avg=2.89µs   min=0s      med=0s       max=3.76ms   p(90)=0s       p(95)=0s       p(99.9)=1.38ms  
     http_req_duration..............: avg=189.69ms min=18.4ms  med=170.92ms max=864.16ms p(90)=239.85ms p(95)=270.39ms p(99.9)=744.63ms
       { expected_response:true }...: avg=189.69ms min=18.4ms  med=170.92ms max=864.16ms p(90)=239.85ms p(95)=270.39ms p(99.9)=744.63ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31605
     http_req_receiving.............: avg=98.91µs  min=35.71µs med=91.71µs  max=41.92ms  p(90)=123.91µs p(95)=137.6µs  p(99.9)=711.57µs
     http_req_sending...............: avg=29.15µs  min=6.6µs   med=19.16µs  max=41.98ms  p(90)=24.39µs  p(95)=26.55µs  p(99.9)=545.7µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=189.56ms min=18.3ms  med=170.79ms max=864.03ms p(90)=239.7ms  p(95)=270.28ms p(99.9)=744.51ms
     http_reqs......................: 31605   259.000272/s
     iteration_duration.............: avg=190.53ms min=64.45ms med=171.36ms max=864.44ms p(90)=240.29ms p(95)=270.92ms p(99.9)=744.95ms
     iterations.....................: 31505   258.18078/s
     success_rate...................: 100.00% ✓ 31505      ✗ 0    
     vus............................: 21      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB


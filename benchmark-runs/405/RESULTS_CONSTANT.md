## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 3,010 | 3,211 | 3,001 | 2.5% |  |
| fusion-nightly-net-11 | 16.7.0-p.29 | 2,769 | 2,948 | 2,755 | 2.4% |  |
| fusion-nightly-net-10 | 16.7.0-p.29 | 2,679 | 2,830 | 2,657 | 2.2% |  |
| hive-router | v0.3.5 | 2,644 | 2,826 | 2,627 | 2.6% |  |
| fusion-net-10 | 16.6.8 | 2,516 | 2,630 | 2,509 | 1.7% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.29 | 2,497 | 2,639 | 2,475 | 2.2% |  |
| grafbase | 0.53.5 | 1,643 | 1,697 | 1,632 | 1.2% |  |
| cosmo | 0.359.0 | 1,431 | 1,488 | 1,429 | 1.5% |  |
| caliban | 3.2.0 | 1,403 | 1,461 | 1,388 | 1.6% |  |
| hive-gateway-router-runtime | 2.15.2 | 516 | 533 | 513 | 1.4% |  |
| apollo-router | v2.18.0 | 410 | 431 | 407 | 2.3% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 380 | 397 | 377 | 1.8% |  |
| hive-gateway | 2.15.2 | 263 | 270 | 262 | 1.0% |  |
| apollo-gateway | 2.14.4 | 262 | 266 | 259 | 0.8% |  |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1084653     ✗ 0     
     data_received..................: 32 GB   263 MB/s
     data_sent......................: 435 MB  3.6 MB/s
     http_req_blocked...............: avg=3.01µs  min=782ns    med=2.14µs  max=14.96ms  p(90)=3.52µs  p(95)=4.23µs   p(99.9)=32.03µs
     http_req_connecting............: avg=318ns   min=0s       med=0s      max=5.62ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.37ms min=951.01µs med=15.91ms max=299.12ms p(90)=23.71ms p(95)=27.07ms  p(99.9)=47.75ms
       { expected_response:true }...: avg=16.37ms min=951.01µs med=15.91ms max=299.12ms p(90)=23.71ms p(95)=27.07ms  p(99.9)=47.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 361651
     http_req_receiving.............: avg=96.3µs  min=27.09µs  med=48.92µs max=71.35ms  p(90)=91.32µs p(95)=186.04µs p(99.9)=7.8ms  
     http_req_sending...............: avg=52.74µs min=4.76µs   med=8.91µs  max=139.56ms p(90)=15.28µs p(95)=103.19µs p(99.9)=8.44ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.22ms min=895.05µs med=15.8ms  max=296.87ms p(90)=23.52ms p(95)=26.79ms  p(99.9)=46.52ms
     http_reqs......................: 361651  3010.253942/s
     iteration_duration.............: avg=16.58ms min=1.66ms   med=16.11ms max=321.1ms  p(90)=23.92ms p(95)=27.31ms  p(99.9)=48.39ms
     iterations.....................: 361551  3009.421578/s
     success_rate...................: 100.00% ✓ 361551      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.29)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 998265      ✗ 0     
     data_received..................: 29 GB   243 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=3.55µs   min=1µs     med=2.62µs  max=16.46ms  p(90)=4.38µs  p(95)=5.21µs   p(99.9)=39.59µs
     http_req_connecting............: avg=274ns    min=0s      med=0s      max=3.65ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.79ms  min=1.39ms  med=16.74ms max=297.69ms p(90)=25.41ms p(95)=29.39ms  p(99.9)=52.82ms
       { expected_response:true }...: avg=17.79ms  min=1.39ms  med=16.74ms max=297.69ms p(90)=25.41ms p(95)=29.39ms  p(99.9)=52.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332855
     http_req_receiving.............: avg=978.19µs min=52.02µs med=98.89µs max=148.77ms p(90)=2.84ms  p(95)=4.34ms   p(99.9)=27.94ms
     http_req_sending...............: avg=53.28µs  min=4.59µs  med=9.55µs  max=46.59ms  p(90)=19.62µs p(95)=106.58µs p(99.9)=6.66ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.76ms  min=1.32ms  med=15.73ms max=297.05ms p(90)=23.99ms p(95)=27.92ms  p(99.9)=49.88ms
     http_reqs......................: 332855  2769.516492/s
     iteration_duration.............: avg=18.02ms  min=2.27ms  med=16.95ms max=309.11ms p(90)=25.64ms p(95)=29.64ms  p(99.9)=53.58ms
     iterations.....................: 332755  2768.684443/s
     success_rate...................: 100.00% ✓ 332755      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.29)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 965970      ✗ 0     
     data_received..................: 28 GB   235 MB/s
     data_sent......................: 387 MB  3.2 MB/s
     http_req_blocked...............: avg=4.01µs   min=1.01µs  med=2.58µs  max=18.8ms   p(90)=4.13µs  p(95)=4.85µs   p(99.9)=36.61µs 
     http_req_connecting............: avg=850ns    min=0s      med=0s      max=18.68ms  p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=18.39ms  min=1.39ms  med=16.12ms max=267.41ms p(90)=29.24ms p(95)=35.28ms  p(99.9)=103.22ms
       { expected_response:true }...: avg=18.39ms  min=1.39ms  med=16.12ms max=267.41ms p(90)=29.24ms p(95)=35.28ms  p(99.9)=103.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 322090
     http_req_receiving.............: avg=643.24µs min=52.67µs med=94.51µs max=133.48ms p(90)=1.37ms  p(95)=2.57ms   p(99.9)=27.53ms 
     http_req_sending...............: avg=52.82µs  min=4.91µs  med=9.58µs  max=218.89ms p(90)=17.84µs p(95)=104.58µs p(99.9)=6.09ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=17.7ms   min=1.31ms  med=15.53ms max=262ms    p(90)=28.13ms p(95)=34.03ms  p(99.9)=101.66ms
     http_reqs......................: 322090  2679.977091/s
     iteration_duration.............: avg=18.62ms  min=1.87ms  med=16.34ms max=287.23ms p(90)=29.47ms p(95)=35.54ms  p(99.9)=104.23ms
     iterations.....................: 321990  2679.145032/s
     success_rate...................: 100.00% ✓ 321990      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 953415      ✗ 0     
     data_received..................: 28 GB   231 MB/s
     data_sent......................: 382 MB  3.2 MB/s
     http_req_blocked...............: avg=3.05µs  min=892ns   med=2.19µs  max=19.18ms  p(90)=3.9µs   p(95)=4.75µs   p(99.9)=36.06µs
     http_req_connecting............: avg=299ns   min=0s      med=0s      max=3.5ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=18.65ms min=1.67ms  med=18.39ms max=287.96ms p(90)=25.51ms p(95)=27.95ms  p(99.9)=47.61ms
       { expected_response:true }...: avg=18.65ms min=1.67ms  med=18.39ms max=287.96ms p(90)=25.51ms p(95)=27.95ms  p(99.9)=47.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 317905
     http_req_receiving.............: avg=94.52µs min=27.05µs med=51.11µs max=167.2ms  p(90)=97.05µs p(95)=155.13µs p(99.9)=7.18ms 
     http_req_sending...............: avg=46.06µs min=4.52µs  med=9.49µs  max=37.86ms  p(90)=18.59µs p(95)=100.28µs p(99.9)=4.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=18.51ms min=1.58ms  med=18.27ms max=275.98ms p(90)=25.35ms p(95)=27.73ms  p(99.9)=46.72ms
     http_reqs......................: 317905  2644.454565/s
     iteration_duration.............: avg=18.86ms min=3.07ms  med=18.59ms max=298.64ms p(90)=25.71ms p(95)=28.18ms  p(99.9)=48.46ms
     iterations.....................: 317805  2643.622727/s
     success_rate...................: 100.00% ✓ 317805      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-10 (HotChocolate subgraphs) (16.6.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 907131      ✗ 0     
     data_received..................: 27 GB   221 MB/s
     data_sent......................: 364 MB  3.0 MB/s
     http_req_blocked...............: avg=2.87µs   min=832ns  med=2.05µs  max=21.7ms   p(90)=3.57µs  p(95)=4.34µs  p(99.9)=33.33µs 
     http_req_connecting............: avg=295ns    min=0s     med=0s      max=3.72ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=19.62ms  min=1.51ms med=16.53ms max=274.61ms p(90)=32.27ms p(95)=39.42ms p(99.9)=137.17ms
       { expected_response:true }...: avg=19.62ms  min=1.51ms med=16.53ms max=274.61ms p(90)=32.27ms p(95)=39.42ms p(99.9)=137.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 302477
     http_req_receiving.............: avg=562.84µs min=50.2µs med=93µs    max=143.53ms p(90)=1.06ms  p(95)=1.85ms  p(99.9)=26.83ms 
     http_req_sending...............: avg=42.02µs  min=4.44µs med=8.6µs   max=102.32ms p(90)=16.8µs  p(95)=83.63µs p(99.9)=3.71ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=19.01ms  min=1.44ms med=16.01ms max=274.51ms p(90)=31.34ms p(95)=38.3ms  p(99.9)=136.42ms
     http_reqs......................: 302477  2516.208869/s
     iteration_duration.............: avg=19.83ms  min=2.41ms med=16.73ms max=308.88ms p(90)=32.49ms p(95)=39.66ms p(99.9)=138.39ms
     iterations.....................: 302377  2515.377001/s
     success_rate...................: 100.00% ✓ 302377      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.29)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 900399      ✗ 0     
     data_received..................: 26 GB   219 MB/s
     data_sent......................: 361 MB  3.0 MB/s
     http_req_blocked...............: avg=3.03µs  min=882ns   med=2.21µs  max=17.32ms  p(90)=3.87µs  p(95)=4.67µs  p(99.9)=33.46µs 
     http_req_connecting............: avg=279ns   min=0s      med=0s      max=4.77ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=19.75ms min=1.79ms  med=17.66ms max=303.55ms p(90)=30.8ms  p(95)=36.6ms  p(99.9)=101.73ms
       { expected_response:true }...: avg=19.75ms min=1.79ms  med=17.66ms max=303.55ms p(90)=30.8ms  p(95)=36.6ms  p(99.9)=101.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 300233
     http_req_receiving.............: avg=659.6µs min=51.97µs med=96.84µs max=136.51ms p(90)=1.47ms  p(95)=2.61ms  p(99.9)=25.97ms 
     http_req_sending...............: avg=45.84µs min=4.7µs   med=9.01µs  max=219.25ms p(90)=19.11µs p(95)=95.93µs p(99.9)=4.13ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=19.05ms min=1.68ms  med=17.02ms max=293.03ms p(90)=29.7ms  p(95)=35.39ms p(99.9)=100.25ms
     http_reqs......................: 300233  2497.129606/s
     iteration_duration.............: avg=19.98ms min=2.98ms  med=17.87ms max=314.39ms p(90)=31.04ms p(95)=36.85ms p(99.9)=102.67ms
     iterations.....................: 300133  2496.297875/s
     success_rate...................: 100.00% ✓ 300133      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 592689      ✗ 0     
     data_received..................: 17 GB   144 MB/s
     data_sent......................: 238 MB  2.0 MB/s
     http_req_blocked...............: avg=4.53µs   min=821ns   med=2.26µs  max=9.58ms   p(90)=4.62µs   p(95)=5.75µs   p(99.9)=43.19µs
     http_req_connecting............: avg=1.52µs   min=0s      med=0s      max=9.54ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=30.12ms  min=2.21ms  med=29.54ms max=292.27ms p(90)=39.64ms  p(95)=43ms     p(99.9)=62.54ms
       { expected_response:true }...: avg=30.12ms  min=2.21ms  med=29.54ms max=292.27ms p(90)=39.64ms  p(95)=43ms     p(99.9)=62.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 197663
     http_req_receiving.............: avg=114.71µs min=26.51µs med=55.38µs max=222.31ms p(90)=125.59µs p(95)=195.17µs p(99.9)=4.4ms  
     http_req_sending...............: avg=39.48µs  min=4.39µs  med=9.1µs   max=45.05ms  p(90)=23.04µs  p(95)=104.9µs  p(99.9)=2.77ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=29.96ms  min=2.09ms  med=29.42ms max=164.62ms p(90)=39.49ms  p(95)=42.83ms  p(99.9)=61.67ms
     http_reqs......................: 197663  1643.274397/s
     iteration_duration.............: avg=30.36ms  min=4.26ms  med=29.76ms max=316.2ms  p(90)=39.86ms  p(95)=43.22ms  p(99.9)=63.1ms 
     iterations.....................: 197563  1642.443046/s
     success_rate...................: 100.00% ✓ 197563      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 516195      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.66µs  min=1.04µs  med=2.71µs  max=3.82ms   p(90)=4.39µs   p(95)=5.17µs  p(99.9)=38.96µs
     http_req_connecting............: avg=576ns   min=0s      med=0s      max=3.78ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=34.62ms min=2.4ms   med=33.7ms  max=305.18ms p(90)=49.51ms  p(95)=54.57ms p(99.9)=80.15ms
       { expected_response:true }...: avg=34.62ms min=2.4ms   med=33.7ms  max=305.18ms p(90)=49.51ms  p(95)=54.57ms p(99.9)=80.15ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 172165
     http_req_receiving.............: avg=82.28µs min=26.62µs med=65.46µs max=43.52ms  p(90)=106.53µs p(95)=126µs   p(99.9)=1.33ms 
     http_req_sending...............: avg=30.39µs min=4.94µs  med=11.63µs max=208.29ms p(90)=18.68µs  p(95)=23.59µs p(99.9)=1.19ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=34.51ms min=2.28ms  med=33.59ms max=304.81ms p(90)=49.4ms   p(95)=54.45ms p(99.9)=79.63ms
     http_reqs......................: 172165  1431.188489/s
     iteration_duration.............: avg=34.86ms min=4.66ms  med=33.92ms max=318.76ms p(90)=49.72ms  p(95)=54.78ms p(99.9)=80.67ms
     iterations.....................: 172065  1430.3572/s
     success_rate...................: 100.00% ✓ 172065      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 506172      ✗ 0     
     data_received..................: 15 GB   123 MB/s
     data_sent......................: 203 MB  1.7 MB/s
     http_req_blocked...............: avg=3.62µs  min=972ns   med=2.7µs   max=4.23ms   p(90)=4.62µs   p(95)=5.42µs   p(99.9)=40.63µs
     http_req_connecting............: avg=558ns   min=0s      med=0s      max=4.19ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=35.3ms  min=2.64ms  med=34.32ms max=293.96ms p(90)=49.95ms  p(95)=55.03ms  p(99.9)=83.2ms 
       { expected_response:true }...: avg=35.3ms  min=2.64ms  med=34.32ms max=293.96ms p(90)=49.95ms  p(95)=55.03ms  p(99.9)=83.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 168824
     http_req_receiving.............: avg=79.96µs min=27.14µs med=62.56µs max=107.43ms p(90)=105.05µs p(95)=124.85µs p(99.9)=1.57ms 
     http_req_sending...............: avg=28.58µs min=4.8µs   med=12.13µs max=184.25ms p(90)=20.53µs  p(95)=24.77µs  p(99.9)=1.26ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=35.19ms min=2.51ms  med=34.22ms max=293.84ms p(90)=49.84ms  p(95)=54.91ms  p(99.9)=82.95ms
     http_reqs......................: 168824  1403.118022/s
     iteration_duration.............: avg=35.55ms min=6.83ms  med=34.55ms max=309.65ms p(90)=50.17ms  p(95)=55.26ms  p(99.9)=83.62ms
     iterations.....................: 168724  1402.286909/s
     success_rate...................: 100.00% ✓ 168724      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 186447     ✗ 0    
     data_received..................: 5.5 GB  45 MB/s
     data_sent......................: 75 MB   620 kB/s
     http_req_blocked...............: avg=4.3µs    min=1.07µs  med=2.68µs  max=3.64ms   p(90)=4.12µs   p(95)=4.74µs   p(99.9)=46.2µs  
     http_req_connecting............: avg=1.41µs   min=0s      med=0s      max=3.6ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.16ms  min=4.4ms   med=93.13ms max=335.5ms  p(90)=116.51ms p(95)=128.59ms p(99.9)=224.91ms
       { expected_response:true }...: avg=96.16ms  min=4.4ms   med=93.13ms max=335.5ms  p(90)=116.51ms p(95)=128.59ms p(99.9)=224.91ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62249
     http_req_receiving.............: avg=138.66µs min=27.97µs med=71.71µs max=268.31ms p(90)=107.1µs  p(95)=120.17µs p(99.9)=681.49µs
     http_req_sending...............: avg=27.16µs  min=4.77µs  med=13.28µs max=125.1ms  p(90)=19.2µs   p(95)=21.15µs  p(99.9)=555.49µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=95.99ms  min=4.24ms  med=93.02ms max=256.58ms p(90)=116.35ms p(95)=128.29ms p(99.9)=221.48ms
     http_reqs......................: 62249   516.341304/s
     iteration_duration.............: avg=96.55ms  min=22.15ms med=93.37ms max=347.49ms p(90)=116.77ms p(95)=128.93ms p(99.9)=226.22ms
     iterations.....................: 62149   515.511827/s
     success_rate...................: 100.00% ✓ 62149      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 148440     ✗ 0    
     data_received..................: 4.3 GB  36 MB/s
     data_sent......................: 60 MB   493 kB/s
     http_req_blocked...............: avg=5.75µs   min=1.36µs  med=3.57µs   max=4.39ms   p(90)=5.1µs    p(95)=5.69µs   p(99.9)=246.32µs
     http_req_connecting............: avg=1.92µs   min=0s      med=0s       max=4.34ms   p(90)=0s       p(95)=0s       p(99.9)=136.82µs
     http_req_duration..............: avg=120.78ms min=5.4ms   med=118.41ms max=317.74ms p(90)=159.45ms p(95)=171.69ms p(99.9)=217.69ms
       { expected_response:true }...: avg=120.78ms min=5.4ms   med=118.41ms max=317.74ms p(90)=159.45ms p(95)=171.69ms p(99.9)=217.69ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49580
     http_req_receiving.............: avg=83.65µs  min=31.83µs med=79.94µs  max=2.39ms   p(90)=111.04µs p(95)=123.49µs p(99.9)=509.12µs
     http_req_sending...............: avg=23.37µs  min=6.16µs  med=16.09µs  max=77.13ms  p(90)=21.42µs  p(95)=23.35µs  p(99.9)=582.96µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=120.68ms min=5.26ms  med=118.31ms max=316.96ms p(90)=159.34ms p(95)=171.56ms p(99.9)=217.55ms
     http_reqs......................: 49580   410.837171/s
     iteration_duration.............: avg=121.3ms  min=30.88ms med=118.75ms max=337.71ms p(90)=159.77ms p(95)=172.06ms p(99.9)=222.22ms
     iterations.....................: 49480   410.008536/s
     success_rate...................: 100.00% ✓ 49480      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 137634     ✗ 0    
     data_received..................: 4.0 GB  33 MB/s
     data_sent......................: 55 MB   457 kB/s
     http_req_blocked...............: avg=5.19µs   min=1.09µs  med=2.94µs   max=3.5ms    p(90)=4.38µs   p(95)=4.94µs   p(99.9)=554.54µs
     http_req_connecting............: avg=2.02µs   min=0s      med=0s       max=3.46ms   p(90)=0s       p(95)=0s       p(99.9)=516.77µs
     http_req_duration..............: avg=130.3ms  min=5.84ms  med=127.88ms max=316.89ms p(90)=170.6ms  p(95)=183.38ms p(99.9)=235.27ms
       { expected_response:true }...: avg=130.3ms  min=5.84ms  med=127.88ms max=316.89ms p(90)=170.6ms  p(95)=183.38ms p(99.9)=235.27ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 45978
     http_req_receiving.............: avg=83.48µs  min=30.27µs med=78.91µs  max=21.82ms  p(90)=110.07µs p(95)=121.64µs p(99.9)=596.16µs
     http_req_sending...............: avg=19.83µs  min=5.15µs  med=15.31µs  max=63.39ms  p(90)=20.52µs  p(95)=22.3µs   p(99.9)=491.47µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=130.2ms  min=5.71ms  med=127.78ms max=316.43ms p(90)=170.49ms p(95)=183.28ms p(99.9)=235.13ms
     http_reqs......................: 45978   380.795649/s
     iteration_duration.............: avg=130.83ms min=39.63ms med=128.18ms max=339.52ms p(90)=170.9ms  p(95)=183.69ms p(99.9)=236.44ms
     iterations.....................: 45878   379.967436/s
     success_rate...................: 100.00% ✓ 45878      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 95136      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   316 kB/s
     http_req_blocked...............: avg=7.33µs   min=1.57µs  med=3.79µs   max=4.25ms   p(90)=5.33µs   p(95)=5.97µs   p(99.9)=1.63ms  
     http_req_connecting............: avg=3.26µs   min=0s      med=0s       max=4.21ms   p(90)=0s       p(95)=0s       p(99.9)=1.61ms  
     http_req_duration..............: avg=188.41ms min=5.97ms  med=170.24ms max=770.73ms p(90)=218.5ms  p(95)=254.3ms  p(99.9)=709.83ms
       { expected_response:true }...: avg=188.41ms min=5.97ms  med=170.24ms max=770.73ms p(90)=218.5ms  p(95)=254.3ms  p(99.9)=709.83ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31812
     http_req_receiving.............: avg=99.21µs  min=36.39µs med=93.67µs  max=54.65ms  p(90)=125.41µs p(95)=139.24µs p(99.9)=632.11µs
     http_req_sending...............: avg=32.37µs  min=5.82µs  med=19.11µs  max=62.03ms  p(90)=23.92µs  p(95)=25.85µs  p(99.9)=565.16µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=188.28ms min=5.87ms  med=170.12ms max=770.63ms p(90)=218.38ms p(95)=254.2ms  p(99.9)=709.72ms
     http_reqs......................: 31812   263.282323/s
     iteration_duration.............: avg=189.29ms min=48.21ms med=170.59ms max=770.98ms p(90)=218.92ms p(95)=255ms    p(99.9)=710.21ms
     iterations.....................: 31712   262.454703/s
     success_rate...................: 100.00% ✓ 31712      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 94968      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   315 kB/s
     http_req_blocked...............: avg=7.07µs   min=1.33µs  med=3.66µs   max=4.02ms   p(90)=5.06µs   p(95)=5.66µs   p(99.9)=1.57ms  
     http_req_connecting............: avg=3.17µs   min=0s      med=0s       max=3.98ms   p(90)=0s       p(95)=0s       p(99.9)=1.55ms  
     http_req_duration..............: avg=188.76ms min=7.81ms  med=193.83ms max=400.69ms p(90)=201.84ms p(95)=206.55ms p(99.9)=280.88ms
       { expected_response:true }...: avg=188.76ms min=7.81ms  med=193.83ms max=400.69ms p(90)=201.84ms p(95)=206.55ms p(99.9)=280.88ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31756
     http_req_receiving.............: avg=104.1µs  min=32.4µs  med=88.59µs  max=131.13ms p(90)=119.16µs p(95)=130.8µs  p(99.9)=567.5µs 
     http_req_sending...............: avg=31.59µs  min=5.95µs  med=17.65µs  max=105.78ms p(90)=22.13µs  p(95)=23.94µs  p(99.9)=570.71µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=188.62ms min=7.68ms  med=193.71ms max=381.9ms  p(90)=201.71ms p(95)=206.41ms p(99.9)=277.13ms
     http_reqs......................: 31756   262.489516/s
     iteration_duration.............: avg=189.65ms min=30.66ms med=194.11ms max=408.42ms p(90)=202.11ms p(95)=206.87ms p(99.9)=286.17ms
     iterations.....................: 31656   261.662934/s
     success_rate...................: 100.00% ✓ 31656      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB


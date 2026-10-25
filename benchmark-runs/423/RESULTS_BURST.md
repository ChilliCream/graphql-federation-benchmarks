## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-fed-net-11 | 16.7.0 | 3,775 | 3,975 | 3,727 | 2.1% |  |
| fusion-net-11 | 16.7.0 | 3,727 | 3,901 | 3,689 | 1.9% |  |
| fusion-aot-11 | 16.7.0 | 3,631 | 3,763 | 3,553 | 2.1% |  |
| fusion-fed-aot-11 | 16.7.0 | 3,535 | 3,736 | 3,475 | 2.3% |  |
| feddi-gateway | 3c75a7db8876 | 3,063 | 3,181 | 3,050 | 1.4% |  |
| hive-router | v0.3.5 | 2,383 | 2,506 | 2,320 | 2.5% |  |
| caliban | 3.2.0 | 1,386 | 1,442 | 1,382 | 1.6% |  |
| cosmo | 0.361.0 | 1,289 | 1,336 | 1,282 | 1.4% |  |
| hive-gateway-router-runtime | 2.15.2 | 469 | 480 | 469 | 0.8% |  |
| apollo-gateway | 2.14.4 | 235 | 241 | 233 | 1.0% |  |
| hive-gateway | 2.15.2 | 235 | 241 | 234 | 1.1% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (27466 across 9/9 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (7891 across 9/9 runs) |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (299136 across 9/9 runs) |


### Details

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 693219      ✗ 0     
     data_received..................: 20 GB   331 MB/s
     data_sent......................: 279 MB  4.5 MB/s
     http_req_blocked...............: avg=77.77µs  min=832ns   med=2.07µs  max=139.97ms p(90)=3.8µs    p(95)=5µs      p(99.9)=32.11ms 
     http_req_connecting............: avg=74.1µs   min=0s      med=0s      max=139.93ms p(90)=0s       p(95)=0s       p(99.9)=31.32ms 
     http_req_duration..............: avg=59.46ms  min=1.18ms  med=51.46ms max=276.39ms p(90)=122.44ms p(95)=149.41ms p(99.9)=210.62ms
       { expected_response:true }...: avg=59.46ms  min=1.18ms  med=51.46ms max=276.39ms p(90)=122.44ms p(95)=149.41ms p(99.9)=210.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 232073
     http_req_receiving.............: avg=1.16ms   min=47.72µs med=87.41µs max=118.37ms p(90)=3.05ms   p(95)=5.92ms   p(99.9)=56.81ms 
     http_req_sending...............: avg=149.51µs min=4.54µs  med=8.64µs  max=97.56ms  p(90)=18.4µs   p(95)=120.79µs p(99.9)=28.41ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=58.15ms  min=1.07ms  med=50.31ms max=274.63ms p(90)=121.09ms p(95)=148.12ms p(99.9)=201.32ms
     http_reqs......................: 232073  3775.662314/s
     iteration_duration.............: avg=61.66ms  min=1.9ms   med=52.73ms max=525.97ms p(90)=126.97ms p(95)=155.57ms p(99.9)=246.35ms
     iterations.....................: 231073  3759.393027/s
     success_rate...................: 100.00% ✓ 231073      ✗ 0     
     vus............................: 76      min=0         max=493 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 680484      ✗ 0     
     data_received..................: 20 GB   327 MB/s
     data_sent......................: 274 MB  4.5 MB/s
     http_req_blocked...............: avg=100.81µs min=992ns    med=2.8µs   max=150.57ms p(90)=4.51µs   p(95)=5.75µs   p(99.9)=44.42ms 
     http_req_connecting............: avg=95µs     min=0s       med=0s      max=150.01ms p(90)=0s       p(95)=0s       p(99.9)=43.81ms 
     http_req_duration..............: avg=60.02ms  min=863.25µs med=52.54ms max=352.97ms p(90)=121.2ms  p(95)=148.53ms p(99.9)=221.08ms
       { expected_response:true }...: avg=60.02ms  min=863.25µs med=52.54ms max=352.97ms p(90)=121.2ms  p(95)=148.53ms p(99.9)=221.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 227828
     http_req_receiving.............: avg=1.26ms   min=48.05µs  med=88.35µs max=204.86ms p(90)=2.5ms    p(95)=6.59ms   p(99.9)=70.33ms 
     http_req_sending...............: avg=169.48µs min=4.28µs   med=9.69µs  max=125.66ms p(90)=18.9µs   p(95)=124.34µs p(99.9)=33.57ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=58.59ms  min=779.41µs med=51.44ms max=313.31ms p(90)=119.64ms p(95)=147.04ms p(99.9)=209.01ms
     http_reqs......................: 227828  3727.026719/s
     iteration_duration.............: avg=62.81ms  min=1.5ms    med=53.82ms max=481.27ms p(90)=128.08ms p(95)=158.21ms p(99.9)=266.04ms
     iterations.....................: 226828  3710.66777/s
     success_rate...................: 100.00% ✓ 226828      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 664083      ✗ 0     
     data_received..................: 20 GB   318 MB/s
     data_sent......................: 267 MB  4.4 MB/s
     http_req_blocked...............: avg=69.78µs  min=812ns    med=2.22µs  max=116.71ms p(90)=4.14µs   p(95)=5.44µs   p(99.9)=29.2ms  
     http_req_connecting............: avg=66.18µs  min=0s       med=0s      max=115.34ms p(90)=0s       p(95)=0s       p(99.9)=28.91ms 
     http_req_duration..............: avg=62.35ms  min=908.4µs  med=54.69ms max=322.42ms p(90)=126.21ms p(95)=153.72ms p(99.9)=218.41ms
       { expected_response:true }...: avg=62.35ms  min=908.4µs  med=54.69ms max=322.42ms p(90)=126.21ms p(95)=153.72ms p(99.9)=218.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 222361
     http_req_receiving.............: avg=2.04ms   min=51.1µs   med=89.79µs max=229.19ms p(90)=6.69ms   p(95)=10.08ms  p(99.9)=64.88ms 
     http_req_sending...............: avg=139.25µs min=4.4µs    med=8.85µs  max=156.56ms p(90)=20.02µs  p(95)=123.68µs p(99.9)=26.28ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=60.17ms  min=837.44µs med=51.8ms  max=307.99ms p(90)=124.52ms p(95)=152.32ms p(99.9)=213.95ms
     http_reqs......................: 222361  3631.002761/s
     iteration_duration.............: avg=64.37ms  min=1.7ms    med=56.06ms max=374.68ms p(90)=130.22ms p(95)=158.75ms p(99.9)=247.45ms
     iterations.....................: 221361  3614.673446/s
     success_rate...................: 100.00% ✓ 221361      ✗ 0     
     vus............................: 68      min=0         max=495 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 649794      ✗ 0     
     data_received..................: 19 GB   310 MB/s
     data_sent......................: 261 MB  4.2 MB/s
     http_req_blocked...............: avg=62.14µs  min=821ns   med=2.1µs   max=120.73ms p(90)=3.88µs   p(95)=5.18µs   p(99.9)=23.98ms 
     http_req_connecting............: avg=58µs     min=0s      med=0s      max=120.66ms p(90)=0s       p(95)=0s       p(99.9)=22.7ms  
     http_req_duration..............: avg=64.25ms  min=1.27ms  med=56.16ms max=333.65ms p(90)=129.95ms p(95)=159.4ms  p(99.9)=223.68ms
       { expected_response:true }...: avg=64.25ms  min=1.27ms  med=56.16ms max=333.65ms p(90)=129.95ms p(95)=159.4ms  p(99.9)=223.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 217598
     http_req_receiving.............: avg=1.89ms   min=53.86µs med=94.68µs max=263.06ms p(90)=5.82ms   p(95)=8.72ms   p(99.9)=51.31ms 
     http_req_sending...............: avg=122.17µs min=4.62µs  med=8.77µs  max=80.69ms  p(90)=19.75µs  p(95)=120.81µs p(99.9)=22.47ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=62.24ms  min=1.2ms   med=53.54ms max=333.47ms p(90)=128.54ms p(95)=158.21ms p(99.9)=220.81ms
     http_reqs......................: 217598  3535.129513/s
     iteration_duration.............: avg=65.79ms  min=2.03ms  med=57.35ms max=345.26ms p(90)=132.69ms p(95)=162.4ms  p(99.9)=252.52ms
     iterations.....................: 216598  3518.883364/s
     success_rate...................: 100.00% ✓ 216598      ✗ 0     
     vus............................: 82      min=0         max=492 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 559863      ✗ 0     
     data_received..................: 16 GB   268 MB/s
     data_sent......................: 225 MB  3.7 MB/s
     http_req_blocked...............: avg=43.1µs   min=912ns    med=2.73µs  max=109.53ms p(90)=4.8µs    p(95)=6.11µs   p(99.9)=9.11ms  
     http_req_connecting............: avg=39.28µs  min=0s       med=0s      max=102.61ms p(90)=0s       p(95)=0s       p(99.9)=9.02ms  
     http_req_duration..............: avg=75.17ms  min=942.39µs med=66.45ms max=335.45ms p(90)=150.99ms p(95)=177.23ms p(99.9)=255.79ms
       { expected_response:true }...: avg=75.17ms  min=942.39µs med=66.45ms max=335.45ms p(90)=150.99ms p(95)=177.23ms p(99.9)=255.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 187621
     http_req_receiving.............: avg=235.11µs min=26.82µs  med=54.12µs max=103.74ms p(90)=195.5µs  p(95)=404.84µs p(99.9)=33.1ms  
     http_req_sending...............: avg=109.26µs min=4.68µs   med=10.3µs  max=160.51ms p(90)=21.6µs   p(95)=142.01µs p(99.9)=20.22ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=74.83ms  min=887.23µs med=66.15ms max=335.37ms p(90)=150.3ms  p(95)=176.44ms p(99.9)=253.65ms
     http_reqs......................: 187621  3063.856801/s
     iteration_duration.............: avg=76.36ms  min=1.39ms   med=67.46ms max=373.33ms p(90)=152.43ms p(95)=179.26ms p(99.9)=272.21ms
     iterations.....................: 186621  3047.526769/s
     success_rate...................: 100.00% ✓ 186621      ✗ 0     
     vus............................: 67      min=0         max=495 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 439389      ✗ 0     
     data_received..................: 13 GB   209 MB/s
     data_sent......................: 177 MB  2.9 MB/s
     http_req_blocked...............: avg=17.64µs  min=862ns   med=2.54µs  max=67.59ms  p(90)=4.63µs   p(95)=5.89µs   p(99.9)=3.41ms  
     http_req_connecting............: avg=13.85µs  min=0s      med=0s      max=67.39ms  p(90)=0s       p(95)=0s       p(99.9)=3.13ms  
     http_req_duration..............: avg=96.45ms  min=1.47ms  med=90.15ms max=314.54ms p(90)=188.78ms p(95)=204.58ms p(99.9)=257.6ms 
       { expected_response:true }...: avg=96.45ms  min=1.47ms  med=90.15ms max=314.54ms p(90)=188.78ms p(95)=204.58ms p(99.9)=257.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 147463
     http_req_receiving.............: avg=121.84µs min=27.23µs med=56.82µs max=90.46ms  p(90)=134.06µs p(95)=345.8µs  p(99.9)=9.41ms  
     http_req_sending...............: avg=69.59µs  min=4.56µs  med=10.28µs max=277.42ms p(90)=20.71µs  p(95)=121.75µs p(99.9)=8.54ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.26ms  min=1.41ms  med=89.98ms max=312.21ms p(90)=188.55ms p(95)=204.29ms p(99.9)=256.57ms
     http_reqs......................: 147463  2383.452894/s
     iteration_duration.............: avg=97.36ms  min=4.77ms  med=91.2ms  max=325.87ms p(90)=189.24ms p(95)=205.03ms p(99.9)=259.02ms
     iterations.....................: 146463  2367.289837/s
     success_rate...................: 100.00% ✓ 146463      ✗ 0     
     vus............................: 47      min=0         max=500 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 258156      ✗ 0    
     data_received..................: 7.6 GB  121 MB/s
     data_sent......................: 105 MB  1.7 MB/s
     http_req_blocked...............: avg=7.14µs   min=1.05µs med=2.89µs   max=15.32ms  p(90)=5.26µs   p(95)=6.37µs   p(99.9)=668.03µs
     http_req_connecting............: avg=3.47µs   min=0s     med=0s       max=15.25ms  p(90)=0s       p(95)=0s       p(99.9)=597.52µs
     http_req_duration..............: avg=163.88ms min=2.14ms med=134.5ms  max=936.32ms p(90)=344.79ms p(95)=411.03ms p(99.9)=677.08ms
       { expected_response:true }...: avg=163.88ms min=2.14ms med=134.5ms  max=936.32ms p(90)=344.79ms p(95)=411.03ms p(99.9)=677.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 87052
     http_req_receiving.............: avg=85.36µs  min=28.1µs med=64.8µs   max=127.67ms p(90)=110.72µs p(95)=134.59µs p(99.9)=2.01ms  
     http_req_sending...............: avg=42.35µs  min=5.13µs med=12.91µs  max=186.18ms p(90)=21.7µs   p(95)=26.68µs  p(99.9)=5.1ms   
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=163.75ms min=2.09ms med=134.35ms max=936.26ms p(90)=344.67ms p(95)=410.92ms p(99.9)=677.01ms
     http_reqs......................: 87052   1386.83373/s
     iteration_duration.............: avg=166.05ms min=6.78ms med=136.95ms max=936.49ms p(90)=346.17ms p(95)=412.63ms p(99.9)=678.09ms
     iterations.....................: 86052   1370.902635/s
     success_rate...................: 100.00% ✓ 86052       ✗ 0    
     vus............................: 91      min=0         max=500
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.361.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 240333      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 97 MB   1.5 MB/s
     http_req_blocked...............: avg=6.59µs   min=1.15µs  med=3.04µs   max=12.38ms  p(90)=4.91µs   p(95)=5.99µs   p(99.9)=583.02µs
     http_req_connecting............: avg=2.88µs   min=0s      med=0s       max=12.31ms  p(90)=0s       p(95)=0s       p(99.9)=497.81µs
     http_req_duration..............: avg=175.84ms min=2.15ms  med=173.5ms  max=500.03ms p(90)=329.92ms p(95)=353.52ms p(99.9)=431.84ms
       { expected_response:true }...: avg=175.84ms min=2.15ms  med=173.5ms  max=500.03ms p(90)=329.92ms p(95)=353.52ms p(99.9)=431.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81111
     http_req_receiving.............: avg=87.91µs  min=26.77µs med=66.33µs  max=90.12ms  p(90)=108.77µs p(95)=129.38µs p(99.9)=2.41ms  
     http_req_sending...............: avg=37.46µs  min=4.82µs  med=12.35µs  max=156.89ms p(90)=19.81µs  p(95)=24.58µs  p(99.9)=4.23ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.72ms min=2.08ms  med=173.41ms max=499.91ms p(90)=329.79ms p(95)=353.4ms  p(99.9)=431.68ms
     http_reqs......................: 81111   1289.943205/s
     iteration_duration.............: avg=178.29ms min=4.59ms  med=176.26ms max=500.3ms  p(90)=330.78ms p(95)=354.11ms p(99.9)=432.73ms
     iterations.....................: 80111   1274.039774/s
     success_rate...................: 100.00% ✓ 80111       ✗ 0    
     vus............................: 51      min=0         max=499
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 88851      ✗ 0    
     data_received..................: 2.7 GB  41 MB/s
     data_sent......................: 37 MB   563 kB/s
     http_req_blocked...............: avg=10.13µs  min=1.17µs  med=3.53µs   max=4.95ms   p(90)=5.44µs   p(95)=6.57µs   p(99.9)=1.72ms
     http_req_connecting............: avg=5.41µs   min=0s      med=0s       max=4.87ms   p(90)=0s       p(95)=0s       p(99.9)=1.65ms
     http_req_duration..............: avg=469.29ms min=4.32ms  med=435.05ms max=2.1s     p(90)=926.14ms p(95)=1.01s    p(99.9)=1.56s 
       { expected_response:true }...: avg=469.29ms min=4.32ms  med=435.05ms max=2.1s     p(90)=926.14ms p(95)=1.01s    p(99.9)=1.56s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 30617
     http_req_receiving.............: avg=99.08µs  min=28.52µs med=80.99µs  max=147.77ms p(90)=118.84µs p(95)=133.34µs p(99.9)=1.26ms
     http_req_sending...............: avg=35.89µs  min=5.21µs  med=16.35µs  max=77.67ms  p(90)=23.09µs  p(95)=25.93µs  p(99.9)=2.89ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=469.16ms min=4.23ms  med=434.93ms max=2.1s     p(90)=926ms    p(95)=1.01s    p(99.9)=1.56s 
     http_reqs......................: 30617   469.191196/s
     iteration_duration.............: avg=485.36ms min=25.48ms med=454.29ms max=2.1s     p(90)=930.81ms p(95)=1.01s    p(99.9)=1.57s 
     iterations.....................: 29617   453.866664/s
     success_rate...................: 100.00% ✓ 29617      ✗ 0    
     vus............................: 67      min=0        max=496
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 45711      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   283 kB/s
     http_req_blocked...............: avg=15.97µs  min=1.1µs   med=3.55µs   max=17.11ms  p(90)=5.48µs   p(95)=7.17µs   p(99.9)=2.16ms
     http_req_connecting............: avg=10.6µs   min=0s      med=0s       max=17.06ms  p(90)=0s       p(95)=0s       p(99.9)=2.14ms
     http_req_duration..............: avg=894.49ms min=7.98ms  med=809.44ms max=3.08s    p(90)=1.83s    p(95)=1.94s    p(99.9)=2.78s 
       { expected_response:true }...: avg=894.49ms min=7.98ms  med=809.44ms max=3.08s    p(90)=1.83s    p(95)=1.94s    p(99.9)=2.78s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16237
     http_req_receiving.............: avg=114.95µs min=36.69µs med=93.25µs  max=195.58ms p(90)=134.14µs p(95)=151.36µs p(99.9)=1.08ms
     http_req_sending...............: avg=46.67µs  min=5.7µs   med=18.2µs   max=143.32ms p(90)=24.22µs  p(95)=27.95µs  p(99.9)=2.95ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=894.32ms min=7.84ms  med=809.19ms max=3.08s    p(90)=1.83s    p(95)=1.94s    p(99.9)=2.78s 
     http_reqs......................: 16237   235.647693/s
     iteration_duration.............: avg=953.23ms min=29.08ms med=899.25ms max=3.09s    p(90)=1.85s    p(95)=1.94s    p(99.9)=2.8s  
     iterations.....................: 15237   221.134686/s
     success_rate...................: 100.00% ✓ 15237      ✗ 0    
     vus............................: 31      min=0        max=500
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 45111      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 19 MB   283 kB/s
     http_req_blocked...............: avg=17.86µs  min=1.18µs  med=3.69µs   max=20.16ms p(90)=5.61µs   p(95)=7.29µs   p(99.9)=2.65ms
     http_req_connecting............: avg=12.3µs   min=0s      med=0s       max=20.07ms p(90)=0s       p(95)=0s       p(99.9)=2.63ms
     http_req_duration..............: avg=909.47ms min=5.82ms  med=823.28ms max=4.69s   p(90)=1.84s    p(95)=2.08s    p(99.9)=4.17s 
       { expected_response:true }...: avg=909.47ms min=5.82ms  med=823.28ms max=4.69s   p(90)=1.84s    p(95)=2.08s    p(99.9)=4.17s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16037
     http_req_receiving.............: avg=107.61µs min=34.14µs med=91.8µs   max=98.38ms p(90)=129.45µs p(95)=145.25µs p(99.9)=1.4ms 
     http_req_sending...............: avg=38.54µs  min=6.27µs  med=18.36µs  max=73.81ms p(90)=24.21µs  p(95)=28.13µs  p(99.9)=5.16ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=909.33ms min=5.73ms  med=823.17ms max=4.69s   p(90)=1.84s    p(95)=2.08s    p(99.9)=4.17s 
     http_reqs......................: 16037   235.763528/s
     iteration_duration.............: avg=969.99ms min=51.22ms med=895.86ms max=4.72s   p(90)=1.86s    p(95)=2.1s     p(99.9)=4.23s 
     iterations.....................: 15037   221.062304/s
     success_rate...................: 100.00% ✓ 15037      ✗ 0    
     vus............................: 27      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

